import cadquery as cq

res = (cq.Workplane("XY")
       .circle(10/2)
       .extrude(5)
       .circle(4.5/2)
       .cutThruAll()
       )
