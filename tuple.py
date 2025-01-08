tuple1 = ("apple",11.4,10,True,"banana")
print("Tuple with different data types: ",tuple1)

tuple2 = (10,20,30,40,50)
print("Tuple of integers: ",tuple2)

tuple3 = tuple2 + (9, )
print("New tuple after adding 9: ",tuple3)

tuple4 = tuple2.count(30)
print("Occurrences of 30 in tuple of integers is: ",tuple4)

tuple5 = tuple2[1:4]
print("Scliced tuple from index 1 to 3: ",tuple5)
