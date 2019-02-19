def list_sort(my_list):
   my_dict = {}
   evens = []
   odds = []
   chars =[]
   for value in my_list:
      if type(value) == int:
         if value % 2 == 0:
            evens.append(value)
         else:
             odds.append(value)
      if type(value) == str:
         chars.append(value)
      if type(value) == float:
         odds.append(value)

   
   sorted_evens = sorted(evens)
   sorted_odds = sorted(odds)
   sorted_characters = sorted(chars)

   my_dict = {
      'evens': sorted_evens,
      'odds': sorted_odds,
      'chars' : sorted_characters
   }

   return my_dict

my_list = [8.0, 'f', 9.0, 'o', 2, 76, 0, 'i', 44.7, 'x', 'e', 0.9, 5, 33, 0, 'g', 3.1]
result = list_sort(my_list)
print(result)
            


   
   
         
            
   
        

