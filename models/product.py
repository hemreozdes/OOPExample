class Product():
    def __init__(self,name,price,quantity):
        self.__name=name
        self.__price=price
        self.__quantity=quantity
        
    @property
    def name(self)->str:
        return self.__name
    @name.setter
    def name(self,value:str)->None:
        if 3 <= len(value) <= 8:
            self.__name = value
    
    @property
    def price(self)->float:
        return self.__price
    @name.setter
    def price(self,value:float)->None:
        if value >= 0:
            self.__price = value
        
    @property
    def quantity(self)->float:
        return self.__quantity
    @name.setter
    def quantity(self,value:float)->None:
        if value >= 1:
            self.__quantity = value
        
    def getTotalPrice(self)->float:
        return self.__quantity * self.__price
    