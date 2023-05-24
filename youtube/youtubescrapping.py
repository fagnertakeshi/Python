import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=mar%C3%ADlia+mendon%C3%A7a"

# Envia uma requisição GET para a URL
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Extrai o conteúdo HTML da resposta
    html_content = response.text
    print(html_content)

    # Cria um objeto BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Encontra todos os elementos que representam os vídeos na página
    video_elements = soup.find_all("a", {"class": "yt-simple-endpoint style-scope ytd-video-renderer"})

    # Itera sobre os elementos de vídeo e extrai informações relevantes
    for video in video_elements:
        title = video.get("title")
        video_id = video.get("href")
        print("Video:", title)
        print("Video ID:", video_id)
        print()

else:
    print("A requisição falhou com código de status:", response.status_code)
