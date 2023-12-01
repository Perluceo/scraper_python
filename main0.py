import httpx
from selectolax.parser import HTMLParser

url = "https://www.rei.com/c/camping-and-hiking/f/scd-deals"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

resp = httpx.get(url, headers=headers, follow_redirects=True)
html = HTMLParser(resp.text)
# print(html.css_first("title").text())

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

products = html.css("li.VcGDfKKy_dvNbxUqm29K")
# print(products)

for product in products:
    item = {
        
        "name": extract_text(product, ".Xpx0MUGhB7jSm5UvK2EY"),
        "price": extract_text(product, "span[data-ui=sale-price]")
        # "name":product.css_first(".Xpx0MUGhB7jSm5UvK2EY").text(),
        # "price":product.css_first("span[data-ui=sale-price]").text()
    }
    print(item)
    # print(product.css_first(".Xpx0MUGhB7jSm5UvK2EY").text())




