import time
starttime = time.process_time()

#for n in range(10):
    # stuff happens here
   # print("Right now, the number is", n)

my_favorite_words = ["baby yoda", "horse", "fuck", "long", "lizard", "list", "of", "words", "coding", "zebra"]
words_i_know = []
for i in my_favorite_words:
    print("computing", i)
    if i in words_i_know:
        # This will ONLY happen if a repeat is found
        print("you already know", i)
        break
    else:
        # Using this 'else' is optional but okay!
        words_i_know.append(i)
    if "z" in i:
        print("we dont need no z's around here")
        words_i_know.pop()
        print("deleting", i)
print(words_i_know)
endtime = time.process_time()
print("Finished in", endtime - starttime)