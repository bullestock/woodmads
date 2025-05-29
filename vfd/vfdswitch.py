import cadquery as cq

# Shell thickness
th = 3

switch_w = 25.5
switch_l = 34.5
switch_offset = -5

# Screw support diameter
screw_sup_dia = 9
screw_sup_ff = 1
screw_dia = 3.5
screw_head_dia = 6.5
screw_head_h = 3

insert_l = 4.5
insert_r = 4.7/2

inner_w = 22 + 20 + 2*screw_sup_dia
inner_l = 60
outer_w = inner_w + th
outer_l = inner_l + th
outer_h = 50+2*th

gland_hole_d = 12.5
gland_x_dist = 22
gland_z_dist = 19
gland_hole_offset = -2

cut_h = 10

res = (cq.Workplane("XY")
       .tag("bot")
       # Shell
       .box(outer_w, outer_l, outer_h, centered=(True, True, False))
       .shell(-th)
       .edges("|Z or >Z")
       .fillet(3)
       .edges("<Z")
       .fillet(1)
       # Cutout for switch
       .faces(">Z")
       .workplane()
       .transformed(offset=(0, switch_offset, 0))
       .rect(switch_w, switch_l)
       .cutBlind(-th)
       # Screw supports
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 0, th*screw_sup_ff))
       .rarray(inner_w - 2*th, inner_l - 2*th, 2, 2)
       .circle(screw_sup_dia/2)
       .extrude(outer_h - 2*th*screw_sup_ff)
       # Screw holes
       .workplaneFromTagged("bot")
       .rarray(inner_w - 2*th, inner_l - 2*th, 2, 2)
       .circle(screw_dia/2)
       .cutBlind(outer_h-th)
       .workplaneFromTagged("bot")
       .rarray(inner_w - 2*th, inner_l - 2*th, 2, 2)
       .circle(screw_head_dia/2)
       .cutBlind(screw_head_h)
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 0, outer_h - cut_h))
       .rarray(inner_w - 2*th, inner_l - 2*th, 2, 2)
       .circle(insert_r)
       .cutBlind(insert_l)
       # Cable gland holes
       .faces(">Y")
       .workplane(centerOption='CenterOfMass')
       .tag("gland")
       .transformed(offset=(0, gland_hole_offset - gland_z_dist/2, 0))
       .circle(gland_hole_d /2)
       .cutBlind(-th)
       .workplaneFromTagged("gland")
       .transformed(offset=(0, gland_hole_offset + gland_z_dist/2, 0))
       .rarray(gland_x_dist, 1, 2, 1)
       .circle(gland_hole_d /2)
       .cutBlind(-th)
)

#show_object(res)

p1 = res.faces(">Z").workplane(-cut_h).split(keepTop=True)
p2 = res.faces(">Z").workplane(-cut_h).split(keepBottom=True)
show_object(p1)
#show_object(p2)
