from build123d import *
from ocp_vscode import *
import math

od2 = 25.7 # hose ID

tube_w = 25
tube_h = 10
tube_r = 4
l = 25

with BuildPart() as p:
    # basic form
    with BuildSketch() as s:
        Circle(radius=od2/2)
        RectangleRounded(tube_h, tube_w, tube_r, mode=Mode.SUBTRACT)
    extrude(amount=l)

show(p)

export_step(p.part, 'spindlehoseadapter.step')
