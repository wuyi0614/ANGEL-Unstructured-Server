import toml

config = toml.load("config/secrets-local.toml")

FASTAPI_AUTH = config["FASTAPI"]["AUTH"]
FASTAPI_BEARER_TOKEN = config["FASTAPI"]["BEARER_TOKEN"]
FASTAPI_MIDDLEWARE_SECRECT_KEY = config["FASTAPI"]["MIDDLEWARE_SECRECT_KEY"]

OPENAI_API_KEY = config["OPENAI"]["API_KEY"]
