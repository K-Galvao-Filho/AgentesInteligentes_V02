import os
from googleapiclient.discovery import build

# Obter a chave da API
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")
if not YOUTUBE_API_KEY:
    raise ValueError("A chave da API do YouTube não foi encontrada nas variáveis de ambiente.")

# Inicializar o cliente YouTube
def get_youtube_client(chave_api):
    return build("youtube", "v3", developerKey=chave_api)

youtube_client = get_youtube_client(YOUTUBE_API_KEY)

def pesquisar_videos_youtube(consulta, num_resultados=5):
    """
    Pesquisa vídeos no YouTube e retorna os resultados.

    Args:
        consulta (str): A consulta de pesquisa.
        num_resultados (int, opcional): Número máximo de vídeos. Padrão: 5.

    Returns:
        list: Lista de dicionários contendo título, descrição, URL e canal.
    """
    try:
        requisicao = youtube_client.search().list(
            part="snippet",
            maxResults=num_resultados,
            q=consulta
        )
        resposta = requisicao.execute()
    except Exception as e:
        print(f"Erro ao buscar vídeos no YouTube: {e}")
        return []

    videos = [
        {
            "Título": item["snippet"]["title"],
            "Descrição": item["snippet"]["description"],
            "URL": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            "Canal": item["snippet"]["channelTitle"]
        }
        for item in resposta.get("items", []) if item["id"]["kind"] == "youtube#video"
    ]

    return videos
