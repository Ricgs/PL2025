## **TPC2: Análise de um dataset de obras musicais**

**2025-02-22**

### **Autor:**
- Ricardo Gomes de Sousa
- A104524

### **Problema**
O problema consiste em criar um programa em Python que processa um ficheiro .csv e que realiza as seguintes queries:
- Lista ordenada alfabeticamente dos compositores musicais;
- Distribuição das obras por período: quantas obras catalogadas em cada período;
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.

### **Funcionamento**
O programa lê o ficheiro .csv, remove as quebras de linhas e espaços dentro de cada campo, tendo assim uma linha com os campos todos. Esses campos são depois separados e o programa realiza as queries pedidas, exibindo de seguida, os resultados. Para a query 1, o programa adiciona os compositores a um set e depois reorganiza alfabeticamente os nomes. Para a query 2, este cria um dicionário onde, para cada período, associa o número de obras que esse período contém. Para a query 3, este cria um dicionário onde, para cada período, é criada uma lista onde serão armazenados os títulos das obras que são organizadas alfabeticamente de seguida. 

### **Instrução de utilização**
```bash
$ python3 main.py <file_path>