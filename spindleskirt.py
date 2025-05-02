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

slot = Cylinder(slot_radius + slot_width/2, slot_height)             
slot -= Cylinder(slot_radius - slot_width/2, slot_height, mode=Mode.SUBTRACT)
plane = Plane(slot.faces().sort_by(Axis.Z).first).offset(-1)
slot = plane*slot

p = Cylinder(outer_dia/2, thickness)
p = fillet(p.edges().sort_by(Axis.Z)[-1], radius=1)
p -= Cylinder(inner_dia/2, thickness, mode=Mode.SUBTRACT)
    
p -= slot

stud_l = 10
stud = Pos(0, slot_radius + stud_l/2, 0) * Box(10, stud_l, thickness)
stud = fillet(stud.edges().filter_by(Axis.Z), radius=1)
stud = fillet(stud.edges().filter_by(Axis.X), radius=0.5)
p += stud

slit = Pos(0, slot_radius, 0) * Box(3, 20, thickness)
p -= slit

hole = Rot(0, 90, 0) * Pos(0, slot_radius + stud_l - thickness/2, 0) * Cylinder(radius=3.2/2, height=20)
p -= hole

show(p)

export_step(p, 'spindleskirt.step')
