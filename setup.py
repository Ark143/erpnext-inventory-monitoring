from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in inventory_monitoring/__init__.py
from inventory_monitoring import __version__ as version

setup(
	name="inventory_monitoring",
	version=version,
	description="Advanced Inventory Monitoring for ERPNext v15",
	author="Ark143",
	author_email="your.email@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)