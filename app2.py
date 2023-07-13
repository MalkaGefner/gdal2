from osgeo import org

data_sorce=org.Open("./AFG_adm2.shp"),1
if data_sorce is None:
    print('Failed to open')
    exit(1)

layer=data_sorce.GetLayer()
new_field=org.FieldDefn("new",1)
layer.ResetReading()
layer.CreateField(new_field)

for vertex in range(layer.GetLayerDefn().GetFieldCount()):
    

for feture in layer:
    