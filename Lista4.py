import random
import math
from typing import Final
from util import inputint, inputfloat, gerar_palavra

'''
Lista de Exercícios: Coleções e Arquivos em Python
'''

VERMELHO: Final = '\033[31m'
VERDE: Final = '\033[32m'
RESET: Final = '\033[m'

# 1. Busca em lista de 15 números
def q1() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(15)]
    print(f"Lista gerada: {numeros}")
    numero: int = inputint('Digite o número a ser localizado na lista: ')
    try:
        posicao: int = numeros.index(numero)
        print(f'Número localizado na posição: {posicao}')
    except ValueError:
        print('Número não encontrado!')

# 2. Listagem numerada de 10 letras (ASCII 65-90)
def q2() -> None:
    letras: list[str] = [chr(random.randrange(65, 91)) for _ in range(10)]
    for posicao, letra in enumerate(letras):
        print(f'[{posicao}]: {letra}')

# 2.1 Gerador de senha aleatória (ASCII 40-126)
def q21() -> None:
    tamanho: int = inputint('Informe a qtde de caracteres (4-32): ', min=4, max=32)
    senha: list[str] = [chr(random.randrange(40, 127)) for _ in range(tamanho)]
    print(f'Senha sugerida: {"".join(senha)}')

# 3. Listagem numerada com Par ou Ímpar
def q3() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(15)]
    for pos, num in enumerate(numeros):
        status = "PAR" if num % 2 == 0 else "IMPAR"
        print(f'[{pos:<2}]: {num:>3} ({status})')

# 4. Múltiplos de seis em lista de 8
def q4() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(8)]
    print(f"Lista: {numeros}")
    mult6 = sum(1 for n in numeros if n % 6 == 0)
    print(f'Quantidade de múltiplos de 6: {mult6}')

# 5. Diário de classe para 15 alunos
def q5() -> None:
    alunos: list[dict] = []
    for c in range(1, 16):
        n1 = round(random.random() * 10, 1)
        n2 = round(random.random() * 10, 1)
        media = round((n1 + n2) / 2, 1)
        alunos.append({
            "mat": c,
            "nome": gerar_palavra(max=5),
            "n1": n1, "n2": n2, "md": media,
            "st": "Aprovado" if media >= 6 else "Reprovado"
        })
    print("MAT\tNOME\tN1\tN2\tMD\tST")
    for a in alunos:
        print(f"{a['mat']}\t{a['nome']}\t{a['n1']}\t{a['n2']}\t{a['md']}\t{a['st']}")

# 6. Reajuste salarial de 8%
def q6() -> None:
    salarios = [round(random.uniform(1412, 5000), 2) for _ in range(20)]
    print(f"{'ID':<3} | {'ATUAL':<10} | {'NOVO':<10}")
    for i, s in enumerate(salarios):
        novo = round(s * 1.08, 2)
        print(f"{i:<3} | R${s:>8.2f} | R${novo:>8.2f}")

# 7. Lucro de mercadorias (100 itens)
def q7() -> None:
    compras = [random.uniform(10, 100) for _ in range(100)]
    vendas = [c * random.uniform(0.9, 1.5) for c in compras]
    l1 = l2 = l3 = 0
    for c, v in zip(compras, vendas):
        lucro = ((v - c) / c) * 100
        if lucro < 10: l1 += 1
        elif lucro <= 20: l2 += 1
        else: l3 += 1
    print(f"Lucro < 10%: {l1}\n10% <= Lucro <= 20%: {l2}\nLucro > 20%: {l3}")

# 8. Gestão de 30 produtos (Dicionário)
def q8() -> None:
    estoque = {i: {"cod": i, "qtd": random.randint(1, 50), "v_comp": 10.0, "v_vend": 15.0} for i in range(1, 31)}
    op = inputint("Código do produto (1-30) ou 0 para todos: ")
    if op == 0:
        for p in estoque.values(): print(p)
    else:
        print(estoque.get(op, "Não encontrado"))

# 9. Elementos comuns entre conjuntos
def q9() -> None:
    c1 = [random.randint(1, 20) for _ in range(10)]
    c2 = [random.randint(1, 20) for _ in range(10)]
    comuns = list(set(c1) & set(c2))
    print(f"Lista 1: {c1}\nLista 2: {c2}\nComuns: {comuns}")

