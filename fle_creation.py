##a=open(r'C:\Users\LENOVO\Desktop\aiml\sample.txt','w')
##a.write("Skill Up Coder (26) batch\n")
##a.write("ML session")
##s=["Skill Up coder\n","ML session"]
##a.writelines(s)

##a.close()
##a=open(r'C:\Users\LENOVO\Desktop\aiml\sample.txt','a')
##a.write("\nin 2-1 sem")
##a.close()
a=open(r'C:\Users\LENOVO\Desktop\aiml\sample.txt','r')
##s=a.read()
s=a.readlines()
for i in s:
    print(i)
a.close()
