from build123d import *
from ocp_vscode import *

i_w = 20
i_l = 41.5
o_w = i_w + 4
o_l = i_l + 2
th = 8
tab_w = 10
tab_h = 3
slot_w = 4.5
slot_th = 1.5
rr = 1

with BuildPart() as p:
    with BuildSketch():
        RectangleRounded(o_w, o_l, rr)
    extrude(amount=th)
    with BuildSketch(p.faces().sort_by(Axis.Z).last):
        Rectangle(tab_w, o_l)
    extrude(amount=tab_h)
    with BuildSketch(p.faces().sort_by(Axis.Z).first.offset(-th)):
        Rectangle(slot_w, o_l)
    extrude(amount=-slot_th, mode=Mode.SUBTRACT)
    with BuildSketch(p.faces().sort_by(Axis.Z).first.offset(-th/2)):
        with Locations((tab_w/2 + 0.5, 0)):
            Rectangle(1, o_l)
        with Locations((-tab_w/2 - 0.5, 0)):
            Rectangle(1, o_l)
    extrude(amount=-th/2, mode=Mode.SUBTRACT)
    with BuildSketch():
        RectangleRounded(i_w, i_l, rr)
    extrude(amount=th+tab_h, mode=Mode.SUBTRACT)
    
show(p, reset_camera=False)

export_step(p.part, 'thermoframe.step')
