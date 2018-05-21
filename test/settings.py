import config.globals
import configparser

print('Using configuration file : ' + config.globals.configfile)

Config = configparser.ConfigParser()
Config.read('../config/' + config.globals.configfile)
sections = Config.sections()
for section in sections:
    print(section)
    options = Config.options(section)
    for option in options:
        optionValue = Config.get(section, option)
        print("\t" + option + ':' + optionValue)
