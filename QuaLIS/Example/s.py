
def unitAdd():

  list2=["a","b","c"]

  list1=["a","c"]

  list1String=""

  for i in list1:
      list1String=list1String+str(i)

  for i in list2:
      if list1String.__contains__(i):
          pass
      else:
          print(i)


unitAdd()









