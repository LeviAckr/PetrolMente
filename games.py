import webbrowser
import sys
from googlesearch import search

def pesquisar_jogos(genero):
    termo_pesquisa = f"jogos de {genero}"
    num_resultados = 10

    try:
        resultados = list(search(termo_pesquisa, num_results=num_resultados, lang='pt'))
        exibir_resultados(resultados)
        selecionar_site(resultados)
    except Exception as e:
        print(f"Ocorreu um erro na pesquisa: {str(e)}")

def exibir_resultados(resultados):
    if resultados:
        print("Resultados da pesquisa:")
        for i, resultado in enumerate(resultados, start=1):
            print(f"{i}. {resultado}")
    else:
        print("Nenhum resultado encontrado.")

def selecionar_site(resultados):
    opcao = input("Digite o número do site que deseja abrir (0 para fechar ou 9 para reiniciar): ")
    if opcao == '0':
        sys.exit("Programa encerrado.")
    elif opcao == '9':
        reiniciar_sistema()
    elif opcao.isdigit() and int(opcao) <= len(resultados):
        site_selecionado = resultados[int(opcao) - 1]
        webbrowser.open(site_selecionado)
    else:
        print("Opção inválida.")
        selecionar_site(resultados)

def reiniciar_sistema():
    # Coloque aqui qualquer lógica necessária para reiniciar o sistema
    print("Sistema reiniciado.")
    genero_pesquisa = input("Digite o gênero de jogo que deseja pesquisar: ")
    pesquisar_jogos(genero_pesquisa)

genero_pesquisa = input("Digite o gênero de jogo que deseja pesquisar: ")
pesquisar_jogos(genero_pesquisa)
