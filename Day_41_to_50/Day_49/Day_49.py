f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()


f=open('myfile2.txt','w')
f.close()



f=open('myfile.txt','w')
f.write("Hello Updaetd")
f.close()

f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()


f=open('myfile.txt','a')
f.write("Hello append")
f.close()


with open('myfile.txt','a') as f:
    f.write("Open With Automatically Close file")