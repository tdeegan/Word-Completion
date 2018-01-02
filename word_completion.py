def fill_completions(fd):

    dictc = dict() 

    words = fd.read().replace('\n','').replace('.',' ').replace(',',' ').replace('!',' ').replace(';',' ').replace('-',' ').replace('?',' ') #replacing punctuation

    x = words.split()#x is a list of words 

    for i in x:#x i is a given word 
        i = i.lower()
        count = 0
        for each in i: #each is a letter in a given word
        
            if((count,each) in dictc):
            
                dictc[(count,each)].add(i)
                count +=1
            
            else:
                dictc[(count,each)] = {i}
                count += 1
                
    return dictc

def find_completions(prefix, c_dict):

    search_list = []

    n = len(prefix) 

    counter = 0

    while(counter < n):
    
        search_list.append((counter,prefix[counter]))
        counter += 1

        sl_length = len(search_list)

        output = set()

        counter2 = 1

    if(sl_length == 1):
        output = c_dict[search_list[0]]
    
    else:
        output = c_dict[search_list[0]]
        while(counter2 < sl_length):
            output = output.intersection(c_dict[search_list[counter2 - 1]].intersection(c_dict[search_list[counter2]]))
            counter2 += 1
    
    
    if(len(output) == 0):
        return output
    
    else:
        
        output_final = set()
        
        for item in output:
        
            if(item.isalpha() and len(item) > 1):
                output_final.add(item)
                
    return output_final
        

def main():

    f_test = open('ap_docs.txt','r')

    rdict = fill_completions(f_test)

    pf = ''

    while(True):
        
        try:

            pf = input("Enter prefix: ")

            result = find_completions(pf,rdict)
    
            if(len(result) == 0):
                print('No completions')
    
            else:
                for x in result:
                    print(x)
                    
        except EOFError:
            print('EOFError caught')
            exit(0)


if __name__ == '__main__':
    main()











        


        
        
    

    
    
    
    

    

    

    
    
    
    

