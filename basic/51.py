st=input("please enter the message = ")
words=st.split(" ")
coding=input(" for coadind 1, for decodin 0")
coding=True if(coding=="1") else False
if(coding):
    nword=[]
    for word in words:
     if(len(word)>=3):
         r="spd"
         r2="jklf"
         st1=r+word[1:]+word[0]+r2
         nword.append(st1)
     else:
         nword.append(words[::-1])
    print(" ".join(nword))

else:
    nword=[]
    for word in words:
       if(len(word)>=3):
        st1=word[3:-3]
        st1=st1[-1] + st1[:-1]
        word.append(st1)
    else:
         nword.append(word[ : :-1])
    print(" ".join(nword))
