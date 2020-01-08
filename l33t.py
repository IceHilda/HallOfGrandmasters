"""
l33t.py

Inputs: A single string
Outputs: The same string in l33tspeak

"""


def l33t(word_in=None, consonants=False):
    # Error handling for bad input:
    if word_in is None:
        print("Error: I need input!")
        return

    new_word = ""

    for c in word_in:
        #print("Looking at", c)
        if c == "e":
            new_word = new_word + "3"
        elif c == "a":
            new_word = new_word + "4"
        else:
            new_word = new_word + c

    final_word = ""
    if consonants==True:
        for c in new_word:
            if c == "t":
                final_word = final_word + "7"
            elif c == "h":
                final_word = final_word + "4"
            else:
                final_word = final_word + c
    else:
        final_word = new_word

    # End the function
    return final_word

def fast_l33t(word_in):
    vowels = ["a", "e", "o"]
    vowel_subs = ["4", "3", "0"]

    #new_word = []
    new_word = ""
    for c in range(len(word_in)):
        if word_in[c] in vowels:
            #new_word.append(vowel_subs[vowels.index(word_in[c])])
            new_word = new_word + vowel_subs[vowels.index(word_in[c])]
        else:
            #new_word.append(word_in[c])
            new_word = new_word + word_in[c]

    #return "".join(new_word)
    return new_word


def faster_l33t(word_in):
    vowels = ["a", "e", "o"]
    vowel_subs = ["4", "3", "0"]
    new_word = ""
    for c in word_in:
        if c in vowels:
            new_word = new_word + vowel_subs[vowels.index(c)]
        else:
            new_word = new_word + c
    return new_word

# [].index(x)    <- gives you the location of item x inside the list
# "".join(l)     <- creates a string from list l separated by the string at the beginning

#s = ["a", "b", "c"]
#print(s)
#print("".join(s))

#4

