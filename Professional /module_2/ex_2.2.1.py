def short_way():
    a1 = int(input())
    b2 = int(input())
    c3 = int(input())

    way_1 = a1 + b2 + b2 + a1
    way_2 = a1 + c3 + c3 + a1
    way_3 = b2 + c3 + c3 + b2
    way_4 = a1 + a1 + b2 + b2
    way_5 = a1 + c3 + b2

    a = min([way_1, way_2, way_3, way_4, way_5])
    return a

print(short_way())