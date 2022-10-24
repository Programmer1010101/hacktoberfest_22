class rectangle:
    def __init__(self,lenght,width):
        self.__lenght = lenght
        self.__width = width

    def get_lenght(self):
        return self.__lenght
    def set_lenght (self,new_lenght):
        self.__lenght = new_lenght
    def get_width(self):
        return self.__width
    def set_width (self,new_width):
        self.__width = new_width
    def get_area(self):
        return self.__width * self.__lenght
    def get_perimeter (self):
        return ( self.__width + self.__lenght)*2
    def __str__(self):
        return str(self.__lenght)+"is the lenght and "+str(self.__width)+"is the width\n"+"area : "+str(rectangle.get_area())+"perimeter : "+ str(rectangle.get_perimeter ())
    
lenght = float(input("Enter lenght : "))
width = float(input("Enter width : "))

rectangle = rectangle(lenght ,width)
print(rectangle.get_lenght(),"is the lenght")
print(rectangle.get_width(),"is the width")
print("area : ",rectangle.get_area())
print("perimeter  : ",rectangle.get_perimeter ())
print(rectangle.__str__())

new_lenght = float(input("Enter new lenght : "))
new_width = float(input("Enter new width : "))
rectangle.set_lenght (new_lenght)
rectangle.set_width (new_width)
print(rectangle.get_lenght(),"is the lenght")
print(rectangle.get_width(),"is the width")
print("area : ",rectangle.get_area())
print("perimeter  : ",rectangle.get_perimeter ())
print(rectangle.__str__())
