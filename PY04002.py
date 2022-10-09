class Rectangle:
    def __init__(self,length,width,color):
        self.length = length
        self.width = width
        self.color = color[0:1:].upper() + color[1::].lower()
    def output(self):
        if self.length<=0 or self.width<=0:
            print("INVALID")
        else:
            print((self.length+self.width)*2,(self.length*self.width),self.color)

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
r.output()
