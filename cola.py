int=número inteiro
float = números quebrados
bool = True or False
string:str:'Caracteres'

Exponenciação = **
Resto da divisão = %
Divisão inteira = //

Ordem de precedência das funções aritméticas
1° ()
2° **
3° *, /, //, %
4° +, - 

Exemplos de Controladores de texto
frase = "a"
print(frase[2::1])  #[início : fim : passo]
len(frase) #Mostra o número de caracteres
frase.count('o',0,13) #Mostra a quantidade de ('o') na string
frase.find() #Mostra localização inicial de alguma palavra inserida em ()
frase.replace('palavra 1', 'palavra 2') #Substitui a palavra 1 pela a palavra 2
frase.upper() #LETRAS MAÍUSCULAS 
frase.lower() #letras minusculas
frase.capitalize() #Deixa somente o primeiro caractere da string em maíusculo
frase.title() #Deixa as primeiras letras de todas as palavras em maíusculo
frase.strip() #Exclui espaços inuteis adicionadas antes e depois da string
frase.rstrip() #Exclui somente os espaços vazios da direita da string
frase.lstrip() #Exclui todos os espaços vazios da esquerda da string
frase.split() #Divide a string em vários pedaços separados pelos espaços vazios
'-'.join(frase) #Une as strings divididas com o caractere que está entre ' '


Manipulação de Listas

lista = [1, 2, 3, 4]
lista.append(5) #Adiciona um valor a lista
lista.insert(0, 5) #Nessa caso, adiciona o valor 5 na posição 0 da lista
del lista(3) #Exclui um valo da lista, nesse caso o valor na posição 3 que é o 2
lista.pop(3) #Mesma função do del
lista.remove(3) #Exclui o valor que está entre parenteses da lista, nesse caso removeria o 3 que está na posição 2
lista.pop() #Exclui o ultimo valor da lista


