import os
import json
import subprocess

class SetupSpider():

    """ By default it sets it up for yum base systems but can take any string
        If it uses a non yum based string it will work on what it can,
        or fail to work.
    """
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}

    def create(self, install_type):
        if not os.path.isfile(self.config_file):
            self.config = {"package_sets": {}, "install_type": install_type}
            self.save_config()
            print "Created file at", self.config_file

        else:
            print "Warning: file already exists, not creating"

    def save_config(self):
        with open(self.config_file, "w") as package_file:
            json.dump(self.config, package_file, sort_keys = True, indent = 4, separators = (',', ': '))

    def load(self):
        with open(self.config_file) as package_file:
            self.config = json.load(package_file)

    def add_package(self, package, install_group):
        if install_group not in self.config['package_sets']:
            self.config['package_sets'][install_group] = [package]
            print "Adding new install group", install_group
            print "Adding package", package

        elif package not in self.config['package_sets'][install_group]:
            self.config['package_sets'][install_group].append(package)
            print "Adding package", package

        else:
            print "Package already added"

    def list_groups(self, show_packages=False):
        print "Install groups for file", self.config_file
        for install_group in self.config['package_sets']:
            print "-", install_group#
            if show_packages:
                print ", ".join(self.config['package_sets'][install_group])

    def _get_install_cmd(self):
        if self.install_type == "yum":
            return ["sudo", "yum", "install"]
        elif self.install_type == "dnf":
            return ["sudo", "dnf", "install"]
        elif self.install_type == "apt":
            return ["sudo", "apt-get", "install"]
        else:
            raise Exception("Unknown install type")

    def install(self, package):
        subprocess.call(self._get_install_cmd().append(package))

    def install_all(self, packages):
        subprocess.call(self._get_install_cmd() + packages)

    def group_install(self, name):
        if self.install_type != "yum":
            print "ERROR: cannot run group install for non yum based installer"
        else:
            subprocess.call(['sudo', 'yum', 'groupinstall', name])

    def update(self):
        if self.install_type == "yum":
            subprocess.call(["sudo", "yum", "update"])
        elif self.install_type == 'dnf':
            subprocess.call(["sudo", "dnf", "update"])
        elif self.install_type == "apt":
            subprocess.call(["sudo", "apt-get", "update"])
            subprocess.call(["sudo", "apt-get", "dist-upgrade"])
        else:
            exit("Unknown install type")

    def run(self, command):
        subprocess.call(command, shell=True)
