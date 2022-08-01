from environs import Env

APP_NAME = "PublicService"

PROPAGATE_EXCEPTIONS = True

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY", default="XXXHHHH")
BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False

ERROR_CODES = [400, 401, 403, 404, 405, 500, 502]

# # log
LOG_PATH = './logs/app.log'
LOG_LEVEL = 'DEBUG'
ADMINS = ()
