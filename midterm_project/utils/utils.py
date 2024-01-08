import random
from faker import Faker
from midterm_project.datas.data import LoginData


faker = Faker()


def get_locked_out_user_data():
    return LoginData(username='alice@example.com')


def generate_no_exist_user_data():
    return LoginData(username=faker.email(), password=str(random.randint(0, 10000000)))


def generate_invalid_login_data(invalid_field):
    data = LoginData()
    if invalid_field in ['username', 'password']:
        data.__setattr__(invalid_field, '')
    elif invalid_field == 'both':
        data.username = ''
        data.password = ''
    return data
