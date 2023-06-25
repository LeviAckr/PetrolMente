import requests
import webbrowser

def buscar_livros(assunto, num_resultados):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": assunto,
        "maxResults": num_resultados
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        dados = response.json()
        itens = dados.get("items", [])

        if itens:
            print(f"Resultados da pesquisa para '{assunto}':")
            for i, item in enumerate(itens, start=1):
                volume_info = item.get("volumeInfo", {})
                titulo = volume_info.get("title", "Desconhecido")
                autor = volume_info.get("authors", ["Desconhecido"])
                print(f"Resultado {i}:")
                print(f"Título: {titulo}")
                print(f"Autor(es): {', '.join(autor)}")
                print()

            selecionar_livro(itens)
        else:
            print("Nenhum resultado encontrado.")
    else:
        print("Ocorreu um erro na pesquisa.")

def selecionar_livro(itens):
    opcao = int(input("Digite o número do livro que deseja pesquisar na internet: (0 para sair ou 9 para reiniciar) "))

    if opcao == 0:
        exit("Programa finalizado.")
    elif opcao == 9:
        main()
    elif opcao >= 1 and opcao <= len(itens):
        item = itens[opcao-1]
        volume_info = item.get("volumeInfo", {})
        titulo = volume_info.get("title", "Desconhecido")
        pesquisa = f"{titulo} book"
        pesquisar_internet(pesquisa)
    else:
        print("Opção inválida.")

def pesquisar_internet(termo):
    url = "https://www.google.com/search"
    params = {
        "q": termo
    }

    pesquisa_url = requests.get(url, params=params).url
    webbrowser.open(pesquisa_url)

def main():
    assunto_pesquisa = input("Digite o assunto que deseja buscar livros: ")
    num_resultados = int(input("Digite o número de resultados desejados: "))

    buscar_livros(assunto_pesquisa, num_resultados)

    while True:
        selecionar_livro()

if __name__ == "__main__":
    main()
