import json
import re
import requests
import xml.etree.ElementTree as ET

def is_valid_arxiv_url(url):
    pattern = r'^https://arxiv\.org/abs/([\w\.]+)(v\d+)?$'
    match = re.match(pattern, url)
    if match:
        return True, match.group(1)
    return False, None

def fetch_abstract(arxiv_id):
    api_url = f'http://export.arxiv.org/api/query?id_list={arxiv_id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        abstract_elem = root.find('.//atom:entry/atom:summary', ns)
        if abstract_elem is not None:
            return abstract_elem.text.strip()
    return None

def handler(event, context):
    body = json.loads(event['body'])
    urls = body.get('urls', [])
    
    results = []
    for url in urls:
        valid, arxiv_id = is_valid_arxiv_url(url)
        if valid:
            abstract = fetch_abstract(arxiv_id)
            if abstract:
                results.append({'url': url, 'abstract': abstract})
            else:
                results.append({'url': url, 'abstract': 'Failed to fetch abstract'})
        else:
            results.append({'url': url, 'abstract': 'Invalid URL'})
    
    return {
        'statusCode': 200,
        'body': json.dumps(results),
        'headers': {
            'Content-Type': 'application/json'
        }
    }