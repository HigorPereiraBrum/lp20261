import random

def inputint(label: str, min: int = None, max: int = None) -> int:
    """Lê um número inteiro com validação opcional de faixa."""
    while True:
        try:
            valor = int(input(label))
            if min is not None and valor < min:
                print(f"Erro: O valor deve ser no mínimo {min}.")
                continue
            if max is not None and valor > max:
                print(f"Erro: O valor deve ser no máximo {max}.")
                continue
            return valor
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def inputfloat(label: str) -> float:
    """Lê um número real com validação."""
    while True:
        try:
            return float(input(label))
        except ValueError:
            print("Erro: Digite um número decimal válido.")

def gerar_palavra(max: int = 5) -> str:
    """Gera uma string aleatória para simular nomes de alunos/produtos."""
    letras = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letras) for _ in range(max)).capitalize()