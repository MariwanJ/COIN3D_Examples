#!/usr/bin/env python

###
# Copyright (c) 2002-2007 Systems in Motion
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

###
# This is an example from the Inventor Mentor
# chapter 16, example 5.
#
# This example creates a simple scene graph and attaches a
# browser Examiner viewer to view the data. The camera and
# light in the scene are automatically created by the viewer.
#

import sys

#THIS WILL NOT WORK AT ALL 

#
#from pivy.coin import *
#from pivy.sogui import *
#
#def main():
#    # Initialize Inventor and Qt
#    myWindow = SoGui.init(sys.argv[0])
#   
#    # Build the viewer in the applications main window
#    myViewer = SoGuiExaminerViewer(myWindow)
#   
#    # Read the geometry from a file and add to the scene
#    myInput = SoInput()
#    if not myInput.openFile("dogDish.iv"):
#        sys.exit(1)
#    geomObject = SoDB.readAll(myInput)
#    if geomObject == None:
#        sys.exit(1)
#        
#    view = Gui.ActiveDocument.ActiveView
#    sg = view.getSceneGraph()
#    sg.addChild(myScene)
