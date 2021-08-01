import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
	# intentionally *not* adding an encoding option to open
	return codecs.open(os.path.join(here, *parts), 'r').read()


setup(
	name='python-packer',
	version='1.0.4',
	url='https://github.com/abhi1693/python-packer',
	author='abhi1693',
	author_email='desk.abhimanyu@gmail.com',
	license='LICENSE',
	platforms='All',
	description='A Python interface for Hashicorp\'s Packer',
	long_description=read('README.md'),
	py_modules=['packer'],
	install_requires=["sh"],
	classifiers=[
		'Programming Language :: Python',
		'Natural Language :: English',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: POSIX :: Linux',
		'Operating System :: Microsoft',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)
