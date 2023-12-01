#refactor
#generator object using yeild
#error-handling
import httpx
from selectolax.parser import HTMLParser
import time

def get_html(url, **kwargs):
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    if kwargs.get("page"):
        resp = httpx.get(
        url + str(kwargs.get("page")), headers=headers, follow_redirects=True
    )
    else:
        resp = httpx.get(url, headers=headers, follow_redirects=True)
    try:
        resp.raise_for_status()
    except httpx.HTTPStatusError as exc:
        print(
            f"Error response {exc.response.status_code} while requesting {exc.request.url!r}. Page Limit Reached."
        )
        return False
    html = HTMLParser(resp.text)
    return html

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None
    
#yeild generator object
def parse_page(html):
    products = html.css("li.VcGDfKKy_dvNbxUqm29K")

    for product in products:
        item = {
            
            "name": extract_text(product, ".Xpx0MUGhB7jSm5UvK2EY"),
            "price": extract_text(product, "span[data-ui=sale-price]"),
            "savings": extract_text(product, "div[data-ui=savings-percent-variant2]")
        }
        yield item

def main():
    baseurl = "https://www.rei.com/c/camping-and-hiking/f/scd-deals?page="
    for x in range(1, 7):
        print(f"Scraping item values for page: {x}")
        html = get_html(baseurl, page=x)
        if html is False:
            break
        data = parse_page(html)
        for item in data:
            print(item)
        time.sleep(0.5)

if __name__=="__main__":
    main()
