import base64
import configparser

import config.globals
from lib.latest import post

Config = configparser.ConfigParser()
Config.read('../config/' + config.globals.configfile)


def main():
    url = Config.get('stdin', config.globals.raspberryStdInPostToUrl)
    key = Config.get('stdin', config.globals.raspberryStdInPostId)
    value = base64.b64encode(b'stdin_as_text()3')

    result = post(url, key, value)
    print(result)


main()
