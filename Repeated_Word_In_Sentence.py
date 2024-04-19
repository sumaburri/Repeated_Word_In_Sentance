sentence=input('Enter a Sentence : ')
l=sentence.split()
new_l=[]
for word in l:
    if word not in new_l:
        new_l.append(word)
for word1 in new_l:
    if sentence.count(word1)>1:
         print(word1)

        
       
