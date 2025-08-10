class data:
    def getdata(self,x):
        self.x = x
        
    def displaydata(self):
        print(self.x)

var = data()
name = input("enter a name")
var.get_data(name)
var.display_data()

    
