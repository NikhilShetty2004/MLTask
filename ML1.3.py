def explode_chains(encoded_lists):
    for iteam in encoded_lists:
       firstTerm=0
       secondTerm=1
       thirdTerm=2
       
       while(firstTerm<=len(iteam)-3 and secondTerm<=len(iteam)-2 and thirdTerm<=len(iteam)-1):
           if iteam[thirdTerm]-iteam[secondTerm]==1 and iteam[secondTerm]-iteam[firstTerm]==1:
               a=iteam[firstTerm]
               b=iteam[secondTerm]
               c=iteam[thirdTerm]
               iteam.remove(a)
               iteam.remove(b)
               iteam.remove(c)
              
           else:
             firstTerm+=1
             secondTerm+=1
             thirdTerm+=1
           
    return encoded_lists       
               
           
encoded_lists=[[1,2,3,4,6],[5,7,8,9,15],[12,14,16,18],[10,11,12,13,16,17,18,20]]
print("encoded_list=")
print(encoded_lists)
result=explode_chains(encoded_lists)
print("After Explode Chains:")
print(result)

