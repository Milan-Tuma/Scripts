from functions.sitemap import get_sitemap_urls


class Sitemaps:
    def __init__(self, text: str):
        self.sitemap_content = text

    def test_sitemap(self):
        return get_sitemap_urls(self.sitemap_content)
