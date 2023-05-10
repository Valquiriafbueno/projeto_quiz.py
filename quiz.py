print('Seja muito bem vindo ao quiz da Valquiria!')
usuario_res = input('Quer comecar? (Sim/Nao)')
print('usuario_res')

if usuario_res != 'Sim':
    quit()

pontos = 0

print('Comecando...')
print('O que é algaritmo?\n (A) Não tem sequência \n (B) Sequências de passos p/ execução de função \n (C) Sequência errada \n')
resposta1 = input('Resposta: ')

if resposta1 == 'B':
    print('Você Acertou!')
    pontos = pontos + 10
else:
    print('Você Errou!\n')  

print('Onde os algoritmos são usados?\n (A) Na área da programação \n (B) Na disciplina matemática \n (C) Nem uma das duas respostas anterior \n')  
resposta2 = input('Resposta: ')

if resposta2 == 'A':
    print('Você Acertou!')
    pontos = pontos + 10
else:
    print('Você Errou!\n')

print('Quando os algoritmos podem ser usados?\n (A) Em uma reunião \n (B) Quando estamos realizando uma sequência de passos p/ uma tarefa\n (C) Principalmente na tecnologia\n')
resposta3 = input('Resposta: ')

if resposta3 == 'B':
    print('Você Acertou!')
    pontos = pontos + 10
else:
    print('Você Errou!\n') 

print('Quais são os três principais conceitos do algoritmo?\n (A) Entrada, Saída, Variáveis\n (B) Dentro, Fora, Meio termo\n (C) Frente, Fundo, Lateral\n')   
resposta4 = input('Resposta: ')

if resposta4 == 'A':
    print('Você Acertou!')
    pontos = pontos + 10
else:
    print('Você Errou!\n')  

print('Como podemos usar o pensamento computacional no nosso dia a dia?\n (A) Para diminuir o tempo de execução nas tarefas do dia a dia\n (B) Para corrigir tarefas concluidas\n (C) As duas respostas anteriores estão erradas\n ')
resposta5 = input('Resposta: ')

if resposta5 == 'A':
    print('Você Acertou!')
    pontos = pontos + 10
else:
    print('Você Errou!')

print(f'Quiz acabou...Pontuação: {pontos}/15')





