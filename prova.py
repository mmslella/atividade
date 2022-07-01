nome = input('insira seu nome')
nota =int(input('insira a sua nota'))

if   0 < nota <= 5:
    nota = 6
  
if nota > 10:
    nota = 10
while nota == 0:
   break
f = open('dados.txt', "w")
f.write(f"{nome};{nota}\n")
f.close()


