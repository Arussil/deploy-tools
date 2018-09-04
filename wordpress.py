import configparser, os

from fabric.api import local, lcd

ROOT = os.path.dirname(os.path.abspath(__file__))

def createVagrant(config):
    #Download VVV on the path
    path = config['LOCAL']['PATH']
    with lcd(path):
        local('git clone -b master git://github.com/Varying-Vagrant-Vagrants/VVV.git ./vagrant')
  
    #Copy the VVV config file to the right path
    vvv_config_file = os.path.join(
        os.path.sep, ROOT,
        'projects',
        config['PROJECT']['NAME'],
        'vvv-custom.yml'
    )
    with lcd(os.path.join(os.path.sep, path, 'vagrant')):
        local('cp {} ./'.format(vvv_config_file))
        #Instal vagrant plugins
        local('vagrant plugin install vagrant-hostsupdater vagrant-triggers vagrant-vbguest')
        #Install the machine
        local('vagrant up')

def createWordpressDevelopmentEnv(config):
    createVagrant(config)
