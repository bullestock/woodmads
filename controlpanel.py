import cadquery as cq

lid_w = 120
lid_l = 100
outer_w = lid_w + 5
outer_l = lid_l + 5
lid_th = 3.2
outer_h = 50
# Shell thickness
th = 5
# Flow indicator dimensions
fi_w1 = 39
fi_w2 = 50
fi_h = 40
fi_th = 23.7
fi_hose_z_offset = 14 # from top
fi_hose_y_offset = 24 # from center
fi_coupler_w = 16

res = (cq.Workplane("XY")
       .tag("bot")
       # Shell
       .box(outer_w, outer_l, outer_h, centered=(True, True, False))
       .faces(">Z")
       .shell(-th)
       .edges("|Z or <Z")
       .fillet(5)
       # Cutout for lid
       .faces(">Z")
       .rect(lid_w, lid_l)
       .cutBlind(-lid_th)
       # Screw supports
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 0, th))
       .rarray(lid_w - 10, lid_l - 10, 2, 2)
       .circle(5)
       .extrude(outer_h - lid_th - th)
       # Screw holes
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 0, outer_h/2))
       .rarray(lid_w - 10, lid_l - 10, 2, 2)
       .circle(4.2/2)
       .cutBlind(outer_h/2)
       # Hose holes
       .workplaneFromTagged("bot")
       .transformed(offset=(0, -fi_hose_y_offset, outer_h - lid_th - fi_hose_z_offset), rotate=(90, 90, 0))
       .circle(4.5)
       .cutThruAll()
       # Cable gland holes
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 30, 16), rotate=(90, 90, 0))
       .circle(12.5/2)
       .cutBlind(-outer_w)
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 5, 16), rotate=(90, 90, 0))
       .circle(12.5/2)
       .cutBlind(-outer_w)
       # Control plug
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 25, 20), rotate=(90, 90, 0))
       .circle(16/2)
       .cutBlind(outer_w)
       # Flow indicator support
       .workplaneFromTagged("bot")
       .transformed(offset=(0, -outer_l/2 + fi_h/2 + th, th))
       .rect(fi_w2, fi_h)
       .extrude(outer_h - lid_th - th)
       # Hole for flow indicator body
       .workplaneFromTagged("bot")
       .transformed(offset=(0, -outer_l/2 + fi_h/2 + th, outer_h))
       .rect(fi_w1, fi_h)
       .cutBlind(-(fi_th + lid_th))
       # Hole for flow indicator couplers
       .workplaneFromTagged("bot")
       .transformed(offset=(0, -fi_hose_y_offset, outer_h))
       .rect(fi_w2, fi_coupler_w)
       .cutBlind(-(fi_th + lid_th))
)

show_object(res)
