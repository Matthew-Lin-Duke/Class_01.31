def line_input():
    x1 = input("x1:")
    y1 = input("y1:")
    


def cal_y(p1,p2,x3):
    y3 = ((x3 - p1[0])/(p1[0]-p2[0]))*(p1[1]-p2[1])+ p1[1]
    return y3


def on_line(p1, p2, p3):
    flag = False
    k = (p1[1]-p2[1])/(p1[0]-p2[0])
    temp_y3 = (p3[0] - p1[0])*k + p1[1]
    print(temp_y3)
    if temp_y3 == p3[1]:
        flag = True
    return flag
    
    

if __name__ == "__main__":
    #line_input()
    p1 = (9,10)
    p2 = (4,6)
    p3 = (2,4)
    p4 = (30, 26.8)
    x3 = 30
    y3 = cal_y(p1,p2,x3)
    print(y3)
    flag_1 = on_line(p1, p2, p4)
    print(flag_1)

