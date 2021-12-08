a=open('C:\\Users\\Lenovo\\Desktop\\LST.txt', 'r')
ln=list(a)
a.close()
media1=0
media2=0
nr1=0
nr2=0
with open ('C:\\Users\\Lenovo\\Desktop\\Lista_clasei_11D_grupa1.txt','w') as f:
    d=['Nume','       ','Prenume','  ','Nota','Grupa\n']
    d='\t'.join(d)
    f.write(d)
f.close()

with open ('C:\\Users\\Lenovo\\Desktop\\Lista_clasei_11D_grupa2.txt','w') as g:
    h=['Nume','Prenume','Nota','Grupa\n']
    h='\t'.join(h)
    h=h.expandtabs(20)
    g.write(h)
g.close()

for b in ln:
    c=b.split()
    nota=int(c[2])
    grupa=c[3]
   #ultima coloana din fisier trebuie sa contina numarul grupei sub forma: 'gr1' sau 'gr2'
    if grupa[2]=='1':
        nr1+=1
        media1+=nota
        e=[str(c[0]),str(c[1]),str(nota),str(c[3]),'\n']
        e='     \t'.join(e)
        with open ('C:\\Users\\Lenovo\\Desktop\\Lista_clasei_11D_grupa1.txt','a') as f:
            f.write(e)
        f.close()
    if grupa[2]=='2':
        nr2+=1
        media2+=nota
        t=[str(c[0]),c[1],str(nota),c[3],'\n']
        t='\t'.join(t)
        t=t.expandtabs(20)      
        with open ('C:\\Users/Lenovo/Desktop/Lista_clasei_11D_grupa2.txt','a') as g:
            g.write(t)
        g.close()
with open ('C:/Users/Lenovo/Desktop/Lista_clasei_11D_grupa1.txt','a') as f:        
  l=('Media celor',str(nr1), 'studenti este=',str(media1/float(nr1)))
  l=' '.join(l)
  f.write(l)
f.close()
with open ('C:/Users/Lenovo/Desktop/Lista_clasei_11D_grupa2.txt','a') as g:        
  l2=('Media celor',str(nr2), 'studenti este=',str(media2/float(nr2)))
  l2=' '.join(l2)
  g.write(l2)
g.close()