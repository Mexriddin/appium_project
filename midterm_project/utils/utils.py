import random
from faker import Faker
from midterm_project.datas.data import LoginData, ShippingAddressData, CardData

faker = Faker()


def get_valid_login_data():
    return LoginData(username='bob@example.com', password='10203040')


def get_locked_out_user_data():
    return LoginData(username='alice@example.com', password='10203040')


def generate_no_exist_user_data():
    return LoginData(username=faker.email(), password=str(random.randint(10000000, 99999999)))


def generate_invalid_login_data(invalid_field):
    data = LoginData()
    if invalid_field == 'username':
        data.__setattr__(invalid_field, '')
        data.__setattr__('password', random.randint(10000000, 99999999))
    elif invalid_field == 'password':
        data.__setattr__(invalid_field, '')
        data.__setattr__('username', faker.email())
    elif invalid_field == 'both':
        data.username = ''
        data.password = ''
    return data


def generate_shipping_address():
    shipping_address = ShippingAddressData(
        full_name=faker.first_name() + ' ' + faker.last_name(),
        address_line1=faker.street_address(),
        city=faker.city(),
        zip_code=str(random.randint(10000, 99999)),
        country=faker.country()
    )
    return shipping_address


def generate_card_data():
    card_data = CardData(
        full_name=faker.first_name() + ' ' + faker.last_name(),
        card_number="5555555555554444",
        expiration_date="0325",
        cvv='123'
    )
    return card_data
