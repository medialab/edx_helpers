# -------------------------------------------------------------------
# EdxBuilder Course Compiler
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
import os
import tarfile
import StringIO


# Main Class
#===========
class Compiler(object):

    # Properties
    arborescence = [
        'about',
        'chapter',
        'course',
        'html',
        'info',
        'policies',
        'sequential',
        'static',
        'vertical',
        'video'
    ]
    files = {}
    
    def __init__(self, course, output_path):

        # Creating arborescences
        self.path = output_path+course.identifier+'/'
        try:
            os.mkdir(self.path)
            for d in self.arborescence:
                os.mkdir(self.path+d)
        except:
            pass

        # Course files
        self.files = {
            'about/effort.html': course.effort,
            'about/overview.html': course.overview,
            'course/%s.xml' % course.identifier: course.compile()
        }

        # Big file loop
        for section in course.sections:
            self.files['chapter/%s.xml' % section.id] = section.compile()

            for sub in section.subsections:
                self.files['sequential/%s.xml' % sub.id] = sub.compile()

                for unit in sub.units:
                    self.files['vertical/%s.xml' % unit.id] = unit.compile()

                    for c in unit.components:
                        self.files['%s/%s.xml' % (c.directory, c.id)] = c.compile()
                        if hasattr(c, 'html'):
                            self.files['%s/%s.html' % (c.directory, c.id)] = c.html

        # Writing file
        for path, data in self.files.items():
            with open(self.path+path, 'w') as wf:
                wf.write(data)


        # self.tar = tarfile.open(output_path+'Course.tar.gz', 'w:gz')

        # # Closing file
        # self.tar.close()
