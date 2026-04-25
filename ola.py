import math

print("Medidor de risco Morte vs Velocidade!!")
Vel_Atual = float(input("Digite sua velociade média de viagem em km/h: "))
Vel_Maior = float(input("Digite a velocidade média maior desejada em km/h: "))
Aumento_Vel = ((Vel_Maior - Vel_Atual) / Vel_Atual)*100
e = 2.7182818284590

Risco_atual = (100)/(1+e**(-0.2*(Vel_Atual-84)))
Risco_maior = (100)/(1+e**(-0.2*(Vel_Maior)))
Aumento_risco = Risco_maior - Risco_atual


Economia_Tempo = (1-(Vel_Atual/Vel_Maior))*100

Risco_Final = (round(Risco_maior))
Risco_inicial = (round(Risco_atual))
Aumento_Vel_Final = (round(Aumento_Vel))
Aumento_Risco_Final = (round(Aumento_risco))
Economia_Tempo_Final = (round(Economia_Tempo))


print(f"O risco atualmente esta em {Risco_inicial}%")
print(f"O risco maior está em {Risco_Final}%")
print(f"O aumento da velocidade em foi de {Aumento_Vel_Final}%")
print(f"O aumento de risco foi de {Aumento_Risco_Final}%")
print(f"A economia de tempo foi de {Economia_Tempo_Final}%")

