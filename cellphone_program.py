from pyexpat import model

import cellphone_class as cc

manufact = 'Samsung'
model = 'Galaxy S7'
price = 799

#print initialized phone
phone_1 = cc.cellphone(manufact, model, price)
print('New phone Initialized')
print('manufact:', phone_1.get_manufact())
print('model:', phone_1.get_model())
print('retail price:', phone_1.get_retail_price())

#Set methods
manufact = input('Enter cell phone manufacturer: ')
model = input('Enter phone model: ')
price = int(input('Enter retail price: '))

phone_1.set_manufact(manufact)
phone_1.set_model(model)
phone_1.set_retail_price(price)

#display updated phone
print()
print('Phone updated')
print('manufact:', phone_1.get_manufact())
print('model:', phone_1.get_model())
print('retail price:', phone_1.get_retail_price())
