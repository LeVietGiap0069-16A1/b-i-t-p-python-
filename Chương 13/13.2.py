
f = open("HumptyDumpty.txt",'r',encoding='utf-8')
print(f.read())

lines=[]
for line in open("HumptyDumpty.txt"):
    line=line.strip()
    a=line.split()
    lines.append(a)
print(lines)
   
    