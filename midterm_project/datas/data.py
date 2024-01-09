from dataclasses import dataclass


@dataclass
class LoginData:
    username: str = None
    password: str = None


@dataclass
class ShippingAddressData:
    full_name: str = None
    address_line1: str = None
    city: str = None
    zip_code: str = None
    country: str = None


@dataclass
class CardData:
    full_name: str = None
    card_number: str = None
    expiration_date: str = None
    cvv: str = None
