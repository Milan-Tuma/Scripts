def get_sitemap(url: str):
    import requests

    sitemap = requests.get(url)
    return sitemap.content.decode("utf-8")


def get_sitemap_urls(content: str):
    import re

    loc_regex = re.compile(r"<loc>(.*?)</loc>")

    matches: list[str] = loc_regex.findall(content)

    urls_from_xml = []

    for match in matches:
        if match.find("sitemap.xml") != -1:
            additional_sitemap = get_sitemap(match)

            print(f"Found additional sitemaps at: {match}")

            additional_urls = get_sitemap_urls(additional_sitemap)
            urls_from_xml.extend(additional_urls)
        else:
            urls_from_xml.append(match)

    return urls_from_xml
