from pathlib import Path
import json
import sys

import core.shared.general
import core.locales.en_US
import core.locales.ru_RU
from core.shared.general import APP_NAME
from core.shared.general import BASE_CONFIG
from core.shared.general import CONFIG_PATH
from core.shared.general import CONFIG_FILE
from core.shared.general import DATA_PATH
from core.shared.general import ENCODING


dirs = {
    'win32': 'AppData/Local',
    'linux': '.config',
    'darwin': 'Library/Application Support'
}


def get_dirs():
    appdata_path = Path.home() / dirs[sys.platform] / APP_NAME

    core.shared.general.CONFIG_PATH = appdata_path / CONFIG_PATH
    core.shared.general.DATA_PATH = appdata_path / DATA_PATH

    return appdata_path, core.shared.general.CONFIG_PATH, core.shared.general.DATA_PATH


def prepare_dirs():
    appdata, config, data = get_dirs()
    config_file = config / CONFIG_FILE

    if not appdata.exists():
        appdata.mkdir()
    if not config.exists():
        config.mkdir()
    if not data.exists():
        data.mkdir()
    if not config_file.exists():
        with open(config_file, 'w', encoding=ENCODING) as conf:
            json.dump(BASE_CONFIG, conf)

    return config, config_file, data


locales = {
    'ru': core.locales.ru_RU.strings,
    'en': core.locales.en_US.strings
}


def prepare_locales():
    _, config_file, _ = prepare_dirs()

    with open(config_file, 'r', encoding=ENCODING) as conf:
        core.shared.general.LOCALE = locales[json.load(conf)['lang']]

