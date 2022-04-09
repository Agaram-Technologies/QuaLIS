dic = {}

number=1

for i in range(15):

     dic.update({str(number):str(i)})

     number=number+1

print(dic.get('1'))