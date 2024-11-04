import json
import re
import requests
import xml.etree.ElementTree as ET
import openai
import os

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

# Function to call OpenAI API
def analyze_abstracts(abstract1, abstract2):
    openai.api_key = os.getenv('OPENAI_API_KEY')  # Read the API key from environment variables
    client = openai.OpenAI()
    prompt = (
        "You are a concise researcher trying to unlock new science. "
        "Read the two abstracts below and state how they could be interconnected in terms of the field of study:\n\n"
        f"Abstract 1: {abstract1}\n\n"
        f"Abstract 2: {abstract2}\n\n"
        "Concise statement on interconnection:"
    )
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content.strip()

def handler(event, context):
    body = json.loads(event['body'])
    urls = body.get('urls', [])
    if len(urls) != 2:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Please provide exactly two arXiv URLs.'})
        }

    valid_urls = [is_valid_arxiv_url(url) for url in urls]
    if not all(valid for valid, _ in valid_urls):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid arXiv URLs provided.'})
        }

    arxiv_ids = [arxiv_id for _, arxiv_id in valid_urls]
    abstracts = [fetch_abstract(arxiv_id) for arxiv_id in arxiv_ids]

    if None in abstracts:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to fetch one or both abstracts.'})
        }

    analysis = analyze_abstracts(abstracts[0], abstracts[1])

    return {
        'statusCode': 200,
        'body': json.dumps({'analysis': analysis})
    }