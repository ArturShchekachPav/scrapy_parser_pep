from pathlib import Path

BOT_NAME = "pep_parse"
RESULTS_DIR = 'results'
SPIDER_MODULES = [f'{BOT_NAME}.spiders']
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
ROBOTSTXT_OBEY = True
BASE_DIR = Path(__file__).resolve().parent.parent

FEED_EXPORTERS = {
    "csv": "pep_parse.exporters.PepCsvItemExporter",
}

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        "format": "csv",
        "overwrite": True,
        "fields": ["number", "name", "status"],
    },
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
