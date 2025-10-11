f = open('myfile.txt', 'r')
i = 0

while True:
    i = i + 1
    line = f.readline()
    
    if not line:
        break
    
    line = line.strip()
    
    if line:
        values = line.split(",")
        
        if len(values) >= 3:
            m1 = values[0]
            m2 = values[1]
            m3 = values[2]
            
            print(f"Maths Student {i} in Marks is {m1}")
            print(f"Science Student {i} in Marks is {m2}")
            print(f"English Student {i} in Marks is {m3}")


f=open('myfile2.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()