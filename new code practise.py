class Phone:
    def set_colour(self,colour):
        self.colour= colour
    def set_cost(self,cost):
        self.cost=cost
    def show_colour(self):
        print(self.colour)
    def show_cost(self):
        print(self.cost)


p1= Phone()
p1.set_colour("Blue")
p1.set_cost(10000)
p1.show_colour()
p1.show_cost()