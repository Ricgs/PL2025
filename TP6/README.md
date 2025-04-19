## **TPC6: Recursivo Descendente para expressões aritméticas**

**2025-04-19**

### **Autor:**
- Ricardo Gomes de Sousa  
- A104524  

### **Problema**
O objetivo deste trabalho é implementar um analisador sintático recursivo descendente capaz de interpretar e avaliar expressões aritméticas simples que envolvem inteiros, parênteses e os operadores +, -, * e /.

### **Funcionamento**
O programa recebe uma expressão aritmética e a analisa utilizando um parser LL(1), que divide a expressão em tokens e aplica regras de gramática recursivas para calcular o valor da expressão. Ele trata operadores (+, -, *, /) e parênteses, respeitando a precedência das operações. Caso encontre um erro de sintaxe, lança uma exceção. O resultado final é o valor calculado da expressão.

### **Instrução de utilização**
```bash
$ python3 main.py