file_object = open("book of John text.txt", "r")

Word_Count = {"Father": 0, "God":0, "Christ":0, "Spirit": 0 , "spirit": 0 , "man":0}

for x in file_object:
    words = x.split(' ') #splits the string at each word with the space being the separator
    for y in words: #the y is for every word that is split in the list you created above
        if y in Word_Count: #if a specific word is found in the dictionary, you add 1
            Word_Count[y] += 1


file_object.close()

print("Father: ", Word_Count["Father"], sep = '') #you are asking for value for the key you gave
print("God: ", Word_Count["God"], sep = '')
print("Christ: ", Word_Count["Christ"], sep = '')
print("Spirit: ", Word_Count["Spirit"], sep = '')
print("spirit: ", Word_Count["spirit"], sep = '')
print("man: ", Word_Count["man"], sep = '')