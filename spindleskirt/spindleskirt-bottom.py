from build123d import *
from ocp_vscode import *
import math
from spindleskirt_defs import *

gap = 1
slot_radius = (outer_dia + inner_dia)/4
slot_width = 1.5
thickness = 12
slot_height = 10

# slot
slot = Cylinder(slot_radius + slot_width/2, slot_height)             
slot -= Cylinder(slot_radius - slot_width/2, slot_height)
plane = Plane(slot.faces().sort_by(Axis.Z).first).offset(3)
slot = plane*slot

# ring
p = Cylinder(outer_dia/2, thickness)
p = fillet(p.edges().sort_by(Axis.Z)[0], radius=1)
p -= Cylinder((inner_dia + gap)/2, thickness, mode=Mode.SUBTRACT)
    
p -= slot

# screw holes
STEP = 45
for angle in range(0, 360, STEP):
    p -= Pos(slot_radius*math.cos(math.radians(angle)),
             slot_radius*math.sin(math.radians(angle)),
             -thickness/2 + 4) * Rot(90, 90 + angle) * Cylinder(radius=0.9, height=10)

# magnet holes
for angle in range(0, 360, STEP):
    p -= Pos(slot_radius*math.cos(math.radians(angle + STEP/2)),
             slot_radius*math.sin(math.radians(angle + STEP/2)),
             thickness/2 - magnet_h) * Cylinder(radius=magnet_d/2, height=2*magnet_h)

show(p)

export_step(p, 'spindleskirt-bottom.step')
