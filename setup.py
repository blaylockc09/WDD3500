from setuptools import setup, find_packages

requires = [
    'flask',
    'url_for'
]
setup(
    name='flask_first_app',
    version='0.0',
    description='My first Python web app built with Flask',
    author='Chris',
    author_email='blayl@mail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
