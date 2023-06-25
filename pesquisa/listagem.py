from googlesearch import search
import webbrowser

def fazer_pesquisa():
    termo_pesquisa = input("Digite o que deseja buscar: ")
    num_resultados = 5

    try:
        resultados = list(search(termo_pesquisa, num_results=num_resultados))
        exibir_resultados(resultados)
        selecionar_site(resultados)
    except Exception as e:
        print(f"Ocorreu um erro na pesquisa: {str(e)}")

def exibir_resultados(resultados):
    if len(resultados) > 0:
        print(f"Os {len(resultados)} primeiros resultados da pesquisa são:")
        for i, resultado in enumerate(resultados, start=1):
            print(f"Resultado {i}: {resultado}")
    else:
        print("Nenhum resultado encontrado.")

def selecionar_site(resultados):
    if len(resultados) > 0:
        while True:
            escolha = input("Digite o número do site que deseja abrir (ou '0' para sair ou '9' para reiniciar): ")
            if escolha == '0':
                break
            elif escolha == '9':
                fazer_pesquisa()
            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(resultados):
                    webbrowser.open(resultados[indice])
                else:
                    print("Escolha inválida. Tente novamente.")
            except ValueError:
                print("Escolha inválida. Tente novamente.")
    else:
        print("Nenhum resultado encontrado.")

fazer_pesquisa()
