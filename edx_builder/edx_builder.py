#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
# EdxBuilder Command Line Hub
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
from colifrapy import Colifrapy
from model.controller import Controller


# Hub
#====
class EdxBuilder(Colifrapy):
    pass

# Launching
#===========
if __name__ == '__main__':

    hub = EdxBuilder(Controller)
    print ''
