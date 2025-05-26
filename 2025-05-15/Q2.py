'''Faça um programa que solicite ao usuário um valor decimal positivo (esse valor corresponde ao valor de u
m saque em um terminal de caixa eletrônico)e que calcule a quantidade de cédulas de R$ 100,00, R$ 50,00,
R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.
'''
#feita!
#arrasei
import sys

Num= float(input('Por gentileza informe um  valor possitivo  desejado para o saque'))

if Num>0:
 cem= int(Num/100) 
 Num= Num-(cem*100)

 ciquenta= int(Num/50) 
 Num= Num-(ciquenta*50)

 vinte= int(Num/20) 
 Num= Num-(vinte*20)

 dez= int(Num/10) 
 Num= Num-(dez*10)

 cinco= int(Num/5) 
 Num= Num-(cinco*5)

 dois= int(Num/2) 
 Num= Num-(dois*2)

 Um= int(Num/1) 
 Num= Num-(Um*1)
 
 Cciquenta= int(Num/0.50)
 Num= Num-(Cciquenta*0.50)
 
 Cvintecinco= int(Num/0.25)
 Num=Num-(Cvintecinco*0.25)
          
 Cdez= int(Num/0.10)
 Num= Num-(Cdez*0.10)
 
 Ccinco= int(Num/0.05)
 Num= Num-(Ccinco*0.05)
 
 Cum= int(Num/0.01)
 Num= Num-Cum*0.01
  
 print('Numeros de celulas de R$ 100,00:',cem)
 print('Numeros de celulas de R$ 50,00',ciquenta)
 print('Numeros de celulas de R$ 20,00',vinte)
 print('Numeros de celulas de R$ 10,00',dez)
 print('Numeros de celulas de R$ 5,00',cinco)
 print('Numeros de celulas de R$ 2,00',dois)
 print('Numeros de moedas de R$ 1,00',Um)
 print('Numeros de moedas deR$ 0,50',Cciquenta)
 print('Numeros de moedas de R$ 0,25',Cvintecinco)
 print('Numeros de moedas de R$ 0,10',Cdez)
 print('Numeros de moedas de R$ 0,05',Ccinco)
 print('Numeros de moedas de R$ 0,01',Cum)
if Num<=0:
      sys.exit('por gentileza informe um valor valido')
     


    
