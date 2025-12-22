from build123d import *
from ocp_vscode import *

i_w = 30
i_l = 60
o_w = 38
o_l = 68
th = 8
hole_dia = 1.6
hole_cc1 = 50
hole_cc2 = 45
rr = 2

xy = (Align.MIN, Align.MIN)

with BuildPart() as p:
    with BuildSketch():
        RectangleRounded(o_w, o_l, rr, align=xy)
    extrude(amount=th)
    with BuildSketch():
        with Locations(((o_w - i_w)/2, (o_l - i_l)/2)):
            RectangleRounded(i_w, i_l, rr, align=xy)
    extrude(amount=th, mode=Mode.SUBTRACT)
    with BuildSketch():
        x = (o_l - i_l)/2 + 1
        y = (o_w - i_w)/4
        w = 33.5
        with Locations((y, x), (y, x + hole_cc1), (y + w, x), (y + w, x + hole_cc2)):
          #with PolarLocations(radius=hole_cc/2, count=2, start_angle=90):
              Circle(hole_dia/2)
    extrude(amount=th, mode=Mode.SUBTRACT)
    
show(p, reset_camera=False)

export_step(p.part, 'flowframe.step')
