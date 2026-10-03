import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time

def search(q):
    query = urllib.parse.quote(q)
    url = f'http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=3'
    try:
        response = urllib.request.urlopen(url)
        xml_data = response.read()
        root = ET.fromstring(xml_data)
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = entry.find('{http://www.w3.org/2005/Atom}title').text.replace('\n', ' ')
            id_url = entry.find('{http://www.w3.org/2005/Atom}id').text
            print(f"Title: {title}\nURL: {id_url}")
    except Exception as e:
        print(e)
    time.sleep(1)

search('all:"inference-time compute scaling"')
search('all:"System 2" AND all:"LLM"')
search('all:"Process Reward Models"')
search('all:"OpenAI o1"')
