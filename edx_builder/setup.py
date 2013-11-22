# -------------------------------------------------------------------
# EdxBuilder Py2exe Configuration
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

import py2exe
from distutils.core import setup

config = {
    'name': 'EdxBuilder',
    'version': '0.1.0',
    'description': 'Edx import format preprocessor.',
    'packages': [
        'edx_builder',
        'edx_builder.model',
        'edx_builder.model.tools',
        'edx_builder.model.templates',
        'edx_builder.model.mdx'
    ],
    'package-data': {
        'edx_builder': ['edx_builder/config/*']
    },
    'include_package_data': True,
    'install_requires': [
        'colifrapy',
        'pyyaml',
        'argparse',
        'Markdown',
        'python-scribd'
    ],
    'entry_points': """
    # -*- Entry points: -*-
    [console_scripts]
    edxbuilder=edx_builder.edx_builder:main
    """,
    'console': ['edxbuilder']
}

setup(**config)