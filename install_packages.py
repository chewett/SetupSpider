import argparse
from SetupSpider import SetupSpider

parser = argparse.ArgumentParser(description='Install and inspect the packages')
parser.add_argument('package_file', help='Package file to use')
parser.add_argument('--list_groups', action='store_true', help='List all groups in the package file')
parser.add_argument('--list_all_packages', action='store_true', help='List all packages in each group')

args = parser.parse_args()

create_file = args.package_file
spider = SetupSpider(create_file)
spider.load()

if args.list_groups:
    spider.list_groups()

elif args.list_all_packages:
    spider.list_groups(True)
