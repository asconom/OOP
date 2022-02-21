class cellphone:

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    def set_manufact(self, new_manufact):
        self.__manufact = new_manufact


    def set_model(self, new_model):
        self.__model = new_model

    #set retail price
    def set_retail_price(self, new_price):
        self.__retail_price = new_price

    #return manufact
    def get_manufact(self):
        return self.__manufact

    #return model
    def get_model(self):
        return self.__model
    
    #return retail price
    def get_retail_price(self):
        return self.__retail_price
