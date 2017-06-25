import argparse
from SetupSpider import SetupSpider

parser = argparse.ArgumentParser(description='Used to set up config files')
parser.add_argument('create', help='Location to create a repo file in')
parser.add_argument('install_type', help="Install type for the machine,  e.g. yum or apt", default="yum")

args = parser.parse_args()

create_file = args.create
spider = SetupSpider(create_file)
spider.create(args.install_type)