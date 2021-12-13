import json
import os, os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StemmingAnalyzer

index_dir = 'index'
preprocessed_events = []

with open('data_v3.json', 'r') as file:
    file_content = file.readline()
    json_data = json.loads(file_content)
    
    for event in json_data:
        preprocessed_events.append({
            'id': event['id'],
            'content': event['title'] + event['description']
        })      

# INDEXING
if not os.path.exists(index_dir):
    os.mkdir(index_dir)

schema = Schema(doc_no=ID(stored=True),
            doc_content=TEXT(analyzer=StemmingAnalyzer(), stored=True))

indexing = index.create_in(index_dir, schema)
writer = indexing.writer()

for event in preprocessed_events:
    writer.add_document(doc_no=f'doc{event["id"]}', doc_content=event['content'])
writer.commit()
