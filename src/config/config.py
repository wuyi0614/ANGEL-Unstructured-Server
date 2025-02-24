import toml

from pathlib import Path

conf_file = Path() / 'src' / 'config' / 'secrets-local.toml'
config = toml.load(str(conf_file))

FASTAPI_AUTH = config["FASTAPI"]["AUTH"]
FASTAPI_BEARER_TOKEN = config["FASTAPI"]["BEARER_TOKEN"]
FASTAPI_MIDDLEWARE_SECRECT_KEY = config["FASTAPI"]["MIDDLEWARE_SECRECT_KEY"]

OPENAI_API_KEY = config["OPENAI"]["API_KEY"]
