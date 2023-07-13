from osgeo import ogr 

data_sorce = ogr.Open("./AFG_adm2.shp")
if data_sorce is None:
    print('Failed to open sapefile')
    exit(1)

layer=data_sorce.GetLayer()
for feature in layer:
    area=feature.GetGeometryRef().GetArea()
    name2=feature.GetField("NAME_2")
    geom=feature.GetGeometryRef()
    ring=geom.GetGeometryRef(0)
    points=ring.GetPointCount()
    coordinates=[]
    for vertex in range(points): 
         coordinates.append(ring.GetPoint(vertex))      
    if area>1:
         print(f'FID:{feature.GetFID()},Area:{area},Name:{name2}')
         for coordinate in coordinates:
               print(f'coordinate:{coordinate}')

data_sorce=None