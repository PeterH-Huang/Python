
# assignment 5 part 2 
# Huang, Peter Helin 

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle(Point):
    def __init__(self,point1,point2,colour):
        ''' (Rectangle,point, point,string) -> None'''
        self.point1=point1
        self.point2=point2
        self.colour=colour

    def __eq__(self, other):
        '''(Rectangle,Reactangle)->bool'''
        return self.point1 == other.point1 and self.point2 == other.point2 and self.colour==other.colour
    def __repr__(self):
        '''(Rectangle)->str'''
        return 'Rectangle('+str(self.point1)+','+str(self.point2)+str(self.colour)+')'
    def __str__(self):
        '''(Rectangle)->str'''
        return 'I am a '+str(self.colour)+' rectangle with bottem left corner at '+str(self.point1)+' and top right corner at '+str(self.point2)+"."     
        
    def get_bottom_left(self):
        ''' (Rectangle) -> Point'''
        return self.point1
    def get_top_right(self):
        ''' (Rectangle) -> Point'''
        return self.point2
    def get_color(self):
        ''' (Rectangle) -> string'''
        return self.colour
    def reset_color(self,colour):
        ''' (Rectangle) -> None'''
        self.colour=colour
    def get_perimeter(self):
        ''' (Rectangle) -> number'''
        x=self.point2.get()[0]-self.point1.get()[0]
        y=self.point2.get()[1]-self.point1.get()[1]
        return 2*x+2*y
    def get_area(self):
        ''' (Rectangle) -> number'''
        x=self.point2.get()[0]-self.point1.get()[0]
        y=self.point2.get()[1]-self.point1.get()[1]
        return x*y
    def move(self,dx,dy):
        ''' (Rectangle) -> None'''
        self.point1.move(dx,dy)
        self.point2.move(dx,dy)

    def intersects(self,second):
        ''' (Rectangle) -> bool'''
        if self.point1.get()[0]>second.point2.get()[0] or self.point1.get()[1]>second.point2.get()[1] or self.point2.get()[0]<second.point1.get()[0] or self.point2.get()[1]<second.point1.get()[1]:
            return False
        return True
        
    def contains(self,x,y):
        ''' (Rectangle) -> bool'''
        return (x>=self.point1.get()[0] and x<=self.point2.get()[0] and y>=self.point1.get()[1] and y<=self.point2.get()[1])

class Canvas(Rectangle):
    def __init__(self,Rectangle=[]):
        ''' (Canvas,list) -> None'''
        self.C=Rectangle
    def __repr__(self):
        ''' (Canvas) -> string'''
        return"Canvas("+str(self.C)+")"
    def __len__(self):
        ''' (Canvas) -> integer'''
        return len(self.C)
    def add_one_rectangle(self,rectangle):
        ''' (Canvas,Rectangle) -> None'''
        self.C.append(rectangle)
    def count_same_color(self,colour):
        ''' (Canvas,string) -> integer'''
        counter=0
        for x in self.C:
            if x.get_color()==colour:
                counter=counter+1
        return counter
    def total_perimeter(self):
        ''' (Canvas) -> number'''
        total=0
        for gonna in range(len(self.C)):
            total=total+self.C[gonna].get_perimeter()
        return total
    def min_enclosing_rectangle(self):
        ''' (Canvas) -> Rectangle'''
        matrix=self.C[0].get_top_right().get()[0]
        for x in range(len(self.C)):
            if self.C[x].get_top_right().get()[0]>matrix:
                matrix=self.C[x].get_top_right().get()[0]
        may=self.C[0].get_top_right().get()[1]
        for i in range(len(self.C)):
            if self.C[i].get_top_right().get()[1]>may:
                may=self.C[i].get_top_right().get()[1]

        roblox=self.C[0].get_bottom_left().get()[0]
        for b in range(len(self.C)):
            if self.C[b].get_bottom_left().get()[0]<roblox:
                roblox=self.C[b].get_bottom_left().get()[0]

        bly=self.C[0].get_bottom_left().get()[1]
        for a in range(len(self.C)):
            if self.C[a].get_bottom_left().get()[1]<bly:
                bly=self.C[a].get_bottom_left().get()[1]

        return Rectangle(Point(roblox,bly),Point(matrix,may),'red')
    def common_point(self):
        ''' (Canvas) -> bool'''
        for on in range(len(self.C)-1):
            if not (self.C[on].intersects(self.C[on+1])):
                return False
            else:
                return True
    
