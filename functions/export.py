import os
import re
import csv
from dotenv import load_dotenv, find_dotenv
from functions.sitemap import get_sitemap, get_sitemap_urls

load_dotenv(find_dotenv())

domain_a = os.environ.get('DOMAIN_A')
domain_b = os.environ.get('DOMAIN_B')

def handle_domain(domain: str):
  sitemap_content = get_sitemap(f"https://{domain}/sitemap.xml")

  urls = get_sitemap_urls(sitemap_content)

  return urls

def prepare_output(urls_a: list[str], urls_b: list[str]):
  arr_a = urls_a
  arr_b = urls_b

  slug_regex = re.compile(r'https://[^/]+/(.*)')

  slugs_a = [slug_regex.search(url).group(1) for url in urls_a]
  slugs_b = [slug_regex.search(url).group(1) for url in urls_b]

  with open('./output/comparison.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = [domain_a, domain_b]
    writer.writerow(field)

    for idx, item_a in enumerate(arr_a):
      try:
        slug_b_idx = slugs_b.index(slugs_a[idx])

        writer.writerow([item_a, arr_b[slug_b_idx]])
        arr_b[slug_b_idx] = ''
      except:
        writer.writerow([item_a, ''])

    for item_b in arr_b:
      if item_b != '':
        writer.writerow(['', item_b])