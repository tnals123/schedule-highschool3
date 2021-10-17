f=open('asdf.txt')
line=f.readlines()
total=0
score=0
for i in line:
    score=score+int(i)

f=open('asdfasdf.txt','w')
average=0
average=score/len(i)
f.write(str(average))
f.close()
