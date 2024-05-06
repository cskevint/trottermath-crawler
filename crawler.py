import requests
import urllib.parse
from bs4 import BeautifulSoup

host = "http://www.trottermath.net"
netloc = "www.trottermath.net"

other_hosts = set()

processed_url_max = 100

def fix_url(current_url, url):
    url = url.strip()
    if url == "index.html":
        url = ""
    url = url.replace("../index.html","")
    url = url.replace("../","")
    if url.startswith("mailto:"):
        raise ValueError("Will not parse mailto: URIs")
    if url.startswith("#"):
        raise ValueError("Will not parse named targets")
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc == "" or parsed.netloc == netloc:
        replaced = urllib.parse.urljoin(current_url, url)
        return replaced
    else:
        other_hosts.add(parsed.netloc)
        raise ValueError("URL is from another host")

urls = {fix_url(host, host)}
processed = set()

# until all pages have been visited
while len(urls) != 0 and processed_url_max > 0:
    # get the page to visit from the list
    current_url = urls.pop()
    processed_url_max -= 1

    # crawling logic
    response = requests.get(current_url)
    if response.status_code != 200:
        print("BROKEN: " + current_url)
    soup = BeautifulSoup(response.content, "html.parser")

    link_elements = soup.select("a[href]")
    for link_element in link_elements:
        url = link_element["href"]
        try:
            fixed_url = fix_url(current_url, url)
            if fixed_url not in processed:
                urls.add(fixed_url)
                processed.add(current_url)
        except ValueError:
            continue

for url in processed:
    print(url)
print(other_hosts)