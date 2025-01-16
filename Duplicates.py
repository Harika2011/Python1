#This program is made to understand more on dictionaries 

students = {'id1':
            {'name':['Sara'],
             'class':['5'],
             'subject':['english,math,science']
             },
             'id2':
             {'name':['David'],
              'class':['5'],
              'subject':['english,math,science']
             },
             'id3':
             {'name':['Jhon'],
              'class':['5'],
              'subject':['english,math,science']
             },
             'id4':
             {'name':['Sara'],
              'class':['5'],
              'subject':['english,math,science']
             }
             
            }

result = {}
for key , value in students.items():
    if value not in result.values():
        result[key]=value

print(result)
