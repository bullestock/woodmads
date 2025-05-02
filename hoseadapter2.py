import cadquery as cq

od1 = 25.7 # hose ID
id2 = 19 # metal tube OD
od2 = id2 + 3
len = 30

res = (cq.Workplane("XY")
       .circle(od1/2)
       .extrude(len)
       .faces(">Z")
       .fillet(3)
       .circle(id2/2)
       .cutThruAll()
      )

show_object(res)
