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
import os
import yaml
from colifrapy import Model
from colifrapy.tools.utilities import normalize_path
from course_folder import CourseFolder
from templates.course import CourseXMLTemplate
from tools.compiler import Compiler
from tools.scribd_client import ScribdClient


# Main Class
#===========
class Controller(Model):

    # Announcement
    def __init__(self):
        self.log.header('main:title')

    # Building Package
    def build(self):

        # Parsing folder
        folder = CourseFolder(self.opts.target)

        # Initializing scribd client
        scribd_client = ScribdClient()
        scribd_client.config(
            self.settings.scribd['key'],
            self.settings.scribd['secret']
        )

        # Creating output folder
        output_path = normalize_path(self.opts.output, True)
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        # Creating XML
        course = CourseXMLTemplate(folder)

        # Compiling the course
        self.log.write('main:compiling', output_path)
        Compiler(course, output_path, not self.opts.unzipped)

        self.log.write('main:done')


    # Testing
    def test(self):
        print 'test'
