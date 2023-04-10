import cadquery as cq

wall_th = 1
w1 = 20
w2 = w1 + 4 * wall_th
w3 = w1 + 2 * wall_th
w4 = w1 - 2*wall_th
w5 = w4 - 2*wall_th
hole_th = 3
lip_th = 1.5
l = 30

res = (cq.Workplane("XY")
       .tag("bot")
       .rect(w2, w2)
       .extrude(lip_th)
       .rect(w3, w3)
       .extrude(l + hole_th)
       .workplaneFromTagged("bot")
       .rect(w1, w1)
       .cutBlind(lip_th + l)
       .rect(w4, w4)
       .cutThruAll()
       .workplaneFromTagged("bot")
       .transformed(offset=(w1/2, 0, 0))
       .rect(w5, w5)
       .cutThruAll()
      )

show_object(res)
