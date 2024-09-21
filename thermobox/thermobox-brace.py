import cadquery as cq

d = 50
w = 20
th = 3
cc = 20

result = (cq.Workplane("XY")
          .tag("o")
          .box(d, w, th, centered=(True, False, False))
          .edges("|Z")
          .fillet(2)
          .workplaneFromTagged("o")
          .box(d, th, w, centered=(True, False, False))
          .edges("|Y and >Z")
          .fillet(2)
          .workplaneFromTagged("o")
          .transformed(offset=(0, w/2, 0))
          .rarray(25, 1, 2, 1)
          .circle(3.5/2)
          .cutThruAll()
          .workplaneFromTagged("o")
          .transformed(rotate=(90, 0, 0), offset=(0, 0, w/2))
          .rarray(25, 1, 2, 1)
          .circle(3.5/2)
          .cutThruAll()
)

show_object(result)

