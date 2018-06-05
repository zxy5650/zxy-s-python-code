#    facebook面试题：给定二维平面内的四个点，判断这四个点是否能组成正方形。坐标(x,y)为整数。输入的范围是[-10000,10000]

#分析，先想正方形的特性，四条边相等，但仅仅满足四条边相等的四边形除了正方形还有菱形，于是排除菱形的方法是正方形对角线相等的性质
#在坐标系中，正方形的竖直方向的坐标应该满足横坐标相等，水平方向的坐标应该满足纵坐标相等
#python解法如下
def position():
    x=int(input('请输入横坐标'))
    y=int(input('请输入纵坐标'))
    if -10000<=x<=10000:
        if -10000<=y<=10000:
            return (x,y)
        else:
            print('输入了错误的纵坐标')
    else:
        print('输入了错误的横坐标')
p1=position()
p2=position()
p3=position()
p4=position()
if abs(p1[0]-p3[0])==abs(p4[0]-p2[0]) and abs(p1[1]-p3[1])==abs(p4[1]-p2[1]):
    if abs(p1[0]-p2[0])==abs(p1[0]-p2[0])and abs(p1[1]-p4[1])==abs(p2[1]-p3[1]):
        print('该四边形为正方形')
else:
    print('该四边形不为正方形')