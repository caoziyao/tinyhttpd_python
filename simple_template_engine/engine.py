#  The main HTML for the whole page.

PAGE_HTML = """
<p>Welcome, {name}!</p>
<p>Products:</p>
<ul>
{products}
</ul>
"""

# The HTML for each product displayed.
PRODUCT_HTML = "<li>{prodname}: {price}</li>\n"

def format_price(price):
    return str(price)

def make_page(username, products):
    product_html = ""
    print(products)
    for prodname, price in products.items():
        product_html += PRODUCT_HTML.format(
            prodname = prodname, price = format_price(price))
    html = PAGE_HTML.format(name=username, products=product_html)

    return html

d =  {'apple': 3000}
html = make_page('gua', d )



print(html)