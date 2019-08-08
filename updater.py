import requests
import os

CONFIG_PATH = 'test/'
CONFIG_FILE = 'config.yml'

DEFAULT_CONFIG = '''config:
  host: test
  domain: crepr.io
  password: xxxx
'''


def main():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
        with open(CONFIG_PATH + CONFIG_FILE, "w+") as cf:
            cf.write(DEFAULT_CONFIG)
    elif not os.path.exists(CONFIG_PATH + CONFIG_FILE):
        with open(CONFIG_PATH + CONFIG_FILE, "w+") as cf:
            cf.write(DEFAULT_CONFIG)


if __name__ == "__main__":
    main()
