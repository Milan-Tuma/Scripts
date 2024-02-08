# Sitemap comparison script

## Description

Python script used for comparison of sitemap.xml between two sites. The script creates a GET request to selected domain's sitemap and extract all URLs in `<loc>` tags. If sitemap contains reference to other sitemaps, the recursive call populates them as well.

Output of the script can be found in `./output/comparison.csv`. Column A contains all links with domain A, column B lists adequate URL based on the slug of the URL. If none are found, the field remains empty. All URLs from domain B are listed below in column B.

## Install & Run the Project

- Installation - `py -m pip install`
- Running the script - `py main.py`

### Setting up local

- generate environment variables `cp .env.sample .env`
- fill in domains of compared sites (use only domain e.g. domain.com)
