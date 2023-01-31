import requests
from appdirs import user_config_dir
from os.path import exists
from sys import exit

from config import config_create_default, check_config, get_confs

CONFDIR = user_config_dir("gitea-mirror", None)
CONFFILE = f"{CONFDIR}/gm.conf"

def main():
    if not exists(CONFDIR) or not exists(CONFFILE):
        config_create_default(CONFDIR, CONFFILE)

    if not check_config(CONFFILE):
        exit(f"Please make needed changes to {CONFFILE}")

    domain, gitea_key, github_key = get_confs(CONFFILE)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCTRL+C")