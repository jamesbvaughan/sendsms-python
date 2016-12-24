from setuptools import setup

setup(name='sendsms',
      version='0.1',
      description='Send an SMS message',
      url='https://github.com/jamesbvaughan/sendsms',
      author='James Vaughan',
      author_email='james@jamesbvaughan.com',
      license='MIT',
      packages=['sendsms'],
      install_requires=['twilio'],
      scripts=['bin/sendsms'],
      zip_safe=False)
