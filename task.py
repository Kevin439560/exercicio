#QUESTÃO 1

INDICE:int = 13
soma:int = 0
k:int = 0
while(k < INDICE):
    k = k + 1
    soma = soma + k
    
print(soma)
#Resultado = 91



#QUESTÃO 2

def fibonnaci(cont1:int, cont2:int, Numeiro:int):
    if(Numeiro == 1):
        return "O numero pertence a sequencia Fibonacci"
    
    aux = cont2
    cont2 = cont1 + cont2
    cont1 = aux
    
    if(Numeiro == cont1):
        return "O numero pertence a sequencia Fibonacci"

    if(cont1 <= Numeiro):
        return fibonnaci(cont1, cont2, Numeiro)
    
    return "O numero não pertence a sequencia Fibonacci"

print(fibonnaci(0, 1, 13))
    
#QUESTÃO 3

#A) 1,3,5,7,9 
#B) 2,4,8,16,32,64,128 
#C) 0,1,4,9,16,25,36,49
#D) 4,16,36,64,100
#E) 1,1,2,3,5,8,13
#F) 2,10,12,16,17,18,19,200

#QUESTAO 4
#A solução envolve deixar uma das luzes ligadas por um periodo prolongado, desligá-la e ligar outra, assim,
#uma sala tera a lampada ligada, outra tera a lampada desligada e quente, e outra a lampada desligada e fria

#QUESTAO 5

def inverte(palavra:str):
    final = ""
    i = len(palavra) - 1
    while (i >= 0):
        final = final + (palavra[i])
        print(i)
        i -= 1
    print(final)
        
inverte("lamamal")
