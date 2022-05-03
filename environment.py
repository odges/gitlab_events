from environs import Env

env = Env()
env.read_env()

TELEGRAM_BOT = env.str("TELEGRAM_BOT")
CHAT_ID = env.str("CHAT_ID")

DEBUG = env.bool("DEBUG")
PROJECT_NAME = env.str("PROJECT_NAME")
VERSION = env.str("VERSION")
