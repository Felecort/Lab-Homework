ax1, ay1, ax2, ay2 = [ int(i) for i in input("первый прямоугольник - x y w h: ").split() ]

bx1, by1, bx2, by2 = [ int(i) for i in input("второй прямоугольник - x y w h: ").split() ]


s1 = ( ax1>=bx1 and ax1<=bx2 ) or ( ax2>=bx1 and ax2<=bx2 )
s2 = ( ay1>=by1 and ay1<=by2 ) or ( ay2>=by1 and ay2<=by2 )
s3 = ( bx1>=ax1 and bx1<=ax2 ) or ( bx2>=ax1 and bx2<=ax2 )
s4 = ( by1>=ay1 and by1<=ay2 ) or ( by2>=ay1 and by2<=ay2 )

print( "yes" if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)) else "no" )
