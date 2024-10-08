from os import environ
import dotenv


dotenv.load_dotenv()

def resolve_token() -> str:
    try:
        token = environ["BOT_TOKEN"]
    except KeyError:
        raise ValueError("The environment variable 'BOT_TOKEN' is not set.")
    return token