with open('file.txt','r') as f:
    print(f)
    f.seek(10)  #Skipping first 10 Character from file

    print(f.tell())  # return where to seek skiping
    data=f.read(5)  #after skipping that raed 5 character from file
    print(data)


with open('sample.txt','w') as f:
    f.write("Hello World !")
    f.truncate(5)
    
with open('sample.txt','r') as f:
    print(f.read())