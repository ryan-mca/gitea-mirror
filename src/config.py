import configparser
from os.path import exists
from os import mkdir

config = configparser.ConfigParser()

def config_create_default(confdir, conffile):
    """Creates a default config file

    Args:
        confdir (String): Path to the config dir
        conffile (String): Path to the config file
    """
    # Checks if the config dir exists
    if not exists(confdir):
        mkdir(confdir)

    # Checks if the config file exists,
    # if it doesn't it creates a default one and exits
    if not exists(conffile):
        config["key"] = {"gitea_key": "None",
                        "github_key": "None"}
        config["web"] = {"root_url": "None"}

        with open(conffile, 'w') as file:
            config.write(file)

def check_config(conffile):
    """Checks if all needed configs are set

    Args:
        conffile (String): Path to the config file

    Returns:
        Boolean
    """

    config.read(conffile)
    for sect in config.sections():
        for conf in config[sect]:
            if config[sect][conf] == "None":
                return False
    return True

def get_confs(conffile):
    """Returns configs

    Args:
        conffile (String): Path to the config file

    Returns:
        String: Returns the domain, gitea_key and the github_key
    """
    config.read(conffile)
    domain = config["web"]["root_url"]
    github_key = config["key"]["github_key"]
    gitea_key = config["key"]["gitea_key"]

    return domain, gitea_key, github_key