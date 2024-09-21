import cadquery as cq

d = 50
h = 40
y1 = 10
x1 = 35
w = 50
d1 = 3
d2 = 5
cc = 20

bottom = (cq.Workplane("XY")
          .box(d, w, 3)
          .edges("|Z")
          .fillet(2)
          )

result = (cq.Workplane("XY")
          .workplane(3)
          .box(d - 6.5, w - 6.5, 5)
          .edges("|Z")
          .fillet(2.99)
          .faces("<Z or >Z")
          .shell(-3)
)

result = bottom + result

result = (result
          .faces(">Z")
          .tag("o")
          # cable 1
          .transformed(offset=(d/2, cc/2, 0))
          .slot2D(12, d1)
          .cutThruAll()
          # cable 2
          .workplaneFromTagged("o")
          .transformed(offset=(d/2, -cc/2, 0))
          .slot2D(15.5, d2)
          .cutThruAll()
          # screw holes
          .workplaneFromTagged("o")
          .transformed(offset=(0, 15, 0))
          .rarray(25, 1, 2, 1)
          .circle(3.5/2)
          .cutThruAll()
          )

show_object(result)

