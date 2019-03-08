"""Consts"""
DOMAIN = 'complimentr'
DOMAIN_DATA = '{}_data'.format(DOMAIN)
VERSION = '0.0.1'
URL = 'https://complimentr.com/api'
REQUIRED_FILES = ['sensor.py', 'const.py']
ISSUE_URL = 'https://github.com/custom-components/complimentr/issues'
PLATFORMS = ['sensor']

STARTUP = """
----------------------------------------------
{name}
Version: {version}
This is a custom component
If you have any issues with this you need to open an issue here:
{issueurl}
----------------------------------------------
"""
