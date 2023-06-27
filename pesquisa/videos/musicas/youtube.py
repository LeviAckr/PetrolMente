from youtube_search import YoutubeSearch
from googlesearch import search
import webbrowser
import sys

def pesquisar_youtube(termo):
    try:
        resultados = YoutubeSearch(termo, max_results=1).to_dict()
        if resultados:
            video = resultados[0]
            titulo = video['title']
            canal = video['channel']
            duracao = video['duration']
            url = f"https://www.youtube.com/watch?v={video['id']}"
            print(f"Resultado da pesquisa: {titulo}")
            print(f"Canal: {canal}")
            print(f"Duração: {duracao}")
            print(f"URL: {url}")
            abrir_video(url)
        else:
            print("Nenhum resultado encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro na pesquisa: {str(e)}")

def abrir_video(url):
    escolha = input("Deseja abrir o url (digite 1 para abrir ou 0 para fechar)")
    if escolha == '1':
         webbrowser.open(url)
    elif escolha == '0':
         sys.exit("Sistema abatido --🔫")
    else:
        print("Voçe inseriu um parametro invalido")
termo_pesquisa = input("Digite o que deseja pesquisar no youtube: ")
pesquisar_youtube(termo_pesquisa)