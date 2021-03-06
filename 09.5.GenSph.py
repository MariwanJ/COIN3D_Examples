#!/usr/bin/env python

###
# Copyright (c) 2002-2007 Systems in Motion
#
# Permission to use, copy, modify, and distribute this coin.Software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE coin.SoFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS coin.SoFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATcoin.SoEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS coin.SoFTWARE.
#

###
# This is an example from The Inventor Mentor,
# chapter 9, example 5.
#
# Using a callback for generated primitives.
# A simple scene with a sphere is created.
# A callback is used to write out the triangles that
# form the sphere in the scene.
#

from __future__ import print_function

####################################################################
#        Modified to be compatible with  FreeCAD                   #
#                                                                  #
# Author : Mariwan Jalal  mariwan.jalal@gmail.com                  #
####################################################################

import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

##############################################################
# CODE FOR The Inventor Mentor STARTS HERE

def printVertex(vertex):
    point = vertex.getPoint()
    print("\tCoords     = (%g, %g, %g)" % (point[0], point[1], point[2]))

    normal = vertex.getNormal()
    print("\tNormal     = (%g, %g, %g)" % (normal[0], normal[1], normal[2]))

def printHeaderCallback(void, callbackAction, node):
    print("\n Sphere ")
    # Print the node name (if it exists) and address
    if not not node.getName():
        print('named "%s" ' % node.getName().getString())
    print("at address %r\n" % node.this)

    return coin.SoCallbackAction.CONTINUE

def printTriangleCallback(void, callbackAction, vertex1, vertex2, vertex3):
    print("Triangle:")
    printVertex(vertex1)
    printVertex(vertex2)
    printVertex(vertex3)

def printSpheres(root):
    myAction = coin.SoCallbackAction()
    
    myAction.addPreCallback(coin.SoSphere.getClassTypeId(), printHeaderCallback, None)
    myAction.addTriangleCallback(coin.SoSphere.getClassTypeId(), printTriangleCallback, None)

    myAction.apply(root)
    
# CODE FOR The Inventor Mentor ENDS HERE
##############################################################

def ExecuteGenSph():
    # Initialize Inventor
    # coin.SoDB.init() invoked automatically upon coin module import

    # Make a scene containing a red sphere
    root = coin.SoSeparator()
    myCamera = coin.SoPerspectiveCamera()
    myMaterial = coin.SoMaterial()
    root.addChild(myCamera)
    root.addChild(coin.SoDirectionalLight())
    myMaterial.diffuseColor = (1.0, 0.0, 0.0)   # Red
    root.addChild(myMaterial)
    root.addChild(coin.SoSphere())
    # Write out the triangles that form the sphere in the scene
    printSpheres(root)