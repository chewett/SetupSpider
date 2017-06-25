import argparse
from SetupSpider import SetupSpider

parser = argparse.ArgumentParser(description='Used to add packages to each install set')
parser.add_argument('setup_file', help='Location of the setup file')
parser.add_argument('package', help='Package to add to the install group')
parser.add_argument('--group', help="Install group to add package to", default="default")

args = parser.parse_args()


setup_file = args.setup_file
package = args.package
install_group = args.group

spider = SetupSpider(setup_file)
spider.load()
spider.add_package(package, install_group)
spider.save_config()