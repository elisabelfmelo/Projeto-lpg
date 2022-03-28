print('='*20,'VACINA COVID','='*20)

arq = open('dados.txt', "r")
linhas = arq.readlines()
result = []
for l in linhas:
   result.append(l.replace('\n', ''))
participantes = []
for d in result:
  if "," in d:
    individual = d.split(",")
    participantes.append(individual)

#1 linha
qtdf=0
qtdm=0
for pessoa in participantes:
    if "F" in pessoa:
      qtdf=qtdf+1
    if "M" in pessoa:
      qtdm=qtdm+1

percentF = qtdf * 100 / 10
percentM = qtdm * 100 / 10


  

#2 linha
j=0
Ad=0
idoso=0
for i in participantes:
	if((len(i)) >1):
		idade = int(i[1])
		if idade <=19 and idade>0:
			j= j + 1
		if idade>=20 and idade <59:
			Ad = Ad + 1
		if idade >=60:
			idoso = idoso+1
	
percentJ = j*100/10
percentAd = Ad*100/10
percentidoso = idoso*100/10
  

#3 linha
qtdV=0
qtdP=0
for x in participantes:		
 if "V" in x:
  	qtdV=qtdV+1
 if "P" in x:
		qtdP= qtdP + 1
percentV=qtdV*100/10
percentP=qtdP*100/10 

#4 linha
contraiu = 0
nao=0
for i in participantes:
  if "S" in i:
    contraiu=contraiu+1
  if "N" in i:
    nao=nao+1

    percentC=contraiu*100/10
    percentN= nao*100/10

    #eficacia geral

for p  in participantes:
  a = len([p for p in participantes if p[2] == 'P' and p[3] == 'S'])    
  
  b = len([p for p in participantes if p[2] == 'V' and p[3] == 'S'])    

  total=100*(a-b)/a

  #eficacia por genero feminino

placebo_f,vacina_f=0,0
for pessoa in participantes:
 if((len(pessoa)) >1):
   if pessoa[0]=="F" and pessoa[2] == "P" and pessoa[3] =="S":				     
    placebo_f = placebo_f + 1
 if pessoa[0] =="F" and pessoa[2] == "V" and pessoa[3] =="S":				     
      vacina_f = vacina_f + 1
																
#masculino
placebo_m=0
vacina_m=0
for pessoa in participantes:
 if((len(pessoa)) >1):
   if pessoa[0]=="M" and pessoa[2] == "P" and pessoa[3] =="S":				     
    placebo_m = placebo_m + 1
 if pessoa[0] =="M" and pessoa[2] == "V" and pessoa[3] =="S":				     
      vacina_m = vacina_m + 1
																
								
##eficacia genero

eficacia_F = 100*(placebo_f-vacina_f)/placebo_f
eficacia_m = 100*(placebo_m-vacina_m)/placebo_m

#eficacia por idade

#jovem
apj,bvj=0,0

for n in participantes:
	if((len(n)) >1):
		if int(n[1])<=19 and n[2] == "P" and n[3] =="S":	apj =apj+1
		if int(n[1])<=19 and n[2] == "V" and n[3] =="S":	bvj =bvj+1
								
#adulto
ap,av=0,0

for pessoa in participantes:
	if((len(pessoa)) >1):
		if int(pessoa[1])>=20 and int(pessoa[1])<=59 and pessoa[2] == "P" and pessoa[3] =="S":ap = ap + 1
		if int(pessoa[1])>=20 and int(pessoa[1])<=59 and pessoa[2]== "V" and pessoa[3] =="S":	av =av+1	

#idoso

ip,iv=0,0

for pessoa in participantes:
	if((len(pessoa)) >1):
		if int(pessoa[1])>=60 and pessoa[2] == "P" and pessoa[3] =="S":ip = ip + 1
		if int(pessoa[1])>=60 and pessoa[2] == "V" and pessoa[3] =="S":iv = iv + 1



##eficacia idade

eficacia_J = 100*(apj-bvj)/apj

eficacia_A = 100*(ap-av)/ap

eficacia_I = 100*(ip-iv)/ip




print('\n0-\n  1- Porcentagem de participantes do sexo feminino / masculino: \n  2- Porcentagem de eficácia geral da vacina: \n  3- Porcentagem de eficácia  considerando jovens, adultos e idosos: \n  4- Porcentagem de eficácia por gênero (feminino/masculino): \n  5- Sair')

op = int(input('\n Selecione uma opção: '))
print('='*60)

if op ==0 or op==1:
  print('\n0- \n 1- - Percentuais de participantes do gênero Feminino / Masculino \n \n  Participantes do sexo feminino: {:.0f} % \n'.format (percentF),' Participantes do sexo masculino: {:.0f} %'.format(percentF))
  print('\n  Adultos: {:.0f} % \n'.format(percentAd),' Jovens: {:.0f} % \n'.format(percentJ),' Idosos: {:.0f} % \n'.format (percentidoso))
  print("  Participantes vacinados: {:.0f} % \n".format(percentV),' Placebo: {:.0f} % \n'.format (percentP))
  print('  Contraiu covid: {:.0f} % \n'.format(percentC),' Não contraiu covid: {:.0f} % \n'.format (percentN))
  print('='*60,'\n')


else:
 if op ==3:
     print('3- Eficácia por idade \n\n', ' idoso: {:.0f} % \n'.format (eficacia_I),' jovem: {:.0f} % \n'.format(eficacia_J),' adulto: {:.0f} % \n'.format(eficacia_A))
     print('='*60,'\n')

 elif op==2:
  print('\n2- Eficácia geral: {:.2f} %'.format(total))
   
if op==4:
  print('4- Eficácia por gênero \n\n', 'feminino: {:.0f} % \n'.format(eficacia_F),'masculino: {:.0f} % \n'.format(eficacia_m))
  print('='*60,'\n')
elif op==5:
  print ("Encerrando Sistema...")
  exit(0)




  
