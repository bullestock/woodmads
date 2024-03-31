from build123d import *
from cadquery import exporters

length, width, thickness = 20.0, 20.0, 6
center_hole_dia = 8.0

with BuildPart() as p:
    Box(length, width, thickness)
    Cylinder(radius=center_hole_dia / 2, height=thickness, mode=Mode.SUBTRACT)
    with Locations(p.faces().sort_by(Axis.Y)[-1]):
        with GridLocations(1, 12, 1, 2):
            CounterBoreHole(radius=1.5, counter_bore_radius=2.4,
                            counter_bore_depth=0.6, depth=10)
    fillet(p.edges().group_by(Axis.Y)[0], radius=0.5)
    fillet(p.edges().group_by(Axis.Y)[1], radius=0.4)

#show_object(p)
p.part.export_stl("bearingholder.stl")
