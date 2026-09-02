from build123d import *
from ocp_vscode import *

i_w = 55.5
i_l = 145.5
th = 3
o_w = i_w + 2*th
o_l = i_l + 2*th
rr = 5
h = 50

with BuildPart() as p:
    with BuildSketch():
        RectangleRounded(o_w, o_l, rr)
    extrude(amount=h)
    with BuildSketch(p.faces().sort_by(Axis.Z).last):
        RectangleRounded(i_w, i_l, rr)
    extrude(amount=-(h - th), mode=Mode.SUBTRACT)
    fillet(p.edges().sort_by(Axis.Y)[1], radius=5)
    with BuildSketch(p.faces().sort_by(Axis.Y).last):
        with Locations((0, -2.5)):
            Circle(radius=7.5)
    extrude(amount=-o_l, mode=Mode.SUBTRACT)
    with BuildSketch(p.faces().sort_by(Axis.X).last):
        with GridLocations(15, 10, 6, 1):
            RectangleRounded(5, 20, 2.49)
    extrude(amount=-o_l, mode=Mode.SUBTRACT)
    
show(p, reset_camera=False)

export_step(p.part, 'spcase.step')
