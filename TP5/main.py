import json
import re
import datetime

# Carregar stock do ficheiro JSON
def carregar_stock():
    try:
        with open("stock.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Guardar stock no ficheiro JSON
def guardar_stock(stock):
    with open("stock.json", "w") as f:
        json.dump(stock, f, indent=4)

# Listar os produtos disponíveis
def listar_produtos(stock):
    print("cod    | nome            | quantidade | preço")
    print("--------------------------------------")
    for produto in stock:
        print(f"{produto['cod']:6} | {produto['nome']:15} | {produto['quant']:<10} | {produto['preco']:.2f}€")

# Processar moedas inseridas
def processar_moedas(moeda_str):
    moedas = re.findall(r'(\d+)([ec])', moeda_str)
    saldo = 0
    for valor, tipo in moedas:
        valor = int(valor)
        if tipo == 'e':
            saldo += valor * 100  # Converter euros para cêntimos
        else:
            saldo += valor  # Já está em cêntimos
    return saldo

# Selecionar um produto
def selecionar_produto(cod, stock, saldo):
    for produto in stock:
        if produto["cod"] == cod:
            if produto["quant"] > 0:
                if saldo >= produto["preco"] * 100:
                    produto["quant"] -= 1
                    return saldo - int(produto["preco"] * 100), produto["nome"]
                else:
                    print(f"Saldo insuficiente! Saldo = {saldo}c; Pedido = {int(produto['preco']*100)}c")
                    return saldo, None
            else:
                print("Produto esgotado!")
                return saldo, None
    print("Código inválido!")
    return saldo, None

# Gerar troco
def calcular_troco(saldo):
    moedas = [50, 20, 10, 5, 2, 1]
    troco = {}
    for moeda in moedas:
        if saldo >= moeda:
            troco[moeda] = saldo // moeda
            saldo %= moeda
    return troco

# Loop principal
def main():
    stock = carregar_stock()
    saldo = 0

    current_time = datetime.datetime.now().strftime("%Y-%m-%d")

    print(f"maq: {current_time}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ").strip().upper()

        if comando == "LISTAR":
            listar_produtos(stock)
        
        elif comando.startswith("MOEDA"):
            match = re.search(r'MOEDA (.+)', comando)
            if match:
                saldo += processar_moedas(match.group(1))
                print(f"maq: Saldo = {saldo}c")
        
        elif comando.startswith("SELECIONAR"):
            match = re.match(r'SELECIONAR\s+([A-Z]\d+)', comando)
            if match:
                cod = match.group(1)
                saldo, produto = selecionar_produto(cod, stock, saldo)
                if produto:
                    print(f"maq: Pode retirar o produto dispensado \"{produto}\"")
                    print(f"maq: Saldo = {saldo}c")
        
        elif comando == "SAIR":
            troco = calcular_troco(saldo)
            print("maq: Pode retirar o troco:", ", ".join(f"{v}x {k}c" for k, v in troco.items()))
            print("maq: Até à próxima")
            guardar_stock(stock)
            break
        
        else:
            print("Comando inválido!")

if __name__ == "__main__":
    main()
