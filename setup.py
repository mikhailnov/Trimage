#!/usr/bin/env python

import sys
win=(sys.platform == "win32")
if win:
  import py2exe
  sys.path.append("src/optimgaika")

from distutils.core import setup

setup(name = "optimgaika",
    version = "1.2",
    description = "Optimgaika image compressor - A cross-platform tool for optimizing PNG and JPG files",
    author = "Mikhail Novosyolov, Kilian Valkhof, Paul Chaplin",
    author_email = "mikhailnov@dumalogiya.ru",
    url = "http://nixtux.ru",
    license = "MIT license",
    package_dir = {'optimgaika' : 'src/optimgaika'},
    packages = ["optimgaika",
              "optimgaika.filesize",
              "optimgaika.ThreadPool",],
    package_data = {"optimgaika" : ["pixmaps/*.*"] },
    data_files=[('share/icons/hicolor/scalable/apps', ['desktop/optimgaika.svg']),
            ('share/applications', ['desktop/optimgaika.desktop']),
            ('share/man/man1', ['doc/optimgaika.1'])],
    scripts = ["optimgaika"],
    long_description = """Optimgaika is a cross-platform GUI and command-line interface to optimize image files via optipng, advpng and guetzli, depending on the filetype (currently, PNG and JPG files are supported). It was inspired by imageoptim. All image files are losslessy compressed on the highest available compression levels. Optimgaika gives you various input functions to fit your own workflow: A regular file dialog, dragging and dropping and various command line options.""",
    requires = ["PyQt4 (>=4.4)"],

    #for py2exe
    windows=[r'src\optimgaika\optimgaika.py'],
    zipfile=None,
    options={"py2exe":{
        "optimize":2,
        "compressed":1,
        "bundle_files":1,
        "includes":["sip",],
        "excludes":['email'],
        },
    },
  )
