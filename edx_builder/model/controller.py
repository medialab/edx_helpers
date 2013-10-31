# -------------------------------------------------------------------
# EdxBuilder Main Controller
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
import yaml
from colifrapy import Model

# Main Class
#===========
class Controller(Model):
    
    # Properties
    folder = None
    layout = None

    # Announcement
    def __init__(self):
        self.log.header('main:title')

    # Building Package
    def build(self):

        self.folder = self.opts.target.rstrip('/')+'/'

        # Retrieving course configuration
        self.log.write('main:retrieving_layout')
        with open(self.folder+'course_layout.yml', 'r') as yf:
            self.layout = yaml.load(yf.read())

        print self.layout

    # Testing
    def test(self):
        self.log.write('main:test')
