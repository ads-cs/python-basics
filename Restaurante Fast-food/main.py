vl = [["Podrão", 21.63],
      ["Podrão 2.0", 43.26],
      ["Podrão 3.0", 64.89],
      ["Cheesepoor", 29.90],
      ["Podrão Bacon", 31.90]]

vs = [["Divertidolé", 5.00],
      ["Alegrelé", 6.50],
      ["Sorvetelé", 7.00],
      ["Tristelé", 0.50],
      ["Gentilvetelé", 10.00],
      ["Picolélé", 40.00],
      ["Picolélé 3.0", 120.00]]
vf = []
v = 0
print("         --- BEM VINDO AO PYTHONLÉ-BURGUER ---")
def cardápio():
  while True:
    try:
      print("\n\n         --- Categorias ---")
      choice = int(input(f"1. Hamburguers\n2. Sobremesas\nEscolha uma categoria pela numeração:"))
      if choice == 1:
        print("\n\n         --- Hamburguers ---")
        max_len = max(len(item[0]) for item in vl)
        for i, item in enumerate(vl):
            print(f"{i+1}. {item[0]:<{max_len}} |     R$ {item[1]:.2f}")
        pedido(vl)
        break
      elif choice == 2:
        print("\n\n         --- Sobremesas ---")
        max_len = max(len(item[0]) for item in vs)
        for i, item in enumerate(vs):
            print(f"{i+1}. {item[0]:<{max_len}} |     R$ {item[1]:.2f}")
        pedido(vs)
        break
      else:
        print("Escolha inválida. Por favor, escolha entre as númerações (1 ou 2).")
    except ValueError:
      print("Entrada inválida. Por favor, utilize as númerações (1 ou 2).")

def pedido(menu):
  global v
  global vf
  while True:
    try:
      item_choice = int(input("Escolha pela númeração do cardápio oque deseja escolher: "))
      if 1 <= item_choice <= len(menu):
        vf.append(menu[item_choice - 1][0])
        v += menu[item_choice - 1][1]
        print(f"\n{vf[-1]} adicionado!. Total provisório: R$ {v:.2f}")
        break
      else:
        print("Escolha inválida. Por favor, escolha uma numeração válida do cardápio.")
    except ValueError:
      print("Entrada inválida. Por favor, utilize as númerações do cardápio.")

def interface(resposta):
  while True:
    try:
      if resposta == "S":
          cardápio()
          break
      elif resposta == "N":
          print("Compra cancelada.")
          break
      else:
          print("Valor indesejado")
          resposta = str(input("Gostaria de iniciar a compra? S/N: ")).capitalize()
    except ValueError:
      print("Valor indesejado")

resposta = str(input("Gostaria de iniciar a compra? S/N: ")).capitalize()
while True:
  interface(resposta)
  while True:
    try:
        response = str(input("\nGostaria de finalizar a compra? S/N: ")).capitalize()
        if response == "S":
            print("\nItens comprados:")
            for item in vf:
                print(item)
            print(f"\n\nValor da compra sem desconto aplicado: R$ {v:.2f} ")
            discount = 0
            if 10 <= v <= 99:
                discount = v * 0.05
                print(f"\n5% de desconto aplicado: R$ {discount:.2f} (Compra entre R$10 e R$99)")
            elif 100 <= v <= 999:
                discount = v * 0.10
                print(f"\n10% de desconto aplicado: R$ {discount:.2f} (Compra entre R$100 e R$999)")
            elif v >= 1000:
                discount = v * 0.15
                print(f"\n15% de desconto aplicado: R$ {discount:.2f} (Compra de mais de R$1000)")

            total_with_discount = v - discount
            print(f"\nTotal da compra: R$ {total_with_discount:.2f}")
            break
        elif response == "N":
            break
        else:
            print("Valor indesejado")
    except ValueError:
        print("Valor indesejado")
  if response == "S":
      break
