from setuptools import setup

setup(
    author='James Vaughan',
    author_email='james@jamesbvaughan.com',
    description='Send an SMS message',
    install_requires=['twilio'],
    license='MIT',
    keywords='sms text command line message twilio phone',
    name='sendsms',
    packages=['sendsms'],
    entry_points={
        'console_scripts': ['sendsms=sendsms.command_line:main'],
    },
    url='https://github.com/jamesbvaughan/sendsms',
    download_url='https://github.com/jamesbvaughan/sendsms/tarball/0.2',
    version='0.2.0',
)
