from build123d import *
from ocp_vscode import *
import math

outer_dia = 78
inner_dia = 65
slot_radius = (outer_dia + inner_dia)/4
slot_width = 1
slot_degrees = 300
slot_height = 4
thickness = 6

bottom = (Align.CENTER, Align.CENTER, Align.MIN)

ring = Cylinder(slot_radius - slot_width/2, slot_height)
ring -= Cylinder(inner_dia/2, slot_height)

slit = Pos(0, slot_radius, 0) * Box(3, 20, thickness)
ring -= slit

show(ring)

export_step(ring, 'spindleskirt-inner.step')
