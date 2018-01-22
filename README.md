# DEPLOY TOOLS
A series of fabric script for development and deploy of projects.

## Getting Started

These instruction will get you, hopefully, a copy of the project up and running on your local machine for development and testing purposes. This is not tested for production enviroment at the moment. Do not use it for production, no, seriusly, it's not that good yet.

### Prerequisites
As a preference for python project you should have a virtual enviroment up and running on your machine, a requirements.txt is included in the project for faster install in virtual env trough pip.

You need to have VirtualBox and Vagrant on your system.

### Starting a Local Project
You can start a project by creating the projects folder inside deploy-tolls root:

```
mkdir projects
```

Then you need to create a couple of configuration files, using the example one provided:

```
#Base for all kind of project
cp project.example.ini projects/project_name/project.ini

#Specific for a Wordpress Development Vagrant
cp vvvv-config-example.yml projects/{project_name}/vvv-custom.yml
```

Change the default configuration inside those files with what you need.

You can see what projects exist using this command:

```
fab listProjects
```

Now you can kickstart che local project creation process:

```
fab startLocalProject:project_name
```

And you will have your local project folders and, if you're installing a Wordpress Local App, your vagrant up and ready.

## Built with

* [Varying Vagrant Vagrants](https://github.com/Varying-Vagrant-Vagrants/VVV) - For the Wordpress development machine
* [Fabric3](https://github.com/mathiasertl/fabric/) a fork of [Fabric](https://github.com/fabric/fabric) for python3
* [Vagrant](https://www.vagrantup.com/) for building and managing virtual machine
* [VirtualBox](https://www.virtualbox.org/) for the virtualization
