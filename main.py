import requests
from bs4 import BeautifulSoup
import datetime, json, os

# Function to create a directory if it doesn't exist
def create_directory(directory):
    parent_path = 'scraped_data'
    if not os.path.exists(f"{parent_path}/"+ directory):
        os.makedirs(f"{parent_path}/"+ directory)
        
        
def get_box_data(URL):
    base_url = "https://wallpaperaccess.com"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url=URL, headers=headers)

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    container = soup.select_one("#maincontent")
    
    products = container.find_all('div', attrs={'data-fullimg': True})
    
    urls = []
    
    for product in products:
        url = product.select_one('img', attrs="data-src").get('data-src')
        urls.append(base_url +url.replace("../", ""))
        
    with open(f"scraped_data/{DIRECTORY_NAME}/{DIRECTORY_NAME}.json", "w", encoding="utf-8") as file:
        json.dump(urls, file, indent=4, ensure_ascii=False)
    print(f"ALL URLS ARE DOWNLOADED AT \'scraped_data/{DIRECTORY_NAME}/{DIRECTORY_NAME}.json\' PATH! ")


def scrap_images(DIRECTORY_NAME):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    with open(f'scraped_data/{DIRECTORY_NAME}/{DIRECTORY_NAME}.json', 'r',encoding="utf-8") as file:
        data = json.load(file)
        for url in data:
            filename = url.split('/')[-1]
            response = requests.get(url, headers=headers)
            html = response.text
            def save_img(filename):
                print(filename)
                r = requests.get(url, allow_redirects=True)
                open((f'scraped_data/{DIRECTORY_NAME}/')+filename,"wb").write(r.content)
            save_img(filename)
    print(f"ALL IMAGES ARE DOWNLOADED AT \'scraped_data/{DIRECTORY_NAME}/\' PATH!")
            
            
while True:
    START_COMMAND = str(input("PLEASE CHOOSE ANYTHING: \n1 - SCRAPING URLS. \n2 - SCRAPING IMAGES IN THE JSON FILE. \n0 - EXIT.\n>> "))
    if START_COMMAND == "1":
        URL = str(input("URL?: "))
        DIRECTORY_NAME = URL.split('/')[-1]
        create_directory(DIRECTORY_NAME)
        get_box_data(URL)
        
    elif START_COMMAND == "2":
        DIRECTORY_NAME = str(input("DIRECTORY NAME?: "))
        scrap_images(DIRECTORY_NAME)
    elif START_COMMAND == "0":
        print("GOODBYE SEE YOU AGAIN!")
        break
    else:
        print("Your choice is incorrect!")






        


