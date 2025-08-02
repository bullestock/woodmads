import cadquery as cq

w = 120
depth = 20
height = 5
bracket_th = 3
d1 = 13.5
d2 = 17.5
d3 = 6
factor = 0.8
mh_cc = 80
w1_offset = -50
w2_offset = -10
h1_offset = 25
h1_dia = 5
h_dist = 10
h2_offset = 50
h2_dia = 6.5
h2_dist = 20

result = (cq.Workplane("XY")
          .box(w, depth, height, centered=(True, True, False))
          .faces("<Z").workplane(centerOption="CenterOfMass", 
                             invert=True).tag("bottom")
          .workplaneFromTagged("bottom")
          # mount plate
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, (depth-bracket_th)/2, -2*height))
          .box(w, bracket_th, 2*height, centered=(True, True, False))
          # hex key
          .workplaneFromTagged("bottom")
          .transformed(offset=(h1_offset, depth/2 - bracket_th - h_dist, 0))
          .circle(h1_dia/2).cutThruAll()
          # hex key
          .workplaneFromTagged("bottom")
          .transformed(offset=(h2_offset, depth/2 - bracket_th - h_dist, 0))
          .circle(h2_dia/2).cutThruAll()
          # large wrench
          .workplaneFromTagged("bottom")
          .transformed(offset=(w1_offset, -depth/6, 0))
          .slot2D(d1, d3).cutThruAll()
          # small wrench
          .workplaneFromTagged("bottom")
          .transformed(offset=(w2_offset, -depth/6, 0))
          .slot2D(d2, d3).cutThruAll()
          # cut through
          .workplaneFromTagged("bottom")
          .transformed(offset=(w1_offset, -8, 0))
          .rect(d1*factor, 7).cutThruAll()
          .workplaneFromTagged("bottom")
          .transformed(offset=(w2_offset, -8, 0))
          .rect(d2*factor, 7).cutThruAll()
          # round edges
          #.edges("|X or |Y").fillet(1)
          .edges("|Y or <Y").fillet(1)
          # mounting holes
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, -height), rotate=(90, 0, 0))
          .rarray(mh_cc, 1, 2, 1)
          .circle(2)
          .cutThruAll()
)

show_object(result)

