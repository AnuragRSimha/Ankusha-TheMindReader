def without(string,character):
    string_list=[string[i] for i in range(0,len(string))]
    if(type(character)==str):
        char_list=[character[i] for i in range(0,len(character))]
    elif(type(character)!=list):
        char_list=list(character)
    else:
        char_list=character
    for i in range(0,len(string_list)):
        if(string_list[i] in char_list):
            string_list[i]=''
    return ''.join(string_list)
