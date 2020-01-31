def line_input():
    x1 = input("x1:")
    y1 = input("y1:")
    


def cal_y(p1,p2,x3):
    y3 = ((x3 - p1[0])/(p1[0]-p2[0]))*(p1[1]-p2[1])+ p1[1]
    return y3

if __name__ == "__main__":
    #line_input()
    p1 = (9,10)
    p2 = (4,6)
    x3 = 30
    y3 = cal_y(p1,p2,x3)
    print(y3)
