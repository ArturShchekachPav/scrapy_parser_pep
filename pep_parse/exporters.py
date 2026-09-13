from scrapy.exporters import CsvItemExporter


class PepCsvItemExporter(CsvItemExporter):
    """Feed-экспортёр для pep."""

    FIELD_HEADERS = {
        "number": "Номер",
        "name": "Название",
        "status": "Статус",
    }

    def _write_headers_and_set_fields_to_export(self, item):
        if not self.include_headers_line:
            return
        headers = [
            self.FIELD_HEADERS.get(field, field)
            for field in self.fields_to_export
        ]
        row = list(self._build_row(headers))
        self.csv_writer.writerow(row)
