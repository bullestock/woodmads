import cadquery as cq

# Shell thickness
th = 3

switch_w = 25.5
switch_l = 34.5
switch_offset = -28

thermo_offset = 30

# Screw support diameter
screw_sup_dia = 9
screw_sup_ff = 1
screw_dia = 3.5
screw_head_dia = 6.5

insert_l = 4.5
insert_r = 4.7/2

inner_w = 70
inner_l = 120
outer_w = inner_w + th
outer_l = inner_l + th
outer_h = 100

gland_hole_d = 12.5
gland_x_dist = 22
gland_hole_offset = -30

lv_x_dist = 10
lv_hole_d = 4
lv_hole_offset = 39

cut_h = 10

screw_head_h = outer_h - cut_h - 15

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
       # Thermometer cutout
       .workplaneFromTagged("bot")
       .transformed(offset=(0, thermo_offset, 10))
       .rect(32.5, 21.5)
       .cutBlind(outer_h)
       # Cable gland holes
       .faces(">Y")
       .workplane(centerOption='CenterOfMass')
       .tag("gland")
       .transformed(offset=(0, gland_hole_offset, 0))
       .rarray(gland_x_dist, 0, 2, 1)
       .circle(gland_hole_d /2)
       .cutBlind(-th)
       # Holes for: thermo sensor, pump power, 3 x motor fan
       .faces(">Y")
       .workplane(centerOption='CenterOfMass')
       .tag("gland")
       .transformed(offset=(0, lv_hole_offset, 0), rotate=(0, 0, 90))
       .rarray(0, lv_x_dist, 1, 5)
       .slot2D(lv_hole_d, lv_hole_d /2)
       .cutBlind(-th)
)

insert_l = 4.5
insert_r = 4.1/2
insert_sr = 1.75

def round_standoff(d, h, d1=None):
    max_d = min(h, 3*insert_l)
    if d1 is None:
        d1 = d
    return (cq.Workplane()
            .circle(d/2)
            .workplane(h)
            .circle(d1/2)
            .loft()
            .faces(">Z")
            .circle(insert_r).cutBlind(-insert_l)
            .faces(">Z")
            .circle(insert_sr+.25).cutBlind(-max_d)
            )

standoff_h = 5
standoff_d = 10

standoff = round_standoff(standoff_d, standoff_h)

v_standoff = round_standoff(standoff_d, standoff_h, d1=standoff_d*1.5)

sx, sy = 22.5, -(inner_l/2 - 10)
standoff1 = (res
             .workplaneFromTagged("bot")
             .transformed(offset=(sx, sy, th))
             .eachpoint(lambda loc: standoff.val().moved(loc), True))

standoff2 = (res
             .workplaneFromTagged("bot")
             .transformed(offset=(sx - 46.8, sy + 79, th))
             .eachpoint(lambda loc: standoff.val().moved(loc), True))

res = res.union(standoff1).union(standoff2)

standoff3 = (res
             .faces(">Y")
             .transformed(offset=(-20, -20, -(th+standoff_h)))
             .eachpoint(lambda loc: v_standoff.val().moved(loc), True))

standoff4 = (res
             .faces(">Y")
             .transformed(offset=(-20, 20, -(th+standoff_h)))
             .eachpoint(lambda loc: v_standoff.val().moved(loc), True))

res = res.union(standoff3).union(standoff4)

#show_object(res)

p1 = res.faces(">Z").workplane(-cut_h).split(keepTop=True)
p2 = res.faces(">Z").workplane(-cut_h).split(keepBottom=True)
#show_object(p1)
show_object(p2)
