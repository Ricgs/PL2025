## **TPC4: Analisador Léxico para Linguagem de Query**

**2025-02-28**

### **Autor:**
- Ricardo Gomes de Sousa
- A104524

### **Problema**
O problema consiste em construir um analisador léxico para uma linguagem de query, permitindo a extração de tokens de comandos como SELECT, WHERE, variáveis, literais, identificadores e operadores.

### **Funcionamento**
O programa utiliza a biblioteca ply.lex para identificar e categorizar tokens numa consulta. Suporta palavras-chave (SELECT, WHERE, LIMIT), variáveis (?nome), identificadores (dbo:MusicalArtist), literais ("Chuck Berry"@en), números (1000) e símbolos ({, }, .).

### **Instrução de utilização**
```bash
$ python3 main.py