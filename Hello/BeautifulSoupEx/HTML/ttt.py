from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p') # soup.p
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

first_paragraph_id = soup.p['id'] # id가 존재하지 않으면 KeyError
first_paragraph_id2 = soup.p.get('id') # id가 존재하지 않으면 None

all_paragraphs = soup.find_all('p') # soup('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

important_paragraphs = soup('p', {'class': 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class',[])]

# <span> 요소 안에 포함된 모든 <div> 요소를 찾아보자.
spans_inside_divs = [span
                     for div in soup('div') # 모든 <div>
                     for span in div('span')] # 포함된 <span>을