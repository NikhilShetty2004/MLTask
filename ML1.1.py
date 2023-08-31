
lambda_index=lambda y:len(y)
jumbled_superheroes=['DocTor_straNage','sPiDerman','Moon_KnigHt','caPTain_aMerIca','hUlk']
print(jumbled_superheroes)
object=enumerate(jumbled_superheroes)
indices=list(object)
for i in range(len(jumbled_superheroes)):
    jumbled_superheroes[i]=jumbled_superheroes[i].lower().replace('_',' ')
decoded_name=jumbled_superheroes
name_lengths=list(map(lambda_index,decoded_name))
decoded_name.sort(key=len)
print("Phase 5 kickoff list:")
for i in range(len(decoded_name)):
    x=decoded_name[i].title()
    print(str(i+1)+".  "+x)
