def binatointeger(binary):
   return int(binary,2)

lst=['0001','0011','0101','1011','1101','1111']
new_lst=list(map(binatointeger,lst))
while len(new_lst)>2 :
    min1=min(new_lst)
    new_lst.remove(min1)
    min2=min(new_lst)
    new_lst.remove(min2)
    total=min1+min2
    new_lst.append(total)
    new_lst.sort

print(new_lst)

