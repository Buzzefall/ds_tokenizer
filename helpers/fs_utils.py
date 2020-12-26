import os
from configparser import ConfigParser


def get_app_config():
    app_path = os.getenv('APP_PATH')
    if app_path is not None:
        path = str(app_path) + '/configs/app.ini'
    else:
        path = os.getcwd() + '/configs/app.ini'

    assert os.path.exists(path) and os.path.isfile(path)

    print("Got main config app.ini: ", path)
    config = ConfigParser()
    config.read(path)

    return config
