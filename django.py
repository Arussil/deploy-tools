import os, errno

from fabric.api import local, lcd
from fabric import colors

ROOT = os.path.dirname(os.path.abspath(__file__))

def createDjangoDevelopmentEnv(config):
    path = config['LOCAL']['PATH']
    project_path = path+'/project'
    try:
        os.makedirs(project_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    print(colors.green('Creating project directory and cloning skeleton'))
    with lcd(project_path):
        local('git clone git@github.com:Arussil/django-project-skeleton.git .')
    print(colors.green('Creating virtualenv'))
    with lcd(path):
        local('python3.7 -m venv venv')
