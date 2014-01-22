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
from colifrapy import Commander


# Main Class
#===========
@singleton
class ScribdClient(object):

    # Properties
    user = None
    sizes = {
    	'edx': ('820', '546'),
    	'fun': ('667', '444')
    }

    def config(self, key, secret):

    	# Connection information
        scribd.config(key, secret)

        # Width and height per target
        platform = Commander().opts.platform
        self.desired_size = self.sizes[platform]

    def get(self, id):
        return scribd.api_user.get(id).get_attributes()
