from selenium import webdriver
from bs4 import BeautifulSoup
import re

# Definir o caminho para o WebDriver (ChromeDriver no exemplo)
webdriver_path = "caminho/para/o/chromedriver"

# Instanciar o navegador usando o WebDriver
driver = webdriver.Chrome(webdriver_path)

# URL da página de resultados da pesquisa do YouTube para "Marília Mendonça"
url = "https://www.youtube.com/results?search_query=marilia+mendon%C3%A7a"

# Abrir a URL no navegador
driver.get(url)

# Obter o conteúdo da página
html_content = driver.page_source


soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar todas as URLs dos shorts
pattern = r'"url":"/shorts/([^"]+)"'
matches = re.findall(pattern, html_content)
shorts_urls = matches if matches else []

print('URLs dos shorts:')
for url in shorts_urls:
    print(url)

# Fechar o navegador
driver.quit()

# Agora você pode usar o conteúdo da página (html_content) como desejar
#print(html_content.encode('utf-8'))