# 10 e 11. Fatoriais e Estatísticas
def q10() -> None:
    orig = [random.randint(1, 10) for _ in range(10)]
    fat = [math.factorial(n) for n in orig]
    pares = [n for n in fat if n % 2 == 0]
    print(f"Fatoriais: {fat}")
    print(f"Maior: {max(fat)} | Menor: {min(fat)} | Média: {sum(fat)/10:.1f}")
    print(f"Pares: {(len(pares)/10)*100}%")

def q11() -> None: q10()

# 12. Reserva de Mesas (30 mesas de 5 lugares)
def q12() -> None:
    mesas = [5] * 30
    total = 150
    while total > 0:
        cod = inputint("Mesa (1-30, 0 p/ sair): ")
        if cod == 0: break
        if 1 <= cod <= 30:
            qtd = inputint(f"Lugares (Disp: {mesas[cod-1]}): ")
            if qtd <= mesas[cod-1]:
                mesas[cod-1] -= qtd
                total -= qtd
                print(f"{VERDE}Reservado!{RESET}")
            else: print(f"{VERMELHO}Sem lugares!{RESET}")
    print("Encerrado.")

# 13. Reserva de Passagens Aéreas
def q13() -> None:
    voos = {random.randint(100, 999): 5 for _ in range(10)}
    print(f"Voos: {voos}")
    while True:
        v = inputint("Voo (0 p/ sair): ")
        if v == 0: break
        if v in voos and voos[v] > 0:
            id_c = inputint("Identidade: ")
            voos[v] -= 1
            print(f"OK! Cliente {id_c} no Voo {v}")
        else: print("Voo lotado ou inexistente.")

# 14. Quadrado de 50 números
def q14() -> None:
    l1 = [random.randint(1, 10) for _ in range(50)]
    l2 = [n**2 for n in l1]
    print(f"Original: {l1}\nQuadrados: {l2}")

# 15. Contar repetidos ao último número
def q15() -> None:
    nums = []
    while len(nums) < 100:
        n = inputint("Número (0 p/ parar): ")
        if n == 0: break
        nums.append(n)
    if nums:
        print(f"O último foi {nums[-1]} e apareceu {nums.count(nums[-1])} vezes.")

# 16. Estatísticas de 100 reais
def q16() -> None:
    l = [round(random.uniform(10, 50), 1) for _ in range(100)]
    media = sum(l) / 100
    print(f"Iguais a 30: {l.count(30.0)}")
    print(f"Maior que média ({media:.1f}): {sum(1 for x in l if x > media)}")
    print(f"Igual à média: {l.count(media)}")

# 17. Inverter 30 inteiros
def q17() -> None:
    l = [random.randint(1, 100) for _ in range(30)]
    print(f"Original: {l}\nInversa: {l[::-1]}")

# 18. Únicos e ordenados
def q18() -> None:
    l = [random.randint(1, 15) for _ in range(20)]
    print(f"Original: {l}\nOrdenada/Única: {sorted(list(set(l)))}")

# 19. Busca Telefone por Código
def q19() -> None:
    agenda = {i: f"9{random.randint(8000, 9999)}-{random.randint(1000, 9999)}" for i in range(100, 130)}
    cod = inputint("Código para busca (100-129): ")
    print(f"Telefone: {agenda.get(cod, 'Não encontrado')}")

# 20. Ordenação de Alunos por Nota
def q20() -> None:
    alunos = [{"m": i, "n": round(random.uniform(0, 10), 1)} for i in range(1, 101)]
    alunos_ord = sorted(alunos, key=lambda x: x['n'], reverse=True)
    for a in alunos_ord: print(f"Mat: {a['m']:<3} | Nota: {a['n']}")

# Menu Principal
try:
    questao = inputint('Questão a ser executada (1-20 ou 21,31): ')
    func_name = f'q{questao}'
    if func_name in locals():
        locals()[func_name]()
    else:
        print("Questão não implementada.")
except Exception as e:
    print(f"Erro: {e}")