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

setup(console=['edx_builder.py build course'])
