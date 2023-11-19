APP_NAME = 'PyGoals'
APP_VER = '0.1'

CONFIG_PATH = 'config'
DATA_PATH = 'data'
DATA_FILE = 'data.db'

CONFIG_FILE = 'config.json'

BASE_CONFIG = {
    'lang': 'ru'
}

GOALS = 'Goals'
TASKS = 'Tasks'

ENCODING = 'utf-8'

DEFAULT_WIDTH = 1024
DEFAULT_HEIGHT = 768

MIN_WIDTH = 640
MIN_HEIGHT = 480

LOCALE = None


def config():
    return CONFIG_PATH / CONFIG_FILE


def data():
    return DATA_PATH / DATA_FILE
