from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review
from reviews.forms import ReviewForm


def store_products(request):

    products = Product.objects.all()
    template = 'products/store_products.html'
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Your search criteria is empty')
                return redirect(reverse('store_products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'sorting': sort,
    }
    my_product = products.filter(image='')
    print(my_product)
    return render(request, template, context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    form = ReviewForm()
    template = 'products/product_details.html'

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
        'on_products_page': True,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """
    adding products to a store
    """
    if not request.user.is_superuser:
        messages.error(request, 'SORRY Only store owners have  access')
        return redirect(reverse('home:home'))
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "New product added successfully")
            return redirect(reverse('products:product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product please check your form for errors')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    editing products from a store
    """
    if not request.user.is_superuser:
        messages.error(request, 'SORRY Only store owners have  access')
        return redirect(reverse('home:home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} edited successfully')
            return redirect(reverse('products:product_detail', args=[product.id]))
        else:
            messages.error(request, f'Failed Edit {product.name} product please check your form for errors')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editig {product.name}')

    template = 'products/edit_product.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    editing products from a store
    """
    if not request.user.is_superuser:
        messages.error(request, 'SORRY Only store owners have  access')
        return redirect(reverse('home:home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products:store_products'))
