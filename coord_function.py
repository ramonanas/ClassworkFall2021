def coord(tup1, tup2, x):
 
    x1 = tup1[0]
    y1 = tup1[1]
    x2 = tup2[0]
    y2 = tup2[1]
    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m*x1)
    retY = (m * x) + b
    return retY 