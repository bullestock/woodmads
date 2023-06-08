import cadquery as cq

lid_w = 120
lid_l = 100
outer_w = lid_w + 5
outer_l = lid_l + 5
lid_th = 3.2
outer_h = 50 #!!
th = 5

res = (cq.Workplane("XY")
       .tag("bot")
       .box(outer_w, outer_l, outer_h, centered=(True, True, False))
       .faces(">Z")
       .shell(-th)
       .edges("|Z or <Z")
       .fillet(5)
       .faces(">Z")
       .rect(lid_w, lid_l)
       .cutBlind(-lid_th)
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 0, th))
       .rarray(lid_w - 10, lid_l - 10, 2, 2)
       #.rect(8, 8)
       .circle(5)
       .extrude(outer_h - lid_th - th)
       .faces(">Z")
       .rarray(lid_w - 10, lid_l - 10, 2, 2)
       .circle(3.5/2)
       .cutThruAll()
       .workplaneFromTagged("bot")
       .rarray(lid_w - 10, lid_l - 10, 2, 2)
       .polygon(6, 6.5)
       .cutBlind(4)
      )

show_object(res)
