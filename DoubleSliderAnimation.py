#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Javier Martínez García    August 2015

from PySide import QtCore
from math import sin, cos, radians

# retrieve the objects from the document
slider_x = FreeCAD.ActiveDocument.getObject("Pad003002")
slider_y = FreeCAD.ActiveDocument.getObject("Pad003001")
arm = FreeCAD.ActiveDocument.getObject("Pad002001")


# store initial placement (needed to restore initial position)
slider_x_placement = slider_x.Placement
slider_y_placement = slider_y.Placement
arm_placement = arm.Placement

# store object placements in a new variable
r_slider_x_pl = slider_x.Placement
r_slider_y_pl = slider_y.Placement
r_arm_pl = arm.Placement


def reset():
  # function to restore initial position of the objects
  slider_x.Placement = r_slider_x_pl
  slider_y.Placement = r_slider_y_pl
  arm.Placement = r_arm_pl


# "i" is the variable that represents the animation steps.
# At this mechanism, "i" represents the angle of the rod in degrees
i = 0

# update function calculates object position as f(i) and increases i
def update():
  global i
  alpha = radians( i )
  x = 150.0*cos( alpha )
  y = 150.0*sin( alpha )
  slider_x.Placement = FreeCAD.Placement( slider_x_placement.Base + FreeCAD.Vector( 150-x, 0, 0 ),
                                          slider_x_placement.Rotation )
  
  slider_y.Placement = FreeCAD.Placement( slider_y_placement.Base + FreeCAD.Vector( 0, y, 0 ),
                                          slider_y_placement.Rotation )
  
  arm.Placement = FreeCAD.Placement( arm_placement.Base + FreeCAD.Vector( 0, y, 0 ),
                                     FreeCAD.Rotation( FreeCAD.Vector( 0,0,1), i))
  # update the scene
  FreeCAD.Gui.updateGui()
  # increase mechanism input position
  i += 1


# create a timer object
timer = QtCore.QTimer()
# connect timer event to function "update"
timer.timeout.connect( update )
# start the timer by triggering "update" every 10 ms
timer.start( 10 )

