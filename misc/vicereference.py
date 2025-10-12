from build123d import *
from ocp_vscode import *

hole_cc = 45
m = 15 # modulus
h = 10
stud_w = 15
stud_l = 55
stud_offset = 12
hole_dia = 6.2
rr = 2

xy = (Align.MIN, Align.MIN)

with BuildPart() as p:
    with BuildSketch():
        RectangleRounded(m, hole_cc + m, rr, align=xy)
    extrude(amount=h)
    with BuildSketch():
        with Locations((5, hole_cc + m - stud_w - m/2 - stud_offset)):
            RectangleRounded(stud_l, stud_w, 1, align=xy)
    extrude(amount=h)
    with BuildSketch():
        with Locations((m/2, hole_cc/2 + m/2)):
          with PolarLocations(radius=hole_cc/2, count=2, start_angle=90):
              Circle(hole_dia/2)
    extrude(amount=h, mode=Mode.SUBTRACT)
    fillet(p.edges().filter_by(Axis.Y), radius=1)
    
    
show(p)

export_step(p.part, 'vicereference.step')
