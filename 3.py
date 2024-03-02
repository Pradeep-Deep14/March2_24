my_list1=['I','Logical']
my_list2=['Love','Python']

#my_list=my_list1+my_list2
#print(my_list)

final_list=[]

for i in my_list1:
    for j in my_list2:
        final_list.append(i+" "+j)

print(final_list)