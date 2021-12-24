import xml.etree.ElementTree as elemTree

tree2 = elemTree.parse("./xml/01_Bounding Box.xml")
user = tree2.find('./image')
#print(user.tag)
#print(user.attrib)
#print(user.get('id'))
#labelss = tree2.find("./image/box[2]")
#print(labelss.attrib)
unknown = 0
bike = 0
large_truck = 0
truck = 0
small_bus = 0
bus = 0
car = 0
l_u_point_x = []
l_u_point_y = []
r_d_point_x = []
r_d_point_y = []
p_point_x_center = []
p_point_y_center = []
p_point_x_center = []
p_point_y_center = []


for i in range(1, len(user), 1):
    params = tree2.find("./image/box[{0}]".format(i))
    l_u_point_x.append(params.get('xtl'))
    l_u_point_y.append(params.get('ytl'))
    r_d_point_x.append(params.get('xbr'))
    r_d_point_y.append(params.get('ybr'))
    p_point_x_center.append( float((float(l_u_point_x[i-1])+float(r_d_point_x[i-1]))/2) )
    p_point_y_center.append( float((float(l_u_point_y[i-1])+float(r_d_point_y[i-1]))/2) )


    if params.get('label') == 'unknown':
        unknown += 1
    if params.get('label') == 'bike':
        bike += 1
    if params.get('label') == 'large_truck':
        large_truck += 1
    if params.get('label') == 'truck':
        truck += 1
    if params.get('label') == 'small_bus':
        small_bus += 1
    if params.get('label') == 'bus':
        bus += 1
    if params.get('label') == 'car':
        car += 1

print(p_point_x[2], l_u_point_x[2])

print('인식되지 않음 : ', unknown)
print('인식된 자전거 수 : ', bike)
print('인식된 대형 트럭 수 : ', large_truck)
print('인식된 일반 트럭 수 : ', truck)
print('인식된 작은 버스 수 : ', small_bus)
print('인식된 일반 버스 수 : ', bus)
print('인식된 차량 수 : ', car)



