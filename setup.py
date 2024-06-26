from setuptools import setup, Extension, find_packages

with open('README.md') as f:
	extd_desc = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements_noversion = [
	'pandas',
    'sqlalchemy',
    'deg',
    'argparse',
    'appdirs',
    'werkzeug',
    'fastapi',
    'uvicorn'
]
setup(
	# Meta information
	name				= 'diweir',
	version				= '0.1.0',
	author				= 'Supratik Chatterjee',
	author_email			= 'supratikdevm96@gmail.com',
	url				= 'https://github.com/supratikchatterjee16/diweir',
	description			= 'Organize and work on large scale data.',
	keywords			= ["data", "anonymize", "obfuscate", "migrate", "backup", "archive", "purge", "rdbms", "oracle", "postgres"],
	install_requires		= requirements_noversion,
	# build information
	py_modules			= ['diweir'],
	packages			= find_packages(),
	package_dir			= {'diweir' : 'diweir'},
	long_description		= extd_desc,
	long_description_content_type	= 'text/markdown',
	include_package_data		= True,
	package_data			= {
            'diweir' : [
						'data/*',
						'res/**',
						]},
    entry_points		= {'console_scripts' : ['diweir = diweir:run'],},
	zip_safe			= True,
	# https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
	classifiers			= [
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	license 			= license
)