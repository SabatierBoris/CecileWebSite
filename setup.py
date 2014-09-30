"""
Setup file to install this app
"""
import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.md')).read()
CHANGES = open(os.path.join(HERE, 'CHANGES.txt')).read()

REQUIRES = [
    # Base
    'pyramid',
    # Debug
    'pyramid_debugtoolbar',
    # BDD
    'sqlalchemy',
    # Template
    'pyramid_mako',
    # Form
    'WTForms',
    # 'WTForms-Alchemy',
    # UnitTest
    'WebTest',
]

setup(
    name='pyramidapp',
    version='0.0',
    description='pyramidapp',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    tests_require=REQUIRES,
    test_suite="pyramidapp.tests",
    entry_points="""\
        [paste.app_factory]
        main = pyramidapp:main
        [console_scripts]
        initialize_bd = pyramidapp.scripts.initializebd:main
    """,
)
