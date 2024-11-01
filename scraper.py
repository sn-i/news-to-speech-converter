import requests
from bs4 import BeautifulSoup
import logging


class Scrap:
    def __init__(self, article_url):
        self.article_url = article_url
        self.base_url = self.get_base_url()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

    def get_base_url(self):
        """Extract the base URL to identify the website."""
        base_url = self.article_url.split('/')[2] if '//' in self.article_url else None
        return base_url.replace('www.', '') if base_url else None

    def fetch_article_content(self):
        try:
            if self.base_url == 'mtavari.tv':
                return self.fetch_mtavari_content()
            elif self.base_url == 'tabula.ge':
                return self.fetch_tabula_content()
            elif self.base_url == 'radiotavisupleba.ge':
                return self.fetch_tavisupleba_content()
            elif self.base_url == 'tvpirveli.ge':
                return self.fetch_tv_pirveli()
            elif self.base_url == '1tv.ge':
                return self.fetch_1_tv()
            else:
                logging.warning(f"Website '{self.base_url}' is not supported for scraping.")
                return None
        except requests.RequestException as e:
            logging.error("A connection error occurred: %s", e)
            return None
        except Exception as e:
            logging.error("An error occurred: %s", e)
            return None

    def fetch_mtavari_content(self):
        try:
            content_data = []
            response = requests.get(self.article_url, headers=self.headers)
            if response.status_code != 200:
                print("Failed to retrieve the article from mtavari.tv")
                return None
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find_all('div', class_='EditorContent__EditorContentWrapper-ygblm0-0 dzgBwY')
            for contents in content:
                paragraphs = contents.find_all('p')
                for paragraph in paragraphs:
                    content_data.append(paragraph.get_text(strip=True))
            full_content = " ".join(content_data)
            return full_content
        except requests.RequestException as e:
            print("An error occurred", e)
            return None


    def fetch_tabula_content(self):
        try:
            content_data = []
            response = requests.get(self.article_url, headers=self.headers)
            if response.status_code != 200:
                print("Failed to retrieve the article from tabula.ge")
                return None
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find_all('div', class_= 'ArticleContent_contentTextWrapper__n-T_q content-text')
            for contents in content:
                paragraphs = contents.find_all('p')
                for paragraph in paragraphs:
                    content_data.append(paragraph.get_text(strip=True))
            full_content = " ".join(content_data)
            return full_content
        except requests.RequestException as e:
            print("An error occurred", e)
            return None

    def fetch_tavisupleba_content(self):
        try:
            content_data = []
            response = requests.get(self.article_url, headers=self.headers)
            if response.status_code != 200:
                print("Failed to retrieve the article from radiotavisupleba.ge")
                return None
            soup = BeautifulSoup(response.text, 'html.parser')
            content1 = soup.find_all('div', class_= 'intro intro--bold')
            for contents1 in content1:
                paragraphs = contents1.find_all('p')
                for paragraph in paragraphs:
                    content_data.append(paragraph.get_text(strip=True))
            content = soup.find_all('div', class_='content-floated-wrap fb-quotable')
            for contents in content:
                paragraphs = contents.find_all('p')
                for paragraph in paragraphs:
                    content_data.append(paragraph.get_text(strip=True))
            full_content = " ".join(content_data)
            return full_content
        except requests.RequestException as e:
            print("An error occurred", e)
            return None
    def fetch_tv_pirveli(self):
        try:
            content_data = []
            response = requests.get(self.article_url, headers=self.headers)
            if response.status_code != 200:
                print("Failed to retrieve the article from tvpirveli.ge")
                return None
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find_all('div', class_='page__usercontent')
            for contents in content:
                paragraphs = contents.find_all('p')
                for paragraph in paragraphs:
                    content_data.append(paragraph.get_text(strip=True))
            full_content = " ".join(content_data)
            return full_content
        except requests.RequestException as e:
            print("An error occurred", e)
            return None


    def fetch_1_tv(self):
        try:
            content_data = []
            response = requests.get(self.article_url, headers=self.headers)
            if response.status_code != 200:
                print("Failed to retrieve the article from tvpirveli.ge")
                return None
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find_all('div', class_='article-intro m-t-20 post-slider-article')
            for contents in content:
                paragraphs = contents.find_all('p')
                for paragraph in paragraphs:
                    content_data.append(paragraph.get_text(strip=True))
            full_content = " ".join(content_data)
            return full_content
        except requests.RequestException as e:
            print("An error occurred", e)
            return None


# url = input("Enter website url: ")
# scraper = Scrap(url)
# print(scraper.fetch_article_content())
# # print(scraper.get_base_url())
