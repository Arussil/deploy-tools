import configparser, os, errno

from fabric.api import env
from fabric import colors

from wordpress import createWordpressDevelopmentEnv

from django import createDjangoDevelopmentEnv

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECTS = os.path.join(os.path.sep, ROOT, 'projects')

def _loadConf(task):
    """
    Decorator to load the Project Configs
    """
    def task_with_conf(project):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.sep, PROJECTS, project, 'project.ini'))
        task(config)
    return task_with_conf

@_loadConf
def startLocalProject(config):
    """
    Create a new local project
    """
    #Create the project folder structure
    #TODO: Cosa succede quando la cartella già esiste? O l'ambiente è creato  a metà?
    path = config['LOCAL']['PATH']
    print(colors.green('Creating project directory in: {}'.format(path)))
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    #Create the local develop enviroment
    if config['APP']['TYPE'] == 'wordpress':
        print(colors.green('Creating a Wordpress app project'))
        print(colors.green('Initializing Development Environment'))
        createWordpressDevelopmentEnv(config)

    if config['APP']['TYPE'] == 'django':
        print(colors.green('Creating a Django app project'))
        print(colors.green('Initializing Development Environment'))
        createDjangoDevelopmentEnv(config)

def listProjects():
    """
    List all available projects
    """
    #TODO: Solo progetti con i file giusti
    # e che siano cartelle
    for project in os.listdir(PROJECTS):
        print(colors.green(project))
