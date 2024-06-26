# Content

1. [Suites](#suites)
2. [Run tests](#run-tests)

## Suites
- [Api Calls](#api-calls) 
- [Login](#login)
- [Logout](#logout)
- [My Cart](#my-cart)
- [Product](#product)
- [Products](#products)
- [Ordering an item](#ordering-an-item)

### Api Calls
####  
- **Name**: The test call all devices
- **Description**: A test calling all devices from the API
- **Objective**: Check when the API is called, the devices are loaded on the page and displayed

####  
- **Name**: The test is an unauthorized call
- **Description**: A negative test that calls all devices from the API without authorization
- **Objective**: Check when the API is called with 401, "Unauthorized" error message is displayed

#### 
- **Name**: The test is calling a non-existent resource
- **Description**: A negative test that calls all devices from a non-existent resource
- **Objective**: Check when the API is called with 404, "Not found" error message is displayed


### Login
####  
- **Name**: Successful login test
- **Description**: A positive login test with valid data for a successful login
- **Objective**: Check that after successfully logging in, the page goes to the products section
- **Test data**: 
-     username="bob@example.com"  password="10203040"

####  
- **Name**: The blocked user's login test
- **Description**: A negative login test with the data of a blocked user
- **Objective**: Checks that an error message is generated after logging in to the page
- **Test data**: 
-     username="alice@example.com"  password="10203040"

#### 
- **Name**: The no exist user's login test
- **Description**: A negative login test with the data of a non-existing user
- **Objective**: Checks that an error message is generated after logged
- **Test data**:
-     username=generated by utilities  password=generated by utilities

#### 
- **Name**: The user's login with empty fields test
- **Description**: Negative login test without filling in both fields
- **Objective**: Checks that an error message is generated after logged

#### 
- **Name**: The user's login with empty username field test
- **Description**: c
- **Objective**: Checks that generated error message "Username is required" after logged
- **Test data**:
-     password=generated by utilities

#### 
- **Name**: The user's login with empty password field test
- **Description**: Negative login test without filling in password field
- **Objective**: Checks that generated error message "Password is required" after logged
- **Test data**:
-     username=generated by utilities


### Logout
####  
- **Name**: Logout test
- **Description**: Successful logout test
- **Objective**: Check that after logging out, an alert appears with a successful message


### My Cart
####  
- **Name**: Empty cart test
- **Description**: The cart test without added items
- **Objective**: Check that the  cart page is no items
- 
####  
- **Name**: The test updates the number of items in the cart
- **Description**: Test increasing the quantity of items in the cart
- **Objective**: Check that the number of products and total price is increasing


### Product
####  
- **Name**: The test of adding an item to the cart
- **Description**: Test adding an item to the shopping cart by selecting a property
- **Objective**: Check that the product has been added(changed) to the cart


### Products
####  
- **Name**: The products sorting test
- **Description**: A test for sorting products by name and price
- **Objective**: Check that the products in the page are sorted correctly

####  
- **Name**: The product review test
- **Description**: The test evaluates the product stars
- **Objective**: Check that after review , a modal appears with a successful message



### Ordering an item
####  
- **Name**: The Product Order test
- **Description**: The end-to-end test adds the product to the cart, login, enter the required fields for delivery address, payment method and place an order
- **Objective**: Check the delivery address, payment method, total price and check that after successfully place order, the page goes to the completed section
- **Test data**:
  - Login data 
    -       username="bob@example.com"  password="10203040" 
  - Shipping address data 
    -     full_name=generated by utilities 
    -     address_line1=generated by utilities 
    -     city=generated by utilities
    -     zip_code=generated by utilities 
    -     country=generated by utilities      
  - Card data
    -     full_name=generated by utilities
    -     card_number="5555555555554444"
    -     expiration_date="0325"
    -     cvv="123"


## Run tests
All tests:

```sh
pytest
```

Positive tests:

```sh
pytest -m  positive
```

Negative tests:

```sh
pytest -m  negative
```

Smoke tests:

```sh
pytest -m  smoke
```
