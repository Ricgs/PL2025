import sys
import re

def parser(text):
    compositores = set()
    periodos = {}
    obras_por_periodo = {}

    text = re.sub(r'\n\s+', ' ', text)
    linhas = text.split("\n")

    for linha in linhas:
        campos = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', linha)
        print(campos)
        if len(campos) > 1:
            compositores.add(campos[4])
            periodo = campos[3]
            if periodo in periodos:
                periodos[periodo] += 1
            else:
                periodos[periodo] = 1

            if periodo not in obras_por_periodo:
                obras_por_periodo[periodo] = []
            obras_por_periodo[periodo].append(campos[0])

    for periodo in obras_por_periodo:
        obras_por_periodo[periodo].sort()

    return sorted(compositores), periodos, obras_por_periodo


def main(path):
    with open(path, "r", encoding="utf-8") as file:
        next(file)
        text = file.read()

    compositores, periodos, obras_por_periodo = parser(text)

    print("Lista ordenada alfabeticamente dos compositores musicais:")
    for compositor in compositores:
        print(compositor)

    print("\nDistribuição das obras por período:")
    for periodo, count in periodos.items():
        print(f"{periodo}: {count} obras")

    print("\nDicionário de períodos com listas alfabéticas dos títulos das obras:")
    for periodo, titulos in obras_por_periodo.items():
        print(f"{periodo}: {titulos}")

if __name__ == "__main__":
    dataset_path = sys.argv[1]
    main(dataset_path)
