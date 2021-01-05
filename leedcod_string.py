#version 1
def romanToInt_3(s):
    

        dicts = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}

        summ = dicts[s[0]]
        i = 1
        while i < len(s) :
    
            if dicts[s[i-1]] < dicts[s[i]]:
                summ += abs(dicts[s[i]] - dicts[s[i-1]] - dicts[s[i-1]])     
            else:
                summ += dicts[s[i]]
            i+=1

        
        return summ


print("Общий вывод : ====", romanToInt_3("III"))
print("==============Общий вывод - ", romanToInt_3("MCMXCIV"))




#version 2
def romanToInt(s):
    

        dicts = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}

        summ = dicts[s[0]]

        
        for i in range(1, len(s)):
            befor_num = dicts[s[i-1]]
            curent = dicts[s[i]]                    
            curent_summ = befor_num - curent 
            print('curent_summ: ', curent_summ)

            if curent_summ < 0:
                summ += abs(curent_summ) - befor_num 
            else:
                summ += curent


        return summ
        
        


##print("Общий вывод : ====", romanToInt("MCMXCIV"))





import numpy as np

def romanToInt_2(s):
    dicts = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
    key = ['I', 'X', 'C']

    summ = dicts[s[0]]


    
    for i in range(1, len(s)):
        if dicts[s[i-1]] < dicts[s[i]]:
            summ += abs(((dicts[s[i-1]]) + (dicts[s[i-1]])) - dicts[s[i]]) 
        else:
            summ += dicts[s[i]]

        
    return summ



##print("==============Общий вывод - ", romanToInt_2("MCMXCIV"))
