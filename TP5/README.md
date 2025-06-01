## **TPC5: Simulador de Máquina de Vending**

**2025-03-15**

### **Autor:**
- Ricardo Gomes de Sousa  
- A104524  

### **Problema**
O problema consiste em construir um simulador de uma máquina de vending, permitindo a interação do utilizador através de comandos simples, como listar produtos, inserir moedas, selecionar um item e sair.

### **Funcionamento**
O programa carrega um ficheiro `stock.json` contendo os produtos disponíveis e os seus respetivos preços e quantidades. Suporta os seguintes comandos:

- `LISTAR`: Exibe os produtos disponíveis na máquina.
- `MOEDA X`: Permite inserir moedas (exemplo: `MOEDA 1e, 50c, 10c`).
- `SELECIONAR COD`: Seleciona um produto pelo código (exemplo: `SELECIONAR A23`).
- `SAIR`: Finaliza a interação, devolvendo o troco em moedas.

O saldo é gerido internamente em cêntimos. A cada interação, o programa verifica a validade dos comandos e responde de acordo com a lógica da máquina de vending. O sistema utiliza expressões regulares para identificar e processar os comandos corretamente, garantindo que apenas entradas válidas sejam aceites.

### **Instrução de utilização**
```bash
$ python3 main.py