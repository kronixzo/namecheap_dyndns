import requests
import yaml
import os

CONFIG_PATH = 'test/'
CONFIG_FILE = 'config.yml'

DEFAULT_CONFIG = '''config:
  host: subdomain
  domain: domain.tld
  password: yourpassword
'''

HOST = ''
DOMAIN = ''
PASSWD = ''


def parse_config():
    global HOST
    global DOMAIN
    global PASSWD

    with open(CONFIG_PATH + CONFIG_FILE, 'r') as config:
        cfg = yaml.load(config, Loader=yaml.BaseLoader)['config']

    HOST = cfg['host']
    DOMAIN = cfg['domain']
    PASSWD = cfg['password']


def update_remote():
    r = requests.post("https://dynamicdns.park-your-domain.com/update?host={0}&domain={1}&password={2}".format(HOST,
                                                                                                               DOMAIN,
                                                                                                               PASSWD))
    if r.status_code == 200:
        print("Remote server updated successfully")
        exit(0)
    else:
        print("Received non success status code {0}".format(r.status_code))
        print(r.text)
        exit(1)


def main():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
        with open(CONFIG_PATH + CONFIG_FILE, "w+") as cf:
            cf.write(DEFAULT_CONFIG)
    elif not os.path.exists(CONFIG_PATH + CONFIG_FILE):
        with open(CONFIG_PATH + CONFIG_FILE, "w+") as cf:
            cf.write(DEFAULT_CONFIG)

    parse_config()

    if HOST and DOMAIN and PASSWD:
        update_remote()
    else:
        print("Missing configuration please check {0}".format(CONFIG_PATH + CONFIG_FILE))
        exit(1)


if __name__ == "__main__":
    main()
