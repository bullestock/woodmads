from build123d import *
from ocp_vscode import *
import math

outer_dia = 78
inner_dia = 65.8
gap = 1
slot_radius = (outer_dia + inner_dia)/4
slot_width = 1.5
slot_degrees = 300
thickness = 25
slot_height = 10#thickness - 2

# slot
slot = Cylinder(slot_radius + slot_width/2, slot_height)             
slot -= Cylinder(slot_radius - slot_width/2, slot_height)
plane = Plane(slot.faces().sort_by(Axis.Z).first).offset(3)
slot = plane*slot

# ring
p = Cylinder(outer_dia/2, thickness)
p = fillet(p.edges().sort_by(Axis.Z)[-1], radius=1)
p -= Cylinder((inner_dia + gap)/2, thickness, mode=Mode.SUBTRACT)
    
p -= slot

# screw holes
STEP = 45
for angle in range(0, 360, STEP):
    p -= Pos(slot_radius*math.cos(math.radians(angle)),
             slot_radius*math.sin(math.radians(angle)),
             -thickness/2 + 4) * Rot(90, 90 + angle) * Cylinder(radius=0.9, height=10)

# grip
grip_radius = inner_dia/2
for angle in range(0, 360, 2*STEP):
    p += Pos(grip_radius*math.cos(math.radians(angle)),
             grip_radius*math.sin(math.radians(angle)),
             0) * Rot(90, 90 + angle) * Box(5, thickness, gap)

show(p)

export_step(p, 'spindleskirt.step')
