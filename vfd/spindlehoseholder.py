import cadquery as cq

SHAPEOKO = False
WOODMADS = True

w = 45
h = 10
th = 20 # thickness
offset = -3

res = (cq.Workplane("XY")
       .tag("bot")
       .box(w, h, th)
       .edges(">Z or |Z")
       .fillet(2)
       .faces(">Z")
       .rarray(35, 1, 2, 1)
       .circle(4/2)
       .cutThruAll()
       .faces(">Y")
       .workplane()
       .transformed(offset=(0, -0.5+offset, 0))
       .tag("c")
       .circle(19/2)
       .cutThruAll()
       .faces(">Y")
       .workplaneFromTagged("c")
       .transformed(offset=(0, -9.5, 0))
       .rect(19, 19)
       .cutThruAll()
      )


show_object(res)
