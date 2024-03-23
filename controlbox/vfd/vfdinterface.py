import cadquery as cq

th = 2
stud_r = 3
stud_h = 2

res = (cq.Workplane("XY")
       .tag("bot")
       .box(30, 23, th, centered=(False, False, False))
       .edges("|Z")
       .fillet(1)
       .workplaneFromTagged("bot")
       .transformed(offset=(5.5, 8, 0))
       .circle(stud_r).extrude(-stud_h)
       .workplaneFromTagged("bot")
       .transformed(offset=(5.5, 18, 0))
       .circle(stud_r).extrude(-stud_h)
       .workplaneFromTagged("bot")
       .transformed(offset=(17, 10, 0))
       .circle(stud_r).extrude(-stud_h)
       .workplaneFromTagged("bot")
       .transformed(offset=(26, 19, 0))
       .circle(4).extrude(-stud_h)
       .workplane()
       .circle(2.5).cutThruAll()
      )

show_object(res)
