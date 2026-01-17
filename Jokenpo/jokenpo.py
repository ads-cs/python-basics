import random
def umj():
  print("--- Modo de um jogador selecionado ---")
  sinais = ["Pedra", "Papel", "Tesoura"]
  p2_index = random.randint(0, 2)
  try:
    p1_input = int(input("1. Pedra\n2. Papel\n3. Tesoura\nColoque a númeração do sinal que deseja jogar: "))
    p1_index = p1_input - 1
    if p1_index < 0 or p1_index > 2:
        print("Número fora do intervalo válido")
        return
  except ValueError:
    print("Escreva um número válido")
    return
  print("\nJO-KEN-PÔ\n")
  print(f"Jogador 1: {sinais[p1_index]}")
  print(f"Comp: {sinais[p2_index]}")

  if sinais[p2_index] == sinais[p1_index]:
    print("EMPATE")
  elif (sinais[p2_index] == "Pedra" and sinais[p1_index] == "Tesoura") or \
       (sinais[p2_index] == "Papel" and sinais[p1_index] == "Pedra") or \
       (sinais[p2_index] == "Tesoura" and sinais[p1_index] == "Papel"):
    print("Você Perdeu!!!")
  else:
    print("Você venceu!!!")

def doisj():
  print("--- Modo de dois jogadores selecionado ---")
  sinais = ["Pedra", "Papel", "Tesoura"]
  try:
    p1_input = int(input("      --- Jogador 1 ---\n1. Pedra\n2. Papel\n3. Tesoura\nColoque a númeração do sinal que deseja jogar: "))
    p2_input = int(input("      --- Jogador 2 ---\n1. Pedra\n2. Papel\n3. Tesoura\nColoque a númeração do sinal que deseja jogar: "))
    p1_index = p1_input - 1
    p2_index = p2_input - 1
    if p1_index < 0 or p1_index > 2 or p2_index < 0 or p2_index > 2:
        print("Número fora do intervalo válido")
        return
  except ValueError:
    print("Escreva um número válido")
    return
  print("\nJO-KEN-PÔ\n")
  print(f"Jogador 1: {sinais[p1_index]}")
  print(f"Jogador 2: {sinais[p2_index]}")

  if sinais[p2_index] == sinais[p1_index]:
    print("EMPATE")
  elif (sinais[p2_index] == "Pedra" and sinais[p1_index] == "Tesoura") or \
       (sinais[p2_index] == "Papel" and sinais[p1_index] == "Pedra") or \
       (sinais[p2_index] == "Tesoura" and sinais[p1_index] == "Papel"):
    print("Jogador 2 Venceu!!!")
  else:
    print("Jogador 1 Venceu!!!")

umj() if int(input("Um ou Dois Jogadores?(1/2): ")) == 1 else doisj()
