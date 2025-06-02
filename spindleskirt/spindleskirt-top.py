from build123d import *
from ocp_vscode import *
import math
from spindleskirt_defs import *

slot_radius = (outer_dia + inner_dia)/4
slot_width = 1.5
slot_degrees = 300
thickness = 30
slot_height = 10#thickness - 2
tube_len = 30
tube_w = 24.9
tube_h = 9.9
tube_r = 4
tube_th = 1.5

with BuildPart() as p:
    # basic form
    with BuildSketch() as s:
        Circle(radius=outer_dia/2)
        Circle(radius=inner_dia/2, mode=Mode.SUBTRACT)
    extrude(amount=thickness)
    edges = p.edges().sort_by(Axis.Z)
    se = [ edges.first, edges[4] ]
    fillet(se, radius=1)
    # tube
    plane = Plane(origin=p.part.center() + (0, 0, -1), z_dir=(1, 0, 0)).offset(outer_dia/2 + tube_len)
    with BuildSketch(plane):
        RectangleRounded(tube_h, tube_w, tube_r)
    extrude(until=Until.PREVIOUS)
    with BuildSketch(plane):
        RectangleRounded(tube_h - 2*tube_th, tube_w - 2*tube_th, tube_r-tube_th)
    extrude(amount=-(tube_len + 10), mode=Mode.SUBTRACT)
    # grip
    with Locations(p.faces().sort_by(Axis.Z).last.offset(-thickness/2)):
        with PolarLocations(radius=inner_dia/2, count=4, start_angle=45):
            Box(thickness, 5, gap - 0.1, rotation=(0, 90, 0))
    # stop
    stop_h = 18
    with Locations(p.faces().sort_by(Axis.Z).last.offset(-thickness + stop_h/2)):
        with PolarLocations(radius=inner_dia/2, count=4):
            Box(stop_h, 5, 8, rotation=(0, 90, 0))
    # magnet holes
    with Locations(p.faces().sort_by(Axis.Z).first):
        with PolarLocations(radius=slot_radius, count=360//STEP, start_angle=STEP/2):
            Cylinder(radius=magnet_d/2, height=2*magnet_h, mode=Mode.SUBTRACT)
    #extrude(amount=10)
    
show(p)

export_step(p.part, 'spindleskirt-top.step')
