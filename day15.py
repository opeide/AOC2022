import numpy as np
from shapely import geometry

with open('day15_input.txt','r') as f:
    lines = f.readlines()
lines = [line.rstrip() for line in lines]
sensors_beacons = []
for line in lines:
    sensorX = line.split('=')[1].split(',')[0]
    sensorY = line.split('=')[2].split(':')[0]
    beaconX = line.split('=')[3].split(',')[0]
    beaconY = line.split('=')[4]
    print(sensorX, sensorY, beaconX, beaconY)
    sensors_beacons.append(([int(sensorX), int(sensorY)], [int(beaconX), int(beaconY)]))
print(sensors_beacons)

boundaries = []
for sensor, beacon in sensors_beacons:
    sensor, beacon = np.array(sensor), np.array(beacon)
    dist = np.linalg.norm(sensor-beacon, ord=1) #manhattan
    poly = [[0, dist], [dist, 0], [0, -dist], [-dist, 0]]
    poly = [[p[0]+sensor[0], p[1]+sensor[1]] for p in poly]
    poly.append(poly[0]) #close polygon
    boundaries.append(geometry.Polygon(poly))

def has_overlap(seg1, seg2):
    enveloping1 = seg1[0] <= seg2[0] <= seg2[1] <= seg1[1]
    enveloping2 = seg2[0] <= seg1[0] <= seg1[1] <= seg2[1]
    partial1 = seg1[0] <= seg2[0] <= seg1[1]
    partial2 = seg1[0] <= seg2[1] <= seg1[1]
    return enveloping1 or enveloping2 or partial1 or partial2

def merge_segments(seg1, seg2):
    return [min([seg1[0], seg2[0]]), max([seg1[1], seg2[1]])]


for row in [2000000]:
    rowLine = geometry.LineString([[-10e10,row], [10e10,row]])
    print(rowLine)
    segments = []
    #segment (start,end) includes end
    for i, boundary in enumerate(boundaries):
        #get row-boundary intersection points
        intersection = boundary.exterior.intersection(rowLine)
        print('boundary', boundary, 'sensorbeacon', sensors_beacons[i])
        #convert to line segment
        if not intersection.is_empty:
            start, end = None,None
            if intersection.geom_type.startswith('MultiPoint'):
                start, end = intersection.geoms[0].x, intersection.geoms[1].x
            elif intersection.geom_type.startswith('Point'):  
                start, end = intersection.x, intersection.x
            else: 
                raise Exception('unexpected intersection points') 
            start, end = sorted([start,end])
            print('intersection', start, end)
            segments.append([start, end])


    segments = np.array(sorted(segments)).astype(int).tolist()
    print(segments)
    for i in range(len(segments)-1):
        if has_overlap(segments[i], segments[i+1]):
            print(f'overlap {segments[i]} {segments[i+1]}')
            segments[i+1] = merge_segments(segments[i], segments[i+1])
            segments[i] = None
        print(segments)
    segments = [seg for seg in segments if seg is not None]
    print(segments)

    rowSum = sum([seg[1]-seg[0]+1 for seg in segments])
    #subtract num beacons in row
    beacons = np.unique([beacon for sens, beacon in sensors_beacons], axis=0)
    print(beacons)
    numRowBeacons = np.count_nonzero(beacons[:,1]==row)
    rowSum -= numRowBeacons
    print(rowSum)

#bonus:
#look for suitable boundary intersection clusters
interestPoints = []
maxPos = 4000000
for i in range(len(boundaries)-1):
    for j in range(i+1, len(boundaries)):
        b1, b2 = boundaries[i], boundaries[j]
        intersection = b1.exterior.intersection(b2.exterior)

        if not intersection.is_empty:
            if intersection.geom_type.startswith('Point'):  
                interestPoints.append([intersection.x, intersection.y])
            elif intersection.geom_type.startswith('MultiPoint'):
                for p in intersection.geoms:
                    interestPoints.append([p.x, p.y])
            elif intersection.geom_type.startswith('GeometryCollection'):
                for p in intersection.geoms:
                    if p.geom_type.startswith('Point'):  
                        interestPoints.append([p.x, p.y])
            else: 
                pass

interestPoints = np.array(sorted(interestPoints))
for p in interestPoints:
    if p[0] > maxPos or p[1] > maxPos:
        continue
    dists = np.linalg.norm(interestPoints - [p], axis=1)
    interest = sum(dists<=2)
    if interest != 4:
        continue
    pointCluster = interestPoints[dists<=2]
    unique = np.unique(pointCluster, axis=0)
    if len(unique) < 4:
        continue
    print(pointCluster, 'interesting')
    x = int(sorted(pointCluster[:,0])[2]) 
    y = int(sorted(pointCluster[:,1])[2])
    print(f'xy {x,y}')
    print(f'tuning freq {x*4000000 + y}')
    break


