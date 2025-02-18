TPC1: Somador on/off

2025-02-10

Autor: Ricardo Gomes de Sousa A104524

Problema
O problema consiste em criar um programa em Python que processa um texto e soma todas as sequências de dígitos encontradas. No entanto, a soma pode ser ativada ou desativada dependendo da presença das palavras "On" e "Off" (independentemente da capitalização). Sempre que a string "Off" aparecer, a soma deve ser interrompida, e sempre que "On" aparecer, deve ser retomada. Além disso, quando o caractere "=" for encontrado, o programa deve exibir o valor acumulado até aquele ponto. No final do processamento, o resultado final da soma deve ser impresso.

Funcionamento
O somador on/off vai percorrendo o texto e guarda todas as palavras que encontra numa lista. Caso consiga formar a palavra "off" com os caracteres que encontra, este converte a lista de palavras numa string e soma os conjuntos de dígitos lá presentes. O comportamento da soma não acontece se encontrar a palavra "on". Para o bom funcionamento deste algoritmo, recorre-se a uma variável booleana para sabermos qual palavra procuramos formar. Caso o somador encontre o caractere "=", este apresenta a soma até aí realizada. 

Instrução de utilização
   $ python3 main.py <file_path>