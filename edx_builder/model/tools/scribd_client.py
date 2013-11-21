# -------------------------------------------------------------------
# EdxBuilder Scribd Client
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
import scribd
from colifrapy.tools.decorators import singleton


# Main Class
#===========
@singleton
class ScribdClient(object):

    # Properties
    user = None

    def config(self, key, secret):
        scribd.config(key, secret)

    def get(self, id):
        return scribd.api_user.get(id).get_attributes()
