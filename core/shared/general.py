APP_NAME = 'PyGoals'
APP_VER = '0.1'


CONFIG_PATH = 'config'
CONFIG_FILE = 'config.json'
DATA_PATH = 'data'
DATA_FILE = 'data.db'


BASE_CONFIG = {
    'lang': 'ru'
}


GOALS = 'Goals'
TASKS = 'Tasks'


ENCODING = 'utf-8'


ICON = r'core\icon.ico'


DEFAULT_WIDTH = 1024
DEFAULT_HEIGHT = 768
MIN_WIDTH = 640
MIN_HEIGHT = 480


LOCALE = None


def config():
    return CONFIG_PATH / CONFIG_FILE


def data():
    return DATA_PATH / DATA_FILE
