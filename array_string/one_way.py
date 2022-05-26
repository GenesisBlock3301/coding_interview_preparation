def replace(string1: str,string2:str) -> bool:
    found_difference = False
    for i in range(0,len(string1)):
        if string1[i] != string2[i]:
            if found_difference:
                return False
            found_difference = True
    return True

def insert_remove(string1:str,string2:str) -> bool:
    index1 = 0
    index2 = 0
    while index1 < len(string1) and index2 < len(string2):
        if string1[index1] != string2[index2]:
            if index1 != index2:
                return False
            index2+=1

        else:
            index1+=1
            index2+=1
    return True


print(replace("pale","bale"))
print(insert_remove("Apple","Aple"))