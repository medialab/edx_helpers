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
import codecs
import tarfile
import shutil


# Main Class
#===========
class Compiler(object):

    # Properties
    arborescence = [
        'about',
        'chapter',
        'course',
        'discussion',
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

        # Creating arborescence
        self.path = output_path+course.identifier + os.sep
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
            'course/%s.xml' % course.identifier: course.compile(),
            'course.xml': course.xml
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
            with codecs.open(self.path + path, 'w', 'utf-8') as wf:
                wf.write(data)

        # Copying static files
        static_directory = course.folder.static

        if course.folder.zipped:
            sfs = [f for f in course.folder.zip_handle.namelist() if static_directory in f.rstrip(static_directory)]
            for sf in sfs:
                with open(self.path + 'static/' + sf.split('static/')[-1], 'w+') as wf:
                    wf.write(course.folder.zip_handle.read(sf))
        else:
            if os.path.isdir(static_directory):
                for sf in [f for f in os.listdir(static_directory) if os.path.isfile(static_directory + f)]:
                    shutil.copyfile(static_directory + sf, self.path + 'static/' + sf)

        # Compressing
        tar_path = '%s%s%s.tar.gz' % (output_path, os.sep, course.identifier)
        tar = tarfile.open(tar_path, 'w:gz')

        tar.add(self.path, arcname=course.identifier)
        tar.close()

        # Cleaning
        shutil.rmtree(self.path)
