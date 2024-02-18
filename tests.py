import unittest
from functions.test_sitemap import Sitemaps
from test_data import sitemap_content


class TestSitemaps(unittest.TestCase):
    def test_sitemap(self):
        self.sitemap = Sitemaps(sitemap_content)
        self.assertEqual(
            self.sitemap.test_sitemap(),
            [
                "https://domain.com/url-a/",
                "https://domain.com/url-b/",
                "https://domain.com/url-c/",
            ],
            "Incorrect return from sitemap",
        )


if __name__ == "__main__":
    unittest.main()
