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
# chapter 5, example 2.
#
# This example creates an IndexedFaceSet. It creates
# the first stellation of the dodecahedron.
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

#
# Positions of all of the vertices:
#

# set this variable to 0 if you want to use the other method
IV_STRICT = 1

# Routine to create a scene graph representing a dodecahedron
So_END_FACE_INDEX=-1

def makeStellatedDodecahedron():


    vertexPositions = (
    (0.0000,  1.2142,  0.7453),  # top

    (0.0000,  1.2142, -0.7453),  # points surrounding top
    (-1.2142,  0.7453,  0.0000),
    (-0.7453,  0.0000,  1.2142),
    (0.7453,  0.0000,  1.2142),
    (1.2142,  0.7453,  0.0000),

    (0.0000, -1.2142,  0.7453),  # points surrounding bottom
    (-1.2142, -0.7453,  0.0000),
    (-0.7453,  0.0000, -1.2142),
    (0.7453,  0.0000, -1.2142),
    (1.2142, -0.7453,  0.0000),

    (0.0000, -1.2142, -0.7453),  # bottom
    )

#
# Connectivity, information 12 faces with 5 vertices each ),
# (plus the end-of-face indicator for each face):
#

    Indicies = (
    1,  2,  3,  4, 5, So_END_FACE_INDEX,  # top face

    0,  1,  8,  7, 3, So_END_FACE_INDEX,  # 5 faces about top
    0,  2,  7,  6, 4, So_END_FACE_INDEX,
    0,  3,  6, 10, 5, So_END_FACE_INDEX,
    0,  4, 10,  9, 1, So_END_FACE_INDEX,
    0,  5,  9,  8, 2, So_END_FACE_INDEX,

    9,  5, 4, 6, 11, So_END_FACE_INDEX,  # 5 faces about bottom
    10,  4, 3, 7, 11, So_END_FACE_INDEX,
    6,  3, 2, 8, 11, So_END_FACE_INDEX,
    7,  2, 1, 9, 11, So_END_FACE_INDEX,
    8,  1, 5, 10, 11, So_END_FACE_INDEX,

    6,  7, 8, 9, 10, So_END_FACE_INDEX,  # bottom face
    )

    # Colors for the 12 faces
    colors = (
    (1.0, .0, 0), (.0,  .0, 1.0), (0, .7,  .7), (.0, 1.0,  0),
    (.7, .7, 0), (.7,  .0,  .7), (0, .0, 1.0), (.7,  .0, .7),
    (.7, .7, 0), (.0, 1.0,  .0), (0, .7,  .7), (1.0,  .0,  0)
    )

    result = coin.SoSeparator()

    if IV_STRICT:
        # This is the preferred code for Inventor 2.1

        # Using the new coin.SoVertexProperty node is more efficient
        myVertexProperty = coin.SoVertexProperty()

        # Define colors for the faces
        for i in range(12):
            myVertexProperty.orderedRGBA.set1Value(
                i, coin.SbColor(colors[i]).getPackedValue())
            myVertexProperty.materialBinding = coin.SoMaterialBinding.PER_FACE

        # Define coordinates for vertices
        myVertexProperty.vertex.setValues(0, 12, vertexPositions)

        # Define the IndexedFaceSet, with Indicies into
        # the vertices:
        myFaceSet = coin.SoIndexedFaceSet()
        myFaceSet.coordIndex.setValues(0, 72, Indicies)

        myFaceSet.vertexProperty = myVertexProperty
        result.addChild(myFaceSet)

    else:
        # Define colors for the faces
        myMaterials = coin.SoMaterial()
        myMaterials.diffuseColor.setValues(0, 12, colors)
        result.addChild(myMaterials)
        myMaterialBinding = coin.SoMaterialBinding()
        myMaterialBinding.value = coin.SoMaterialBinding.PER_FACE
        result.addChild(myMaterialBinding)

        # Define coordinates for vertices
        myCoords = coin.SoCoordinate3()
        myCoords.point.setValues(0, 12, vertexPositions)
        result.addChild(myCoords)

        # Define the IndexedFaceSet, with Indicies into
        # the vertices:
        myFaceSet = coin.SoIndexedFaceSet()
        myFaceSet.coordIndex.setValues(0, 72, Indicies)
        result.addChild(myFaceSet)
    view = Gui.ActiveDocument.ActiveView
    sg = view.getSceneGraph()
    sg.addChild(result)
