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
import uuid
import yaml
from zipfile import ZipFile
from colifrapy import Model
from colifrapy.tools.utilities import normalize_path
from tools.unit_index import UnitIndex


# Main Class
#===========
class CourseFolder(Model):

    def __init__(self, path):

        # Initializing unit index
        self.index = UnitIndex()

        # Checking whether the course is zipped
        self.zipped = '.zip' in path
        path = normalize_path(path, not self.zipped)

        self.path = path if not self.zipped else ''
        self.log.write('main:retrieving', path)

        # Reading folder or zipfile
        if self.zipped:
            self.zip_handle = ZipFile(path)
            self.zip_folder = path.split(os.sep)[-1].replace('.zip', '') + '/'

        # Reading layout
        try:
            yf = self.openPath('course_layout.yml')
            self.layout = yaml.load(yf)
        except Exception as e:
            self.log.write('errors:course_not_found')
            self.log.write('errors:aborting')
            sys.exit()

        # Static file path
        self.static = self.path + self.layout.get('static', 'static') + os.sep

        self.log.write('main:course_name', self.layout['name'])

    # Opening a file path (folder/zip agnostic)
    def openPath(self, path):
        if self.zipped:
            return self.zip_handle.read(self.zip_folder + path)
        else:
            with open(self.path + path, 'r') as pf:
                return pf.read()

    # Sequence iterator
    def sections(self):
        sections = []

        for sec in self.layout['sections']:
            for sub in sec['subsections']:
                for unit in sub['units']:
                    p = os.path.join(
                        sec['directory'].rstrip(os.sep),
                        sub['directory'].rstrip(os.sep),
                        unit['path'].rstrip('.md') + '.md'
                    )

                    try:
                        unit['file'] = self.openPath(p)
                    except Exception as e:
                        print e
                        self.log.write('errors:file_not_found', p)
                        sys.exit()

                    # Assigning a precise id to the unit
                    unit['uuid'] = uuid.uuid4().hex

                    # Indexing
                    self.index.set(
                        '%s/%s/%s' % (
                            sec['directory'],
                            sub['directory'],
                            unit['path']
                        ),
                        unit['uuid']
                    )

            # Yielding to next step
            sections.append(sec)

        # Returning the modified version
        return sections
