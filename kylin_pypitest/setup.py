import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="debug_life",
	version="0.0.1",
	author="kylin",
	author_email="author@example.com",
	description="PyPI Tutorial",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
