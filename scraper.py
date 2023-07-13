from bs4 import BeautifulSoup
import regex as re
import os
import wget
from multiprocessing.pool import ThreadPool
import random
from urllib.request import urlopen, Request
import ssl 
import certifi

class Scraper():
    
    def __init__(self, asin : str):
        self.asin = asin
        self.soup_fr = ''
        self.soup_pl = ''
        self.soup_de = ''
        self.headers_list = [
                        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
                        "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
                        "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
                        "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
                        ] 
        
    def make_soup(self, url):
        headers = {"User-Agent": random.choice(self.headers_list),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'dnt': '1',
            'upgrade-insecure-requests': '1'}
        
        req = Request(url, headers = headers)
        r = urlopen(req, context=ssl.create_default_context(cafile=certifi.where()))
        soup = BeautifulSoup(r, 'html.parser')
        
        return soup
    
    
    def get_pl_soup(self):
        if not self.soup_pl:
            url = "https://www.amazon.pl/-/dp/{}".format(self.asin)
            self.soup_pl = self.make_soup(url)
            
        return self.soup_pl

    def get_de_soup(self):
        if not self.soup_de:
            url = "https://www.amazon.de/-/pl/dp/{}".format(self.asin)
            self.soup_de = self.make_soup(url)
            
        return self.soup_de

    def get_fr_soup(self):
        if not self.soup_fr:
            url = "https://www.amazon.fr/-/dp/{}".format(self.asin)
            self.soup_fr = self.make_soup(url)
            
        return self.soup_fr


    def save_images(self):
        
        cwd = os.getcwd()
        parent_dir = f"{cwd}"

        try:
            directory = "images"
            mode = 0o666
            path = os.path.join(parent_dir, directory)
            os.mkdir(path, mode)
        except FileExistsError:
            pass
        
        image_list = re.findall(re.compile('(?<={"hiRes":")(.*?)(?=","thumb")'), str(self.get_de_soup()))

        if not image_list:
            image_list = re.findall(re.compile('(?<={"hiRes":")(.*?)(?=","thumb")'), str(self.get_fr_soup()))

        directory = "images\\{}".format(self.asin)
        mode = 0o666
        path = os.path.join(parent_dir, directory)

        try:
            os.mkdir(path, mode)
        except FileExistsError:
            pass

        for image in image_list:
            image_filename = wget.download(image, out=path)
            
    """ product Description """
    
    def scrap_description(self, soup):
        try:
            description = soup.find("div", id="productDescription")
            return description.text
        except AttributeError:
            pass
        
        try:
            description = soup.find("div", id="aplus")
            des = description.text
            
        except AttributeError:
            return "Brak opisu"
            
        return des
    
    
    def format_description(self, description):
        temp = description.split('\n')
        formated = ''
        end_count = 0

        for i in range(len(temp)):
            if temp[i] == '':
                continue
            
            elif end_count == 0:
                end_count += 1 
                formated += ' '.join(temp[i].strip().split()) + '\n'
                
            elif end_count == 1:
                end_count -= 1 
                formated += ' '.join(temp[i].strip().split())
        
        formated = formated.replace('\n\n', '\n')
        return formated
    
    
    def get_description(self, soup):
        description = self.scrap_description(soup)
        description = self.format_description(description)
        
        return description
    
    """ feature bullets """
    def format_front_table(self, front_table):
        front_table = front_table.replace('\n', '')
        temp = front_table.split('    ')
        temp.pop(0)

        for i in range(len(temp)):
            temp[i] = ' '.join(temp[i].strip().split())
            
            if temp[i] == '':
                temp.pop(i)

        front = '\n'.join(temp)
        return front
    
    
    def scrap_front_table(self, soup):
        try:
            description = soup.find("div", id="feature-bullets")
            return description.text
        except AttributeError:
            return 'Nie udało się pobrać tablicy frontowej, sprawdz id(feature-bullets)'
        
    def get_front_table(self, soup):
        front_table = self.scrap_front_table(soup)
        front_table = self.format_front_table(front_table)
        
        return front_table
        
    """ prod Details """
    def scrap_technical_spec(self, soup):
        try:
            description = soup.find("div", id="prodDetails")
            return description.text
        except AttributeError:
            return "Zobacz dormatowanie strony (a-row a-spacing-top-base)"
        
        
    def format_technical_spec(self, raw_spec):
        raw_spec = raw_spec.replace('\n', '')
        temp = raw_spec.split('    ')
        temp.pop(0)

        alpha_temp = []

        j = 0
        for i in range(len(temp)):
            temp[i] = ' '.join(temp[i].strip().split())
            
            if temp[i] != '':
                if "\u200e" in temp[i] and i != 0:
                    alpha_temp[j - 1] = alpha_temp[j - 1] + ' : ' + temp[i].replace('\u200e', '')
                    
                elif j!= 0 and "ASIN" in alpha_temp[j - 1].upper():
                    break
                
                else:
                    alpha_temp.append(temp[i])
                    j += 1
            
        alpha_temp.pop(0)
        tech_spec = '\n'.join(alpha_temp)
        
        return tech_spec

    def get_technical_spec(self, soup):
        tech = self.scrap_technical_spec(soup)
        tech = self.format_technical_spec(tech)
        
        return tech
    
    
    def merge(self, soup):
        tech = self.get_technical_spec(soup)
        front_table = self.get_front_table(soup)
        description = self.get_description(soup)
        
        merged = front_table + "\n\n" + description + "\n\n" + tech
        return merged
    
    
    def get_every_description(self) -> dict:
        
        pool = ThreadPool()
        soup_de = pool.apply_async(self.get_de_soup, ())
        soup_pl = pool.apply_async(self.get_pl_soup, ())
        soup_fr = pool.apply_async(self.get_fr_soup, ())
        
        self.soup_de = soup_de.get()
        self.soup_pl = soup_pl.get()
        self.soup_fr = soup_fr.get()
        
        full_desc_de = pool.apply_async(self.merge, ( self.soup_de, ))
        full_desc_pl = pool.apply_async(self.merge, ( self.soup_pl, ))
        full_desc_fr = pool.apply_async(self.merge, ( self.soup_fr, ))
        
        full_desc_de = full_desc_de.get()
        full_desc_pl = full_desc_pl.get()
        full_desc_fr = full_desc_fr.get()
                
        pool.close()
        pool.join()
        
        descriptions ={"pl": full_desc_pl, "de" : full_desc_de, "fr" : full_desc_fr}
        
        return descriptions
        
        