from datetime import datetime
from collections import defaultdict
from itemadapter import ItemAdapter
import csv

from pep_parse.settings import BASE_DIR, RESULTS_DIR


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        status = adapter['status']
        self.status_counts[status] += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = self.results_dir / f"status_summary_{now}.csv"
        total = sum(self.status_counts.values())

        rows = [
            ('Статус', 'Количество'),
            *self.status_counts.items(),
            ('Total', total),
        ]

        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
