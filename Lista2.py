import datetime

def q1():
    x = int(input('Digite um Número: '))
    y = int(input('Digite outro Número: '))
    z = x + y
    if z > 10:
        print(f"Resultado: {z}")

def q2():
    n1 = int(input('Valor 1: '))
    n2 = int(input('Valor 2: '))
    soma = n1 + n2
    if soma > 20:
        print(f"Resultado: {soma + 8}")
    else:
        print(f"Resultado: {soma - 5}")

def q3():
    num = int(input('Número: '))
    print("É múltiplo de 3" if num % 3 == 0 else "Não é múltiplo de 3")

def q4():
    num = int(input('Número: '))
    print("Divisível por 5" if num % 5 == 0 else "Não é divisível por 5")

def q5():
    num = int(input('Número: '))
    if num % 3 == 0 and num % 7 == 0:
        print("Divisível por 3 e 7")
    else:
        print("Não é divisível por ambos")

def q6():
    salario = float(input('Salário Bruto: '))
    prestacao = float(input('Valor da Prestação: '))
    if prestacao <= (salario * 0.3):
        print("Empréstimo CONCEDIDO")
    else:
        print("Empréstimo NEGADO")

def q7():
    num = int(input('Número: '))
    print("Está entre 20 e 50" if 20 <= num <= 50 else "Fora do intervalo")

def q8():
    num = int(input('Número: '))
    if num > 20: print("Maior do que 20")
    elif num == 20: print("Igual a 20")
    else: print("Menor do que 20")

def q9():
    nasc = int(input('Ano de nascimento: '))
    atual = datetime.date.today().year
    if nasc > atual or nasc < 1900:
        print("Ano inválido")
    else:
        print(f"Idade: {atual - nasc} anos")

def q10():
    nums = [int(input(f'N{i+1}: ')) for i in range(3)]
    print(f"Ordem crescente: {sorted(nums)}")

def q11():
    nums = [int(input(f'N{i+1}: ')) for i in range(3)]
    print(f"O maior é: {max(nums)}")

def q12():
    idade = int(input('Idade: '))
    if idade < 18: print("Menor de idade")
    elif 18 <= idade <= 65: print("Maior de idade")
    else: print("Maior de idade e maior de 65 anos")

def q13():
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    if media >= 7: status = "Aprovado"
    elif media < 3: status = "Reprovado"
    else: status = "em Prova Final"
    print(f"{nome} - Média: {media} - {status}")

def q14():
    sal = float(input('Salário: '))
    if sal <= 600: print("Isento")
    elif sal <= 1200: print(f"Desconto 20%: {sal*0.2}")
    elif sal <= 2000: print(f"Desconto 25%: {sal*0.25}")
    else: print(f"Desconto 30%: {sal*0.3}")

def q15():
    custo = float(input('Valor do produto: '))
    lucro = 0.45 if custo < 20 else 0.3
    print(f"Valor de venda: {custo * (1 + lucro)}")

def q16():
    idade = int(input('Idade: '))
    if 5 <= idade <= 7: print("Infantil A")
    elif 8 <= idade <= 10: print("Infantil B")
    elif 11 <= idade <= 13: print("Juvenil A")
    elif 14 <= idade <= 17: print("Juvenil B")
    elif idade >= 18: print("Sênior")

def q17():
    nome = input('Nome: '); idade = int(input('Idade: '))
    if idade <= 10: v = 30
    elif idade <= 29: v = 60
    elif idade <= 45: v = 120
    elif idade <= 59: v = 150
    elif idade <= 65: v = 250
    else: v = 400
    print(f"{nome}: R$ {v:.2f}")

def q18():
    meses = ["", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    m = int(input('Mês (1-12): '))
    print(meses[m] if 1 <= m <= 12 else "Mês inexistente")

def q19():
    p = sorted([int(input(f'Arqueiro {i+1}: ')) for i in range(3)], reverse=True)
    print(f"Pontos: {p}")
    if sum(p) > 100: print(f"Média: {sum(p)/3:.2f}")
    else: print("Equipe desclassificada")

def q20():
    saldo = float(input('Saldo médio: '))
    if saldo <= 500: p = 0
    elif saldo <= 1000: p = 0.3
    elif saldo <= 3000: p = 0.4
    else: p = 0.5
    print(f"Saldo: {saldo} | Crédito: {saldo * p}")

def q21():
    livro = input('Livro: '); tipo = input('Tipo (professor/aluno): ').lower()
    dias = 10 if tipo == 'professor' else 3
    print(f"Livro: {livro} | Dias: {dias}")

def q22():
    km = float(input('KM: ')); tipo = input('Tipo (A/B/C): ').upper()
    consumo = {'A': 12, 'B': 9, 'C': 8}
    print(f"Consumo estimado: {km / consumo.get(tipo, 1):.2f}L")

def q23():
    cal = {'p': [180, 230, 250, 350], 's': [75, 110, 170, 200], 'b': [20, 70, 100, 65]}
    p = int(input('Prato (1-4): '))-1; s = int(input('Doce (1-4): '))-1; b = int(input('Bebida (1-4): '))-1
    print(f"Total: {cal['p'][p] + cal['s'][s] + cal['b'][b]} cal")

def q24():
    placa = input('Placa: '); final = int(placa[-1])
    meses = ["Out", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set"]
    print(f"Renovação: {meses[final]}")

def q25():
    i = float(input('Índice: '))
    if i >= 0.5: print("1º, 2º e 3º grupos intimados")
    elif i >= 0.4: print("1º e 2º grupos intimados")
    elif i >= 0.3: print("1º grupo intimado")
    else: print("Índice aceitável")

# --- Menu Principal ---

menu = '''
--- LISTA DE EXERCÍCIOS (1-25) ---
Escolha o número da questão para executar.

Digite a opção: '''

try:
    opcao = input(menu)
    if opcao.isdigit() and 1 <= int(opcao) <= 25:
        eval(f'q{opcao}()')
    else:
        print("Opção inválida!")
except Exception as e:
    print(f"Erro: {e}")