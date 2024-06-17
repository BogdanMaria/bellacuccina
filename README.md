# PP5 UNDER DEVELOPMENT
(Developer: Bogdan Maria)

![Mockup image]()


[View live website]()

## Table of Contents
0. [About](#about)
1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
2. [Business Model](#business-model)
    1. [SEO](#seo)
    2. [Marketing](#marketing)
    3. [Target Audience](#target-audience)
2. [User Experience](#user-experience)
    1. [User Requirements and Expectations](#user-requirements-and-expectations)
    2. [User Stories](#user-stories)
    3. [Site Owner Stories](#site-owner-stories)
3. [Design](#design)
    1. [Colours](#colours)
    2. [Fonts](#fonts)
    3. [Project Structure](#project-structure)
    4. [Database](#database)
    5. [Data Models](#data-models)
    6. [Wireframes](#wireframes)
    7. [Agile Design](#agile-design)
4. [Technologies Used](#technologies-used)
    1. [Languages & Frameworks](#languages--frameworks)
    2. [Libraries and Tools](#libraries--tools)
5. [Features](#features)
6. [Future Features](#future-features)

7. [Validation](#validation)
    1. [CSS](#css)
    2. [Html](#html)
    3. [Javascript](#javascript)
    4. [Python](#python)
    5. [Chrome Dev Tools Lighthouse](#lighthouse)
    6. [WAVE Validation](#wave)  
8. [Testing](#testing)

9. [Bugs](#bugs)

10. [Deployment](#deployment)
    1. [Heroku](#heroku)
    2. [AWS][#aws]
    2. [Forking GitHub Repo](#forking-the-github-repository)
    3. [Clone a GitHub Repo](#clone-a-github-repository)
12. [Credits](#credits)
    1. [Code](#code)
    2. [Tutorials](#tutorials)
    3. [Imagery](#imagery)
13. [Acknowledgements](#acknowledgements)

## Overview

BellaCuccina MArket Webstore is a Django full-stack e-commerce app designed to offer italin produce in an online shop. With its smooth user experience, dynamic content updates, and integration with the Stripe API, the webstore offers a reliable platform for customers to explore and purchase high-quality italian products. Webstore focuses on providing an effortless and logical interface. Through the use of AJAX calls,parts of the website content is updated dynamically, eliminating the need for page reloads and ensuring a seamless browsing experience. Users can explore various knife options, view detailed product descriptions, and add items to their shopping cart without interruptions.The underlying technology stack  includes the Django Full Stack Web Framework, which provides a solid foundation for developing scalable and robust web applications. Additionally, Bootstrap is utilized for front-end styling, resulting in a visually appealing and responsive design that adapts to different screen sizes.
To experience the  BellaCuccina Market Webstore, you can visit the deployed project using the provided link.
If you wish to test the purchase functionality, you can use the following mock payment details:

- Card Number: 4242424242424242
- Expiration Date: Any future date in the format MM/YY
- CVN: Any 3-digit number
- Postcode: Any 5-digit numeral

Please note that any payments made using actual payment cards will fail, and no charges will be incurred. The webstore is designed for demonstration purposes, and no orders made will be fulfilled.
Enjoy the BellaCuccina Market experince.
***
## Project (Site owner) Goals

- To offer users purchase of products listed on a webstore
- To give users a great user experience while visiting a webstore
- To give users option for buying as a guest or a registered user
- To allow user creating or updating an account
- To give users option to check the order history
- To give users option to leave a poduct review
- To give users option to save products on a wishlist

### User Goals

- View and search for products.
- Filter products based on criteria.
- Register and log into/out of an account.
- View and edit account profile.
- Add products to the shopping bag and make purchases.
- View order history.
- Write product reviews.
- Create and manage a wishlist.
- Contact the site owner or customer support.
- Sign up for a newsletter.

## Business Model



BellaCuccina Market was born out of a love for authentic Italian food and a desire to share the unparalleled quality and tradition of Italian ingredients with food enthusiasts around the world. From the rolling hills of Tuscany to the sun-drenched coastlines of Sicily, we source our products from trusted artisans and farmers who take pride in their craft, ensuring that every item meets the highest standards of quality and taste.

- Value Proposition:
    - Pasta: Discover our diverse collection of pasta, from classic spaghetti and penne to regional specialties like orecchiette and tagliatelle. Each variety is made using traditional methods and premium durum wheat, providing the perfect base for your favorite sauces and recipes.
    - Cured Meats: Our selection of cured meats includes an array of Italian delicacies such as prosciutto, salami, pancetta, and more. These artisanal meats are crafted using time-honored techniques and carefully aged to perfection, delivering rich, savory flavors that elevate any dish.
    - Fresh Produce: We bring you the freshest, highest-quality produce, from vibrant cherry tomatoes and crisp arugula to fragrant basil and robust zucchini. Our produce is sourced from local growers who prioritize sustainability and freshness, ensuring that you receive the best nature has to offer.

- Target market:
    - BellaCuccina Market's target market consists of a diverse group of consumers who share a passion for high-quality, authentic Italian food. 

- Customer Relationships:
    - Engage with customers through social media, email newsletters, and personalized communications to foster brand loyalty.
    -  Encourage customer feedback and reviews to continuously improve the product selection and overall shopping experience.

- Communication channels:
    - E-commerce website: Provide a user-friendly online platform where customers can browse, select, and purchase italian products.
    - Social media platforms: Utilize platforms like Instagram, Facebook, and Twitter to showcase the products, engage with the audience, and drive traffic to the webshop.

### SEO


### Marketing


### Target audience

- Home Cooks: Individuals who enjoy cooking at home and experimenting with authentic Italian recipes.
- Food Lovers: Consumers who appreciate the rich flavors and traditional methods of Italian cuisine.
- Food Connoisseurs: People who seek premium, artisanal ingredients for their culinary creations.
- Gourmet Food Enthusiasts: Customers who value high-quality, specialty food products.
- Quality-Conscious Shoppers: Consumers who look for minimally processed, natural ingredients.
- Italian Expatriates: Individuals living abroad who want to stay connected to their cultural roots through traditional Italian foods.

##### Back to [top](#table-of-contents)

## User Experience

### User Requirements and Expectations

- Intuitive and user-friendly website interface.
- Clear and detailed product descriptions.
- High-quality product images.
- Easy search and filtering options.
- Secure and seamless checkout process.
- Convenient account registration and login.
- Ability for customers to leave product reviews and ratings.
- Option to create and manage a personal wishlist of desired items.

### User stories

- From User/customer perspective
1. As an unauthenticated user/customer, I would like website navigation to be fast and easy
2. As an unauthenticated user/customer, I would like the ability to browse through all the products available on the site.
3. As an unauthenticated user/customer, I would like to search the website to see what kind of product are offered to purchase
4. As an unauthenticated user/customer, I would like to see a details of a products on a website such as(description, price)
5. As an unauthenticated user/customer, I would like functionality to refine my search of products on a website by
Price ,rating, and alphabet
6. As an unauthenticated user/customer, I would like functionality to select product and add it to my shopping basket
7. As an unauthenticated user/customer, I would like functionality to select multiple product and add it to my shopping basket
8. As an unauthenticated user/customer, I would like functionality to increase or decrease quantity of products in my shopping basket
9. As an unauthenticated user/customer, I would like functionality to register for an account  to a website
10. As an authenticated user/customer, I would like functionality to save and  edit my account information
11. As an authenticated user/customer, I would like functionality to see relevant info and my order history on my account page
12. As an authenticated user/customer, I would like functionality to delete an account(profile) if I find no use in using the website anymore
13. As an authenticated user/customer I would like functionality to add my details(shipping and billing) to a secure checkout form so that they could be saved along with my order to easier keep track of my past purchases
14. As user/customer, I would like functionality to put in my card details so that I can make a purchase
15. As an unauthenticated user/customer I would like to be able to view and read reviews of products to make informed purchasing decisions.
16. As an authenticated user/customer I would like functionality to leave a product review on a product detail page so that other customers deciding on purchase of the item will have an insight from somebody who already bought the product
17. As a authenticated user/customer I would Like functinality to edit or delete my product review so that information given in review are up to date and can help other users /customers
<!-- new ones -->
18. As an authenticated user/customer, I want to have the option to add products to my wishlist for future reference and easy access.
19. As an authenticated user/customer, I want to be able to remove items from my wishlist, so that I can manage my saved products effectively and remove those that I am no longer interested in
20. As an authenticated user/customer, I want to receive email notifications for order confirmations, shipping updates, and special promotions.
21. As an unauthenticated user/customer, I would like to be able to view and read reviews of products to make informed purchasing decisions.
22. As an authenticated user/customer, I would like to have the option to contact team or the site owner for any inquiries or assistance related to products or orders.
23. As an unauthenticated user/customer, I want to see links to the business's social media profiles on the website to stay connected and follow updates on different platforms.
24. As an unauthenticated user/customer, I want to have the option to contact the business through social media channels (such as Facebook, Instagram, or Twitter) for inquiries or support.
25. As an unauthenticated user/customer, if I encounter a page not found error, I want to be redirected to a relevant page or provided with suggestions to navigate back to valid areas of the site.

- From site owner perspective:
26. As a site owner, I want to provide secure payment options for customers, such as integrating with secure payment gateways (e.g. Stripe)
27. As a site owner, I want to be able to add new products to the webshop, including details like product name, description, price, and images.
28. As a site owner, I want to be able to delete existing products from the webshop that are no longer available or relevant.
29. As a site owner, I want to be able to update product information, such as descriptions, details, prices, and images, to keep the webshop content accurate and up to date.
30. As a site owner, I want to integrate a newsletter signup form  to capture user information and allow customers to subscribe for updates and promotions.
31. As a site owner, I want to ensure that error pages allow users to easily return to valid areas of the site without relying on browser controls.


| id  |  content | Github issue Numb
| ------ | ------ | ------ |
|  [#1](https://github.com/BogdanMaria/bellacuccina/issues/1#issue-2300158963) | As an unauthenticated user/customer, I would like website navigation to be fast and easy|  |
|  [#2](https://github.com/BogdanMaria/bellacuccina/issues/3#issue-2300171942) | As an unauthenticated user/customer, I would like the ability to browse through all the products available on the site.|  |
|  [#3](https://github.com/BogdanMaria/bellacuccina/issues/2#issue-2300163971) | As an unauthenticated user/customer, I would like to search the website to see what kind of product are offered to purchase|  |
|  [#4](https://github.com/BogdanMaria/bellacuccina/issues/4#issue-2300177757) | A s an unauthenticated user/customer, I would like to see a details of a products on a website such as(description, price)|  |
|  [#5](https://github.com/BogdanMaria/bellacuccina/issues/5#issue-2300181182) | As an unauthenticated user/customer, I would like functionality to refine my search of products on a website by
Price ,rating, and alphabet ||

## Design
***
### Colours

### Fonts

## Project Structure 
### Structure of Code

- This e-commerce project is structured using Django framework
and it is organized in app structure with apps clearly defining its purpose
and apps are as follows:
- Home - App contains landing page about webshop with a
call to action redirecting user to an all product pages, simple and intuitive navigation, footer with social media links and newsletter section.

- Products - app containing all product page with list of all products
,search and filter functionality and also add to cart and wishlist option buttons. Products are displayed within cards with 2 links(click on product image or an eye button) to a product detail page.
- Product detail page with adding,updating product quantity to shopping cart, Reviews section where authenticated user can add product reviews.
site owner CRUD functionality is part of this app also with included add and edit templates and delete button with confirmation modal for site owner.

- Shopping cart - App contains a cart template and functionality to view , update quantity remove and add to wishlist products inside shopping cart

- Checkout - the app is constructed to handle a payment form, list of products to be purchased and total amount of users order.

- Customer profile - app containing user account/profile data that can be updated and prefilled to make checkout experience smoother

- Reviews - app responsible for handling product reviews functionality
with review form, and full CRUD functionality

- Wishlist -app containing list of products that authenticated user can save to purchase or have as an products to review for later

### Code structure beside created apps

- settings.py: This file contains configuration settings for your Django project, such as database settings, installed apps, and middleware.
- Procfile: This file defines the commands executed during deployment of your Django app on a hosting platform.
- Templates: The project includes a base-level folder containing fundamental templates that are extended throughout other templates such as base.html, navigation, toast messages files and footer.html. It also includes templates for user authentication. Additionally, each app within the project has its own templates folder with HTML files that support the specific functionality and promote reusability within the app.
- Static: The project includes a "static" directory that contains the base CSS and JavaScript files. This directory serves as a central location for storing and organizing the static assets used throughout the project. In addition to the base-level files, each app within the project may have its own static directory to house CSS and JavaScript files specific to that app's functionality.


##### Back to [top](#table-of-contents)

## Database
***


### Data Models

#### User model

- User model as part of the Django allauth library contains basic information about authenticated user and contains folowing fields:
username, password,email

####  Product
- Product model made to represent webshop product containing all relevant fields giving user/customer information they need to make a desired purchase

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|category       | category      | ForeignKey| 'Category', null=True, blank=True, on_delete=models.SET_NULL|
|item_no    | item_no   | CharField|  max_length=254, default=random_generated_string,unique=True|
|description     | description    | TextField|  |
| price      |  price     | DecimalField| max_digits=6, decimal_places=2 User|
| weight     | weight    | DecimalField|  max_digits=5, decimal_places=2 |
|image_url      | image_url   | URLField|  max_length=1024, null=True, blank=True|
|image      | image   | imageField| null=True, blank=True|


####  Category

- Model made to clearly separate usage and desing of various webshop products
containing bellow stated fields

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|name      | name   | CharField|  max_length=254|
|notes       |notes     | TextField|  null=True, blank=True|
|slug      | slug     | SlugField| max_length=254, blank=True, null=True|
|friendly_name      | friendly_name     | CharField|  max_length=254, null=True, blank=True|


####   CustomerProfile

- Model representing an account of a registered user containing
following fields:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | OneToOneField|  User, on_delete=models.CASCADE|
|default_phone_number      | default_phone_number     | CharField|  max_length=20, null=True, blank=True|
|default_country       |default_country    | CountryField|  blank_label='Country *', null=True, blank=True|
|default_postcode       | default_postcode     | CharField| max_length=20, null=True, blank=True|
|default_town_or_city       | default_town_or_city     | CharField| max_length=20, null=True, blank=True|
|default_stereet_address1       | default_stereet_address1     | CharField| max_length=20, null=True, blank=True|
|default_street_address2       | default_street_address2     | CharField| max_length=20, null=True, blank=True|
|default_county       | default_county     | CharField| max_length=20, null=True, blank=True|



####  Contact

- Model made with purpose of storing contact info between user and business with bellow stated fields:

  INQUIRY_CHOICES = [
        ('', 'Purpose of Inquiry'),
        ('PRODUCT', 'Poduct Inquiry'),
        ('ORDER', 'Order Inquiry'),
        ('SUGGESTIONS', 'Suggestions'),
        ('OTHER', 'Other'),
    ]


| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| inquiry_purpose  |inquiry_purpose      | CharField|  max_length=24, choices=INQUIRY_CHOICES |
|name        |name      | CharField|  max_length=100|
|email       |email      | EmailField|  max_length=100|
|phone      |phone     | CharField|  max_length=20, blank=True, null=True|
| message      | message     | TextField|  max_length=1000|
| date_submmited     | date_submmited    | DateTimeField|  auto_now_add=True|




#### Order

- Model storing information relevant to customer webshop order ,containing
fields:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|order_number       | order_number     | CharField|  max_length=32, null=False, editable=False|
|user_profile        |user_profile       | ForeignKey|  CustomerProfile,on_delete=models.SET_NULL, null=True,blank=True, related_name='orders'|
|full_name        | full_name    | CharField|  max_length=50, null=False, blank=False|
| email     | email    | EmailField| max_length=254, null=False, blank=False|
|phone_number       | phone_number     | CharField|  max_length=20, null=False, blank=False|
| country       | country      | CountryField|  blank_label='Country *', null=False, blank=False|
| postcode      | postcode     | CharField|  max_length=20, null=True, blank=True|
| town_or_city      |  town_or_city    | CharField|  max_length=40, null=False, blank=False|
|street_address1       | street_address1     | CharField|  max_length=80, null=False, blank=False|
|street_address2       | street_address2     | CharField|  max_length=80, null=False, blank=False|
|county        | county      | CharField|  max_length=80, null=True, blank=True|
|date       | date     | DateTimeField|  auto_now_add=True|
|order_total       | order_total     | DecimalField|  max_digits=10, decimal_places=2, null=False, default=0|
|grand_total       | grand_total     | DecimalField|  max_digits=10, decimal_places=2, null=False, default=0|
|original_cart       | original_cart     | TextField|  null=False, blank=False, default=''|
|stripe_pid       | stripe_pid     | CharField|  max_length=254, null=False, blank=False, default=''|


####  OrderLineItem

- model representing single product in a user order

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| order      | order     | ForeignKey|  Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'|
|product       | product    | ForeignKey|  Product, null=False,blank=False, on_delete=models.CASCADE|
|quantity       | quantity     | IntegerField|  null=False, blank=False, default=0|
|lineitem_total      | lineitem_total    | DecimalField|  max_digits=6,decimal_places=2, null=False blank=False, editable=False|


####  Review

- Model representing reviews for each product

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| author     | author    | ForeignKey|  User,on_delete=models.SET_NULL,null=True, blank=True|
|product      | product     |ForeignKey|  Product, on_delete=models.CASCADE|
|content       | content      | CharField|  max_length=1024|
|time_posted        | time_posted     | TimeField|  auto_now_add=True|


### Wireframes

<details><summary>images</summary>

<details><summary>Home page</summary>
  <img src="docs/wireframes/home_page.png" >
</details>
</details>


## Agile Design

### Overview

- For this project Agile principles and design was implemented from a start since this was the 2nd time in my development career that im implementing agile. While process was familiar, plan was set from beginning and it was adjusted along the way. Drawing from my previous experience, I knew that Agile would empower me to embrace change and prioritize tasks efficiently, ensuring that I consistently delivered incremental value to my project.I leveraged techniques such as user stories,kanban boards an milestones to maintain a clear project vision.This time kanban board are constructed by iterations(sprints)This iterative development cycle gave mae a regular chance to review and try to refine my work.Overall, learning and implementing Agile as a solo developer working on my e-commerce project has been a highly rewarding experience.By implementing Agile principles and design, I was confident in delivering a high-quality and user-focused e-commerce solution.

### Epics(Milestones)
- By effectively leveraging GitHub's 'Milestones' feature and thoughtfully connecting user stories to their corresponding tasks.

<details><summary>See epics</summary>
<img src="">
</details>

### User stories

- I started by creating a user story template using GitHub issues. As the project progressed, these initial rough sketches evolved and were refined into complete user stories.

<details><summary> Template for User story </summary>
<img src="docs/agile/user_story_template.png">
</details>
<details><summary> User story ticket</summary>
<img src="docs/agile/user_story_ticket.png">
</details>
<details><summary> User story finished</summary>
<img src="docs/agile/user_story_finished.png">
</details>


Using Agile methodologies for my solo e-commerce project, I made steady progress by breaking tasks into smaller parts. This approach allowed me to prioritize and deliver important features step by step. With continuous feedback and adjustments, I improved the development environment, implemented crucial functionalities, and built a user-friendly e-commerce platform. Agile proved to be a valuable framework, helping me navigate complexities, achieve tangible results, and prioritize user satisfaction.


## Technologies Used

### Languages & Frameworks

- HTML5
- CSS3
- JavaScript
    - ajax
- jQuery
- Python 3.10.2
- Django 3.2


### Libraries & Tools



- [Bootstrap 5.1](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Modal, Navbar)
- [AWS (Amazon Web Services)](https://aws.amazon.com/)
- [Stripe](https://stripe.com/)
- [Balsamiq](https://balsamiq.com/) to create the projects wireframes
- [Am I Responsive](http://ami.responsivedesign.is/) was used for creating the multi-device mock-up at the top of this README.md file
- [Lucidchart.com](https://www.lucidchart.com/) for creating Entity relationship diagrams(ERD) of my project database
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Boostrap icons](https://fontawesome.com/) - Icons from Bootstrap icons  were used throughout the site
- [GitPod](https://gitpod.io/) was used for version control to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/) - for typography in project
- [Design.com](https://www.design.com/)- for making the custom website logo


## Features

### Nav-bars and Logo
- The navbar, an integral component of the e-commerce store website, is implemented consistently throughout the entire project. It serves as a navigational element that allows users to easily access different sections and pages of the website. The navbar remains present and accessible on every page, ensuring a seamless browsing experience for users as they navigate through the various sections and features of the e-commerce store.And giving users accurate info about state of the shopping cart(number of items in and total price of all items in a shopping cart), and number of products saved in a wishlist.
- User Story covered with this feature:

<details><summary>See Nav-bars and Logo</summary>


![Logo and navbar](docs/features/navbar_desk.png)

![Logo and navbar](docs/features/navbar_mob.png)



</details>



### Footer
- The footer feature is included in most of the project templates, except for the user authentication templates. This decision was made because including the footer in those templates could disrupt the flow and divert the user's attention from the specific purpose of the user authentication process.


<details><summary>See Footer</summary>

![Footer](docs/features/footer.png)
![Footer](docs/features/navbar_mob.png)


</details>



- Features included in projects pages

1. Landing Page Carousel:

- A captivating slideshow on the landing page that serves as a call to action, enticing users to explore the product offerings. It provides visually appealing images and compelling slogan, leading users to click and navigate to all products page for more details and to make purchases.

<details><summary>See Landing Page Carousel </summary>

![Landing Page Carousel](docs/features/carousel.png)

![Landing Page Carousel](docs/features/carousel_mob.png)


</details>



2. Search sidebar :

- A user-friendly sidebar feature for quick and efficient product searches within the e-commerce store. Users can enter keywords or product names to find desired items or categories easily. Enhancing navigation and the overall shopping experience, the search sidebar simplifies the process of finding specific products.

<details><summary>See Search sidebar </summary>

![Search sidebar](docs/features/sidebar.png)

![Search sidebar](docs/features/sidebar_mob.png)


</details>