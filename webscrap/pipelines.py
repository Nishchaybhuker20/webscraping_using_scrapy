from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        return item