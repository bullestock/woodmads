from build123d import *
from ocp_vscode import *
import math

outer_dia = 78
inner_dia = 65
slot_radius = (outer_dia + inner_dia)/4
slot_width = 1.5
slot_degrees = 300
thickness = 10
slot_height = thickness - 2

bottom = (Align.CENTER, Align.CENTER, Align.MIN)

slot = Cylinder(slot_radius + slot_width/2, slot_height)             
slot -= Cylinder(slot_radius - slot_width/2, slot_height)
plane = Plane(slot.faces().sort_by(Axis.Z).first).offset(-1)
slot = plane*slot

p = Cylinder(outer_dia/2, thickness)
p = fillet(p.edges().sort_by(Axis.Z)[-1], radius=1)
p -= Cylinder(inner_dia/2, thickness, mode=Mode.SUBTRACT)
    
p -= slot

stud_l = 14
stud = Pos(0, slot_radius + stud_l/2 - 2, 0) * Box(10, stud_l, thickness)
stud = fillet(stud.edges().filter_by(Axis.Z), radius=1)
stud = fillet(stud.edges().filter_by(Axis.X), radius=0.5)
p += stud

slit = Pos(0, slot_radius, 0) * Box(3, 30, thickness)
p -= slit

hole = Rot(0, 90, 0) * Pos(0, slot_radius + stud_l - thickness*0.6, 0) * Cylinder(radius=3.2/2, height=20)
p -= hole

STEP = 30
for angle in range(STEP//2, 360 + STEP//2, STEP):
    p -= Pos(slot_radius*math.cos(math.radians(angle)),
             slot_radius*math.sin(math.radians(angle)),
             -thickness/2 + 4) * Rot(90, 90 + angle) * Cylinder(radius=1, height=10)

show(p)

export_step(p, 'spindleskirt.step')
