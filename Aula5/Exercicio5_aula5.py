def avaliar_turma(qtd_alunos):
    notas = []
    for i in range(qtd_alunos):
        while True:
            try:
                nota = float(input(f"Digite a nota do aluno {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    media = sum(notas) / qtd_alunos
    print(f"A média da turma é: {media:.2f}")
qtd_alunos = int(input("Digite a quantidade de alunos: "))
avaliar_turma(qtd_alunos)