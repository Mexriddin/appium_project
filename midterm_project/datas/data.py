from dataclasses import dataclass


@dataclass
class LoginData:
    username: str = 'bob@example.com'
    password: str = '10203040'
