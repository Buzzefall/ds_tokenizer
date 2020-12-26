import os
from configparser import ConfigParser


def get_app_config():
    app_path = os.getenv('APP_PATH')
    path = str(app_path) + '/configs/app.ini'
    print("Got main config app.ini: ", path)

    config = ConfigParser()
    config.read(path)

    return config
