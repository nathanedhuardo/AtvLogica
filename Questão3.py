totalAlunos = 36
errouTodas = 4
acertouApenas2 = 5
acertouApenas3 = 7
acertou1e2 = 9
acertou1e3 = 10
acertou3e2 = 7


#totalAlunos - errouTodas, para saber os alunos que acertaram pelo menos uma questão

#Alunos que acertaram todas as questões
A_U_B_U_C = (totalAlunos - errouTodas) - (acertou1e2 + acertou1e3 + acertou3e2)
print(f"A quantidade de alunos que acertaram todas foi: {A_U_B_U_C}")