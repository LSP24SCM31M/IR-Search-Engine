import scrapy
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re

class MyCrawlerSpider(scrapy.Spider):
    name = 'projectir'
    allowed_domains = ['w3schools.com']
    start_urls = ['https://www.w3schools.com/tutorials/index.php']

    custom_settings = {
        'DEPTH_LIMIT': 2,  
        'CLOSESPIDER_PAGECOUNT': 10,  
    }
    page_count = 0
    documents = []
    document_names = []

    def parse(self, response):
        self.page_count += 1
        filename = self.get_valid_filename(response.url.split("/")[-1]) + '.html'
        self.document_names.append(filename)  
        if self.page_count > self.settings.get('CLOSESPIDER_PAGECOUNT'):
            return
        if response.meta.get('depth', 0) > self.settings.get('DEPTH_LIMIT'):
            return
        try:
            with open(filename, "wb") as f:
                f.write(response.body)
            self.log(f"Saved file {filename}")

            with open(filename, "rb") as f:
                html_content = f.read().decode('utf-8')
                soup = BeautifulSoup(html_content, 'html.parser')
                text = soup.get_text()
                
                clean_text = self.clean_text(text)
                self.documents.append(clean_text)

            for next_page in response.css('a::attr(href)').getall():
                if next_page.startswith("javascript:"):
                    continue  
                yield response.follow(next_page, callback=self.parse)
        except Exception as e:
            self.logger.error(f"Error processing {response.url}: {e}")

    def closed(self, reason):
        self.build_index()

    def build_index(self):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(self.documents)
        cosine_sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

        index = {}
        for idx, (doc_name, doc) in enumerate(zip(self.document_names, self.documents)):
            index[idx] = {
                'document_name': doc_name,
                'document': doc,
                'tfidf_vector': tfidf_matrix[idx],
                'cosine_similarities': cosine_sim_matrix[idx]
            }

        with open('index.pkl', 'wb') as f:
            pickle.dump(index, f)

    def get_valid_filename(self, filename):
        return re.sub(r'[<>:"/\\|?*]', '_', filename)

    def clean_text(self, text):
        clean_text = re.sub(r'<.*?>', '', text)
        clean_text = re.sub(r'\\[ntr]', '', clean_text)
        clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', clean_text)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        clean_text = clean_text.lower()
        return clean_text
