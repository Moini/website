import csv
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

from parser import parse_events

today = datetime.now()

with open('2020_events_db.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    events = parse_events(reader, today, False)

file_loader = FileSystemLoader('src/templates')
env = Environment(loader=file_loader)
template = env.get_template('index.html')
result = template.render(
    upcoming=events['upcoming'],
    prev=events['prev'], year='2020',
    other_year='2019',
    other_year_link='/'
)
with open('build/events-2020.html', 'a') as f:
    f.write(result)