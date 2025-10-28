from setuptools import setup, find_packages

setup(
	name="py_ascii_cards",
	version="0.1",
	description="Display playing cards in ASCII format.",
	long_description=open("readme.md", encoding="utf-8").read(),
	long_description_content_type="text/markdown",
	author="Tony Trinh",
	author_email="taylor.tony.tech@gmail.com",
	install_requires=[],
	url="https://github.com/ToekneeT/Ascii-Cards/",
	keywords="cards ascii",
	license="MIT",
	packages=find_packages(include=["ascii_cards", "ascii_cards.*"]),
	classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
	python_requires=">=3.7",
	)