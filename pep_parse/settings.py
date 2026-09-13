from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True
BASE_DIR = Path(__file__).resolve().parent.parent

FEED_EXPORTERS = {
    'csv': 'pep_parse.exporters.PepCsvItemExporter',
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'overwrite': True,
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
