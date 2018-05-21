import base64
import configparser

import config.globals
from lib.latest import post
from lib.latest import stdin_as_byte
import time

Config = configparser.ConfigParser()
Config.read('config/' + config.globals.configfile)


def main():
    url = Config.get('stdin', config.globals.raspberryStdInPostToUrl)
    key = Config.get('stdin', config.globals.raspberryStdInPostId)
    value = base64.b64encode(stdin_as_byte())

    try:
        while result != 200:
            time.sleep(1)
            result = post(url, key, value)
    except:
        print('Exception.')

    print(result)


main()
