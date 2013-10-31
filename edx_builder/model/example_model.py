# -------------------------------------------------------------------
# EdxBuilder Example Model
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
from colifrapy import Model


# Main Class
#===========
class ExampleModel(Model):
    
    # Example of model action
    def hello(self):
        self.log.write('main:model')
        self.log.write('main:test')
