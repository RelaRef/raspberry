import base64
import configparser

import config.globals
from lib.latest import post


def do(value):
    conf = configparser.ConfigParser()
    conf.read('config/' + config.globals.configfile)

    url = conf.get('stdin', config.globals.raspberryStdInPostToUrl)
    key = conf.get('stdin', config.globals.raspberryStdInPostId)
    if str(type(value)).find("byte") >= 0:
        value = base64.b64encode(value)
    else:
        value = base64.b64encode(value.encode())

    result = post(url, key, value)

    return result
