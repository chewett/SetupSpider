import argparse
from SetupSpider import SetupSpider

parser = argparse.ArgumentParser(description='Install and inspect the packages')
parser.add_argument('package_file', help='Package file to use')
parser.add_argument('--list_groups', action='store_true', help='List all groups in the package file')
parser.add_argument('--list_all_packages', action='store_true', help='List all packages in each group')
parser.add_argument('--install_all', action='store_true', help='Install all packages')
parser.add_argument('--install_group', help='Install allpackages in the group')

args = parser.parse_args()

create_file = args.package_file
spider = SetupSpider(create_file)
spider.load()

if args.list_groups:
    spider.list_groups()

elif args.list_all_packages:
    spider.list_groups(True)

elif args.install_all:
    spider.update()
    spider.install_all()

elif args.install_group:
    spider.update()
    spider.install_group(args.install_group)
