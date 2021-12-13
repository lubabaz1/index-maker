import json
import os
from whoosh import index
from whoosh.fields import Schema, TEXT, ID, STORED
from whoosh.analysis import StemmingAnalyzer

index_dir = 'index'
raw_events = []

with open('data/data_v3.json', 'r') as file:
    file_content = file.readline()
    raw_events = json.loads(file_content)
    
# INDEXING
if not os.path.exists(index_dir):
    os.mkdir(index_dir)

schema = Schema(
    doc_no=ID(stored=True),
    doc_content=TEXT(analyzer=StemmingAnalyzer(), stored=True),
    title=STORED(),
    description=STORED(),
    location=STORED(),
    date=STORED(),
    url=STORED(),
    is_recurring=STORED(),
    source=STORED()
)

indexing = index.create_in(index_dir, schema)
writer = indexing.writer()

for event in raw_events:
    writer.add_document(
        doc_no=f'doc{event["id"]}', 
        doc_content=f'${event["title"]} ${event["description"]}',
        title=event['title'],
        description=event['description'],
        location=event['location'],
        date=event['date'],
        url=event['link'],
        is_recurring=event['recurring'] != '',
        source=event['source']
    )
writer.commit()
