import os
import json
import argparse

parser = argparse.ArgumentParser(description='Used to add packages to each install set')
parser.add_argument('setup_file', help='Location of the setup file')
parser.add_argument('package', help='Package to add to the install group')
parser.add_argument('install_group', help="Install group to add package to", default="default")

args = parser.parse_args()


setup_file = args.setup_file
package = args.package
install_group = args.install_group

with open(setup_file) as package_file:
    install_data = json.load(package_file)

if install_group not in install_data['package_sets']:
    install_data['package_sets'][install_group] = [package]
    print "Adding new install group", install_group
    print "Adding package", package
elif package not in install_data['package_sets'][install_group]:
    install_data['package_sets'][install_group].append(package)
    print "Adding package", package
else:
    print "Package already added"

with open(setup_file, "w") as package_file:
    json.dump(install_data, package_file)