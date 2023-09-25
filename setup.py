from setuptools import setup
setup(
    name = 'secret_santa',
    version = '0.1.0',
    packages = ['secret_santa'],
    entry_points = {
        'console_scripts': [
            'secret_santa = secret_santa.__main__:main'
        ]
    }
)
