from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='stock_price',
      version=version,
      description="Get stock prices.",
      long_description="""""",
      classifiers=[],
      keywords='',
      author='Jesse Aldridge',
      author_email='JesseAldridge@gmail.com',
      url='https://github.com/JesseAldridge/stock_price',
      license='MIT',
      packages=['stock_price'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'requests'
      ]
      )
