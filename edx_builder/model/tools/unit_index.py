# -------------------------------------------------------------------
# EdxBuilder Unit Index
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
from colifrapy.tools.decorators import singleton


# Main Class
#===========
@singleton
class UnitIndex(object):

    # Properties
    index = {}

    def set(self, key, value):
        self.index[key] = value

    def get(self, key):
        return self.index.get(key)

    def __repr__(self):
        return str(self.index)
