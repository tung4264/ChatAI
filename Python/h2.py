ch = ['A','B','C','D']
def creat_dic(data):
    data_dict = {}
    for i in data:
        if i in data_dict:
            data_dict[i]+=1
        else:
            data_dict[i] = 1
    return data_dict
def count_char(*sData):
    dicData = creat_dic(ch)
    for i in sData:
        for j in i:
            char = j.upper()
            if char in dicData:
                dicData[char] +=1
            else:
                continue
    return dicData
    
print(count_char("ACC","DDd"))