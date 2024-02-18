import os
from dotenv import load_dotenv, find_dotenv
from functions.export import handle_domain, prepare_output

load_dotenv(find_dotenv())

domain_a = os.environ.get("DOMAIN_A")
domain_b = os.environ.get("DOMAIN_B")


def main():
    try:
        urls_a = handle_domain(domain_a)
        urls_b = handle_domain(domain_b)

        prepare_output(urls_a, urls_b)

        print("Done")
        exit(0)
    except:
        exit(1)


main()
