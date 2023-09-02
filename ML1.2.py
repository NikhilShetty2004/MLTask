def binatointeger(binary):
   return int(binary,2)

lst=['0001','0011','0101','1011','1101','1111']
new_lst=list(map(binatointeger,lst))
new_lst.sort()
s = sum(new_lst) / 2
sum1, sum2, flag, ans = new_lst.pop(), 0, 0, []
for i in range(len(new_lst)-1):
     if (sum1 + new_lst[0]) <= s:
            sum1 += new_lst.pop(0)
     elif flag != 1:
      ans.append(sum1)
      flag = 1

     if flag == 1:
        sum2 = sum(new_lst)
        ans.append(sum2)
       
print(abs(ans[0] - ans[1]))



