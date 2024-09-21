import cadquery as cq

d = 50
h = 30
y1 = 10
x1 = 35
w = 50

result = (cq.Workplane("XY")
          .box(d, w, h)
          .faces("<Z")
          .shell(-3)
          .edges("|Z or >Z")
          .fillet(2)
          .faces(">Z")
          .workplane()
          .rect(32.5, 21.5)
          .cutBlind(-5)
)

show_object(result)

