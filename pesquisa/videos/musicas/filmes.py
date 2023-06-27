import requests
from bs4 import BeautifulSoup
import sys

def buscar_filmes(tema):
    url = f"https://www.google.com/search?q=filmes+{tema}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        resultados = soup.find_all("div", class_="r")

        if resultados:
            print(f"Resultados da pesquisa para '{tema}':")
            for i, resultado in enumerate(resultados, start=1):
                titulo = resultado.find("h3").text
                link = resultado.find("a")["href"]
                print(f"Filme {i}: {titulo}")
                print(f"Link: {link}")
                print()

                reset(tema)
        else:
            print("Nenhum resultado encontrado.")
            reset(tema)
    else:
        print("Ocorreu um erro na pesquisa.")
        reset(tema)


def reset(tema):
    escolha = input("Digite 0 para fechar o sistema ou 9 para reiniciar")
    if escolha == "0":
        sys.exit()
    elif escolha == "9":
        buscar_filmes(tema)
    else:
        print("Você digitou um parametro invalido no sistema")
tema_pesquisa = input("Digite o tema que deseja buscar filmes: ")



buscar_filmes(tema_pesquisa)
