import cadquery as cq

d = 50
h = 40
y1 = 10
x1 = 35
w = 50

result = (cq.Workplane("XZ")
          .vLine(h)
          .hLine(x1)
          .lineTo(d, y1)
          .vLine(-y1)
          .close()
          .extrude(w)
          .faces("<Z")
          .shell(-3)
          .edges("|Z or >Z")
          .fillet(2)
          .faces(f">({h - y1}, 0, {d - x1})")
          .workplane()
          .transformed(offset=(-w/2, 3, 0))
          .rect(32.5, 21.5)
          .cutBlind(-5)
)

show_object(result)

