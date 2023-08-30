jumbled_superheroes=['dOcToR_sTranGe','sPidErMan','mOoN_kNiGht','cApTaIn_AmErICa','hUlK']
l1=enumerate(jumbled_superheroes)
indices=[]
decoded_names=[]
for count,ele in l1:
    indices.append(count)
    ele=ele.lower() 
    ele=ele.replace('_',' ')
    decoded_names.append(ele)
name_lengths=list(map(lambda x:len(x),decoded_names))
indices.sort(key=lambda i:name_lengths[i])
j=0
for i in indices:
    print(f"{j+1}. {decoded_names[i].title()}") 
    j=j+1