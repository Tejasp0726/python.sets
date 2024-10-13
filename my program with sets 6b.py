Ration1 = {"Salt",  "Sugar", "Milk"}
Ration2 = {"Biscuit", "Milk", "Coffee Powder"}
print(Ration1)
print(Ration2)
union_set = Ration1 | Ration2
print(union_set)
intersection_set = Ration1 & Ration2
print(intersection_set)
difference_set = Ration1 - Ration2
print(difference_set)
sym_diff_set = Ration1 ^ Ration2 
print(sym_diff_set)
cars = {"Toyata Fortuner", "XUV 700", "NEXON", "POLO","Bugatti Chiron"}
cars.add("Ferrari")
print(cars)
cars.remove("Bugatti Chiron")
print(cars) 
cars.discard("Bugatti Chiron") 
print(cars)
cars.pop()
print(cars)
cars.clear()
print(cars)