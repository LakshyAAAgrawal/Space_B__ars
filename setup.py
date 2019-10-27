import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name = "Space_B__ars",
	version = "0.6",
	maintainer = 'Lakshya A Agrawal',
	maintainer_email = 'lakshya.aagrawal@gmail.com',
	description = "An expansive game made on PyGame. All the rogue keys have escaped your keyboard, except the loyal Space_B__ar. Use the Space Bar to capture all of the other keys. And then use those keys to come up with commands, which help you catch the rest.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/LakshyAAAgrawal/Space_B__ars",
	install_requires = ['pygame'],
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
	python_requires = '>=3.6'
	)
