import httpx
from selectolax.parser import HTMLParser

def get_html():
    url = "https://www.rei.com/c/camping-and-hiking/f/scd-deals"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
    resp = httpx.get(url, headers=headers, follow_redirects=True)
    html = HTMLParser(resp.text)
    return html

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

def parse_page(html):
    products = html.css("li.VcGDfKKy_dvNbxUqm29K")

    for product in products:
        item = {
            
            "name": extract_text(product, ".Xpx0MUGhB7jSm5UvK2EY"),
            "price": extract_text(product, "span[data-ui=sale-price]"),
            "savings": extract_text(product, "div[data-ui=savings-percent-variant2]")
        }
        print(item)

def main():
    html = get_html()
    parse_page(html)

if __name__=="__main__":
    main()
