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
# This is an example from the Inventor Mentor,
# chapter 5, example 4.
#
# This example creates the St. Louis Arch using a QuadMesh.
#

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

# Positions of all of the vertices:
vertexPositions = (
    # 1st row
    (-13.0,  0.0, 1.5), (-10.3, 13.7, 1.2), (-7.6, 21.7, 1.0),
    (-5.0, 26.1, 0.8), (-2.3, 28.2, 0.6), (-0.3, 28.8, 0.5),
    (0.3, 28.8, 0.5), (2.3, 28.2, 0.6), (5.0, 26.1, 0.8),
    (7.6, 21.7, 1.0), (10.3, 13.7, 1.2), (13.0,  0.0, 1.5),
    # 2nd row
    (-10.0,  0.0, 1.5), (-7.9, 13.2, 1.2), (-5.8, 20.8, 1.0),
    (-3.8, 25.0, 0.8), (-1.7, 27.1, 0.6), (-0.2, 27.6, 0.5),
    (0.2, 27.6, 0.5), (1.7, 27.1, 0.6), (3.8, 25.0, 0.8),
    (5.8, 20.8, 1.0), (7.9, 13.2, 1.2), (10.0,  0.0, 1.5),
    # 3rd row
    (-10.0,  0.0, -1.5), (-7.9, 13.2, -1.2), (-5.8, 20.8, -1.0),
    (-3.8, 25.0, -0.8), (-1.7, 27.1, -0.6), (-0.2, 27.6, -0.5),
    (0.2, 27.6, -0.5), (1.7, 27.1, -0.6), (3.8, 25.0, -0.8),
    (5.8, 20.8, -1.0), (7.9, 13.2, -1.2), (10.0,  0.0, -1.5),
    # 4th row
    (-13.0,  0.0, -1.5), (-10.3, 13.7, -1.2), (-7.6, 21.7, -1.0),
    (-5.0, 26.1, -0.8), (-2.3, 28.2, -0.6), (-0.3, 28.8, -0.5),
    (0.3, 28.8, -0.5), (2.3, 28.2, -0.6), (5.0, 26.1, -0.8),
    (7.6, 21.7, -1.0), (10.3, 13.7, -1.2), (13.0,  0.0, -1.5),
    # 5th row
    (-13.0,  0.0, 1.5), (-10.3, 13.7, 1.2), (-7.6, 21.7, 1.0),
    (-5.0, 26.1, 0.8), (-2.3, 28.2, 0.6), (-0.3, 28.8, 0.5),
    (0.3, 28.8, 0.5), (2.3, 28.2, 0.6), (5.0, 26.1, 0.8),
    (7.6, 21.7, 1.0), (10.3, 13.7, 1.2), (13.0,  0.0, 1.5)
)

# set this variable to 0 if you want to use the other method
IV_STRICT = 0

# Routine to create a scene graph representing an arch.


def makeArch():
    result = coin.SoSeparator()

    if IV_STRICT:
        # This is the preferred code for Inventor 2.1

        # Using the new coin.SoVertexProperty node is more efficient
        myVertexProperty = coin.SoVertexProperty()

        # Define the material
        myVertexProperty.orderedRGBA = coin.SbColor(.78, .57, .11).getPackedValue(
        )

        # Define coordinates for vertices
        myVertexProperty.vertex.setValues(0, 60, vertexPositions)

        # Define the QuadMesh.
        myQuadMesh = coin.SoQuadMesh()
        myQuadMesh.verticesPerRow(12)

        myQuadMesh.verticesPerColumn(5)

        myQuadMesh.vertexProperty = myVertexProperty
        result.addChild(myQuadMesh)

    else:
        # Define the material
        myMaterial = coin.SoMaterial()
        myMaterial.diffuseColor = (.78, .57, .11)
        result.addChild(myMaterial)

        # Define coordinates for vertices
        myCoords = coin.SoCoordinate3()
        myCoords.point.setValues(0, 60, vertexPositions)
        result.addChild(myCoords)

        # Define the QuadMesh.
        myQuadMesh = coin.SoQuadMesh()
        myQuadMesh.verticesPerRow = 12

        myQuadMesh.verticesPerColumn = 5
        result.addChild(myQuadMesh)
    view = Gui.ActiveDocument.ActiveView
    sg = view.getSceneGraph()
    sg.addChild(result)
