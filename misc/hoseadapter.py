import cadquery as cq

id1 = 35.2 # vacuum hose OD
od1 = id1 + 3
od2 = 25.7 # hose ID
len1 = 30
len2 = 30
id = 23

res = (cq.Workplane("XY")
       .circle(od1/2)
       .extrude(len1)
       .faces(">Z")
       .fillet(3)
       .faces(">Z")
       .circle(od2/2)
       .extrude(len2)
       .faces(">Z")
       .fillet(1)
       .circle(id/2)
       .cutThruAll()
       .faces("<Z")
       .circle(id1/2)
       .cutBlind(len1 - 3)
      )

show_object(res)
