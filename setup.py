import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='ADBox',  
    version='0.1.0',
    author="Ping-P0ng",
    author_email="6xefe1d5@protonmail.com",
    description="ADBox is a viewer for active directory objects.",
    long_description=long_description,
    url="https://github.com/Ping-P0ng/ADBox",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"": ["*.png"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
     ],
    install_requires=["ldap3==2.9.1","PySide6==6.2.3"]
 )