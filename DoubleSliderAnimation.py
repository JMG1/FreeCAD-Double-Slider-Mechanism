#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Javier Martínez García    August 2015

from PySide import QtCore
from math import sin, cos, radians

slider_x = FreeCAD.ActiveDocument.getObject("Pad003002")
slider_y = FreeCAD.ActiveDocument.getObject("Pad003001")
arm = FreeCAD.ActiveDocument.getObject("Pad002001")

slider_x_placement = slider_x.Placement
slider_y_placement = slider_y.Placement
arm_placement = arm.Placement

r_slider_x_pl = slider_x.Placement
r_slider_y_pl = slider_y.Placement
r_arm_pl = arm.Placement

def reset():
  slider_x.Placement = r_slider_x_pl
  slider_y.Placement = r_slider_y_pl
  arm.Placement = r_arm_pl


i = 0
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
  FreeCAD.Gui.updateGui()
  i += 1


timer = QtCore.QTimer()
timer.timeout.connect( update )
timer.start( 10 )

