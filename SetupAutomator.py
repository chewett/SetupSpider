import subprocess

class SetupAutomator():

    def __init__(self, install_type="yum"):
        self.install_type = install_type

    def _get_install_cmd(self):
        if self.install_type == "yum":
            return ["sudo", "yum", "install"]
        elif self.install_type == "apt":
            return ["sudo", "apt-get", "install"]
        else:
            exit("Unknown install type")


    def install(self, package):
        subprocess.call(self._get_install_cmd().append(package))

    def install_all(self, packages):
        subprocess.call(self._get_install_cmd() + packages)

    def update(self):
        subprocess.call(["sudo", "yum", "update"])

    def run(self, command):
        subprocess.call(command, shell=True)
