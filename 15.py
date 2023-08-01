#Q.15) check if the items in list are sorted in ascending or descending order and
# print suitable message accordingly . otherwise print " Items are not sorted"

lst=[1,2,3,4,5,6,7,8,9,10]

if lst==sorted(lst,reverse=False):
  print(f" list items are sorted in ascending order")

elif lst==sorted(lst,reverse=True):
  print(f" list items are sorted in descending order")

else:
  print(f" list items are not sorted")