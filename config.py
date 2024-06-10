from dotenv import load_dotenv
import os

load_dotenv()
user_config = {
    "BROWSERSTACK_USERNAME": os.getenv('BROWSERSTACK_USERNAME'),
    "BROWSERSTACK_ACCESS_KEY": os.getenv('BROWSERSTACK_ACCESS_KEY')
}
