#Write a program to return - 
# 1. zipped list from two lists 
# 2. elements of two lists zipped together, but 2nd list in reverse order 
# 3. elements of two lists zipped into a dictionary


s1 = {1,2,3,4}
s2= {'a','b','c','d'}
s3 = list(zip(s1,s2))

print(s3,"\n")

list1 = [10,20,30,40,50,60,70,80,90,100]
list2 = [100,200,300,400,500,600,700,800,900,1000]

for x,y in zip(list1,list2 [::-1]):
    print(x,y)


compaines = ['infosys','reliance','dell']
prices = [6565,9898,7676]

new_dict = {company: price for company, price in zip(compaines, prices)}


print ('\n{}'.format(new_dict))

