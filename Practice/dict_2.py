def longest_word(sent):
    words = {k: len(k) for k in sent.split()}  
    print(words,"\n\n")  

    max_length = max(words.values())  
    longest_words = {k: v for k, v in words.items() if v == max_length}  
    
     
    return longest_words  
print(longest_word("The quick fox jumped over a lazy dog"))




def longest_word(sent):
    words = {k: len(k) for k in sent.split()}
    return {k: v for k, v in words.items() if v == max(words.values())}

print(longest_word("The quick fox jumped over a lazy dog"))
