import datetime
#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    x = int(input('Digite um Número: '))
    y = int(input('Digite outro Número: '))
    z = x + y
    if z > 10:
        print(f"Resultado: {z}")
#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
    n1 = int(input('Valor 1: '))
    n2 = int(input('Valor 2: '))
    soma = n1 + n2
    if soma > 20:
        print(f"Resultado: {soma + 8}")
    else:
        print(f"Resultado: {soma - 5}")
#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    num = int(input('Número: '))
    print("É múltiplo de 3" if num % 3 == 0 else "Não é múltiplo de 3")
#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
    num = int(input('Número: '))
    print("Divisível por 5" if num % 5 == 0 else "Não é divisível por 5")
#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
    num = int(input('Número: '))
    if num % 3 == 0 and num % 7 == 0:
        print("Divisível por 3 e 7")
    else:
        print("Não é divisível por ambos")
#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q6():
    salario = float(input('Salário Bruto: '))
    prestacao = float(input('Valor da Prestação: '))
    if prestacao <= (salario * 0.3):
        print("Empréstimo CONCEDIDO")
    else:
        print("Empréstimo NEGADO")
#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7():
    num = int(input('Número: '))
    print("Está entre 20 e 50" if 20 <= num <= 50 else "Fora do intervalo")
#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
    num = int(input('Número: '))
    if num > 20: print("Maior do que 20")
    elif num == 20: print("Igual a 20")
    else: print("Menor do que 20")
#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.

def q9():
    nasc = int(input('Ano de nascimento: '))
    atual = datetime.date.today().year
    if nasc > atual or nasc < 1900:
        print("Ano inválido")
    else:
        print(f"Idade: {atual - nasc} anos")
#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.

def q10():
    nums = [int(input(f'N{i+1}: ')) for i in range(3)]
    print(f"Ordem crescente: {sorted(nums)}")
#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    nums = [int(input(f'N{i+1}: ')) for i in range(3)]
    print(f"O maior é: {max(nums)}")
#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos
def q12():
    idade = int(input('Idade: '))
    if idade < 18: print("Menor de idade")
    elif 18 <= idade <= 65: print("Maior de idade")
    else: print("Maior de idade e maior de 65 anos")
#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

def q13():
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    if media >= 7: status = "Aprovado"
    elif media < 3: status = "Reprovado"
    else: status = "em Prova Final"
    print(f"{nome} - Média: {media} - {status}")
#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
    sal = float(input('Salário: '))
    if sal <= 600: print("Isento")
    elif sal <= 1200: print(f"Desconto 20%: {sal*0.2}")
    elif sal <= 2000: print(f"Desconto 25%: {sal*0.25}")
    else: print(f"Desconto 30%: {sal*0.3}")
#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
    custo = float(input('Valor do produto: '))
    lucro = 0.45 if custo < 20 else 0.3
    print(f"Valor de venda: {custo * (1 + lucro)}")
#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

def q16():
    idade = int(input('Idade: '))
    if 5 <= idade <= 7: print("Infantil A")
    elif 8 <= idade <= 10: print("Infantil B")
    elif 11 <= idade <= 13: print("Juvenil A")
    elif 14 <= idade <= 17: print("Juvenil B")
    elif idade >= 18: print("Sênior")
#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def q17():
    nome = input('Nome: '); idade = int(input('Idade: '))
    if idade <= 10: v = 30
    elif idade <= 29: v = 60
    elif idade <= 45: v = 120
    elif idade <= 59: v = 150
    elif idade <= 65: v = 250
    else: v = 400
    print(f"{nome}: R$ {v:.2f}")
#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def q18():
    meses = ["", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    m = int(input('Mês (1-12): '))
    print(meses[m] if 1 <= m <= 12 else "Mês inexistente")
#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

def q19():
    p = sorted([int(input(f'Arqueiro {i+1}: ')) for i in range(3)], reverse=True)
    print(f"Pontos: {p}")
    if sum(p) > 100: print(f"Média: {sum(p)/3:.2f}")
    else: print("Equipe desclassificada")
#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def q20():
    saldo = float(input('Saldo médio: '))
    if saldo <= 500: p = 0
    elif saldo <= 1000: p = 0.3
    elif saldo <= 3000: p = 0.4
    else: p = 0.5
    print(f"Saldo: {saldo} | Crédito: {saldo * p}")
#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

def q21():
    livro = input('Livro: '); tipo = input('Tipo (professor/aluno): ').lower()
    dias = 10 if tipo == 'professor' else 3
    print(f"Livro: {livro} | Dias: {dias}")
#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def q22():
    km = float(input('KM: ')); tipo = input('Tipo (A/B/C): ').upper()
    consumo = {'A': 12, 'B': 9, 'C': 8}
    print(f"Consumo estimado: {km / consumo.get(tipo, 1):.2f}L")
#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal
def q23():
    cal = {'p': [180, 230, 250, 350], 's': [75, 110, 170, 200], 'b': [20, 70, 100, 65]}
    p = int(input('Prato (1-4): '))-1; s = int(input('Doce (1-4): '))-1; b = int(input('Bebida (1-4): '))-1
    print(f"Total: {cal['p'][p] + cal['s'][s] + cal['b'][b]} cal")
#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.
def q24():
    placa = input('Placa: '); final = int(placa[-1])
    meses = ["Out", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set"]
    print(f"Renovação: {meses[final]}")
#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos
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