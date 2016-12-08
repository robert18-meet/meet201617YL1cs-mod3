class Student:
    def __init__(self,name,hometown,age,height,favorite_ice_cream_flavor):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.favorite_ice_cream_flavor=favorite_ice_cream_flavor
    def short_summary(self):
        print(self.name+" "+self.hometown+" "self.age+" "+self.height+" "+self.favorite_ice_cream_flavor)
    def get_giraffe_gap(self,gap):
        self.gap=500-self.height
        
