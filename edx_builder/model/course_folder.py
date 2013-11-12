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
            self.layout = yaml.load(yf.read())
        except IOError:
            self.log.write('errors:course_not_found')
            self.log.write('errors:aborting')
            sys.exit()

        self.log.write('main:course_name', self.layout['name'])

    # Sequence iterator
    def sections(self):
        for sec in self.layout['sections']:

            # Applying meta modification to subsections
            sec = self.overloadLayout(sec)

            # Yielding to next step
            yield sec

    # Overloading subsequences
    def overloadLayout(self, sec):
        for sub in sec['subsections']:
            for unit in sub['units']:
                p = (self.path +
                     sec['directory'].rstrip('/')+'/' +
                     sub['directory'].rstrip('/')+'/' +
                     unit['path'].rstrip('.md')+'.md')

                try:
                    unit['file'] = open(p, 'r').read()
                except:
                    self.log.write('errors:file_not_found', p)
                    sys.exit()
        return sec
