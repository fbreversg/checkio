def checkio(text):

    #counting
    freq = {}
    for letra in text.lower():
        if letra.isalpha():
            freq[letra] = freq.get(letra, 0) +1
    
    #max value
    valores = list(freq.values())
    llaves = list(freq.keys())  
    maxi = llaves[valores.index(max(valores))]
    
    #mostRep, invalid value > than ord(z)
    mostRep = 'ç'
    
    #compare if there are more than 1 value
    for letra in freq.keys():
        print(letra, " ", freq[letra] )
        if freq[letra] == freq[maxi]:
            if ord(letra) < ord (mostRep):
                mostRep = letra
            
    
    return mostRep
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
