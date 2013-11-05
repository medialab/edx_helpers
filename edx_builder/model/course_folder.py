# -------------------------------------------------------------------
# EdxBuilder Course Folder
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
import os
import sys
import yaml
from colifrapy import Model
from colifrapy.tools.utilities import normalize_path


# Main Class
#===========
class CourseFolder(Model):
    
    # Properties
    path = None
    layout = None

    def __init__(self, path):
        self.path = normalize_path(path, True)
        self.log.write('main:retrieving', self.path)

        # Reading layout
        try:
            yf = open(self.path+'course_layout.yml', 'r')
            self.layout = yaml.load(yf.read())['course']
        except IOError:
            self.log.write('errors:course_not_found')
            self.log.write('errors:aborting')
            sys.exit()

        self.log.write('main:course_name', self.layout['display_name'])

    # Sequence iterator
    def sequences(self):
        for s in self.layout['sequences']:
            yield s

    # Subsequence iterator
    def subsequences(self, sequence):
        for sub in sequence['subsequences']:
            p = self.path+s['path'].rstrip('/')+'/'
            s['files'] = [f for f in os.listdir(p) if os.path.isfile(f)]
            yield s
