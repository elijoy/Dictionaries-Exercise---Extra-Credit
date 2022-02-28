file_object = open("book of John Text.txt", "r")

unwanted_char = ['.', ',', "(", ")", '"', "%", "'", ";", ":", "!"]
unwanted_char = str(unwanted_char)

words = file_object.readline()


for x in unwanted_char:
    words = words.replace(x,' ')
words = words.split()


wordlist = []
for i in words:
    wordlist.append(i)


wordfreq = {}
for word in words:
    if word in wordfreq:
        counter = wordlist.count(word)
        wordfreq[word] = counter
    else:
        wordfreq[word] = 1

for key in list(wordfreq.keys()):
    if key == "Father" and key != "fathers" and key != "father":
        print(key, ": ", wordfreq[key], sep='')
   

file_object.close()