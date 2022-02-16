import InsectClass as i

# mosquito = i.Insect()
# housefly = i.Insect()

mosquito = i.Insect(2,4)
housefly = i.Insect(3,6)


mosquito.flight_length()
housefly.flight_length()


print('the mosquito can fly up to ' + str(mosquito.get_flight()) + ' miles')
print('the housefly can fly up to ' + str(housefly.get_flight()) + ' miles')

# print(mosquito.wings)
# print(housefly.wings)