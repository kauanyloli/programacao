'''Em um estacionamento, as tarifas são as seguintes (cumulativas):

Até duas horas: R$ 8,00/hora ou fração;
Entre três e quatro horas: R$ 5,00/hora ou fração;
Horas seguintes: R$ 3,00/hora ou fração;
Depois de 12h, o custo passa a ser fixo: R$ 30,00.

Faça um programa que solicite ao usuário o tempo que um veículo permaneceu no estacionamento (no for
mato HH:MM) e exiba o valor a ser pago pelo responsável.


Como exemplo, considere que o carro ficou 5 horas e 10 minutos no estacionamento; deve pagar: R$ 16,00 (pelas duas primeiras ho
ras) + R$ 10,00 (pela terceira e quarta horas) 
+ R$ 6,00 (pela quinta hora e fração da sexta hora): total de R$ 32,00'''

t=float(input('Informe o tempo que o veiculo permaneceu no estacionamento no formato HH:MM)'))

if t<=2:
    valor=8*t
    print(f'Valor que deve ser pago:',valor)
        
if 3<=t<=4:
    valor=5*t
    print(f'Valor que deve ser pago:',valor)
    
if 4<t<12:
    #16 das 2 primeiras horas e 10 da 3 e 4 logo 26
   valor=26+(t-4)*3
   print(f'Valor que deve ser pago:',valor)       

if t>=12:
    valor=30
    print(f'Valor que deve ser pago:',valor)    
                    