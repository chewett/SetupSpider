import subprocess

class SetupAutomator():

    def install(self, package):
        subprocess.call(["sudo", "yum", "install", package])
