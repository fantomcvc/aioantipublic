from setuptools import setup, find_packages


setup(
	name="aioantipublic",
	version='0.1',
	url="https://github.com/fantomcvc/aioantipublic",
	license="MIT License",
	author="fantomcvc",
	description="aioantipublic",
	install_requires=[
		'aiohttp',
		'pydantic',
		'typing',
	],
)