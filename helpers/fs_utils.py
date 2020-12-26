import os
from configparser import ConfigParser


def get_app_config():
    path = 'configs/app.ini'
    print("Got main config app.ini: ", path)

    config = ConfigParser()
    config.read(path)

    return config
