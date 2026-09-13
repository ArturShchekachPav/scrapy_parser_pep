from datetime import datetime

from itemadapter import ItemAdapter

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = {}
        self.results_dir = BASE_DIR / "results"
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        status = adapter["status"]
        self.status_counts[status] = self.status_counts.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = self.results_dir / f"status_summary_{now}.csv"
        total = sum(self.status_counts.values())
        with open(filename, mode="w", encoding="utf-8", newline="") as f:
            f.write("Статус,Количество\n")
            for status, count in self.status_counts.items():
                f.write(f"{status},{count}\n")
            f.write(f"Total,{total}\n")
