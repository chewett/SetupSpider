import os
import json
import argparse



parser = argparse.ArgumentParser(description='Used to configure setup files')
parser.add_argument('--create', help='Location to create a repo file in')

args = parser.parse_args()

if args.create:
    create_file = args.create
    if not os.path.isfile(create_file):
        with open(create_file, "w") as package_file:
            json.dump({"package_sets": {}}, package_file)
        print "Created file at", create_file

    else:
        print "Warning: file already exists, not creating"