import os
import json
import argparse

parser = argparse.ArgumentParser(description='Used to set up config files')
parser.add_argument('create', help='Location to create a repo file in')
parser.add_argument('install_type', help="Install type for the machine,  e.g. yum or apt", default="yum")

args = parser.parse_args()

create_file = args.create
if not os.path.isfile(create_file):
    with open(create_file, "w") as package_file:
        json.dump({"package_sets": {}, "install_type": args.install_type}, package_file)
    print "Created file at", create_file

else:
    print "Warning: file already exists, not creating"