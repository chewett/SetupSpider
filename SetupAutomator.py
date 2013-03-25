import subprocess

class SetupAutomator():

    def install(self, package):
        subprocess.call(["sudo", "yum", "install", package])

    def install_all(self, packages):
        cmd = ["sudo", "yum", "install"] + packages

        subprocess.call(cmd)
