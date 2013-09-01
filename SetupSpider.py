import subprocess

class SetupSpider():

    """ By default it sets it up for yum base systems but can take any string
        If it uses a non yum based string it will work on what it can,
        or fail to work.
    """
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
		
	def group_install(self, name):
		subprocess.call(['sudo', 'yum', 'groupinstall', name])

    def update(self):
        if self.install_type == "yum":
            subprocess.call(["sudo", "yum", "update"])
        elif self.install_type == "apt":
            subprocess.call(["sudo", "apt-get", "update"])
            subprocess.call(["sudo", "apt-get", "dist-upgrade"])
        else:
            exit("Unknown install type")

    def run(self, command):
        subprocess.call(command, shell=True)
