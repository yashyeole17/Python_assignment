#Q.13) check if the items in list are sorted in ascending or descending order and
# print suitable message accordingly . otherwise print " Items are not sorted"

lst=[11,44,3,5,2,0,66,78,94,12]
if lst == sorted(lst, reverse=False):
  print("List items are sorted in ascending order")
elif lst == sorted(lst, reverse=True):
  print("List items are sorted in descending order")
else:
  print("list items are not sorted")