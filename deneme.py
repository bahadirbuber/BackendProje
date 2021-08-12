def deneme(url):
    import requests
    from bs4 import BeautifulSoup

    URL = url
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="listing-page-cart")
    title_elements = results.find_all("div", class_="wt-mb-xs-2")
    title = ""
    for title_element in title_elements:
        title = title_element.find("h1", class_="wt-text-body-03 wt-line-height-tight wt-break-word wt-mb-xs-1")
        if title != "":
            title = title.text.strip()
            break
        
    print(title)
    results = soup.find(id="listing-right-column")
    images = results.find_all("li", class_="wt-position-absolute wt-width-full wt-height-full wt-position-top wt-position-left carousel-pane")
    image = ""
    for image_element in images:
        image = image_element.find("img", class_="wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded")
        if image != "":
            image = image.get("src")
            break
    print(image)
    results = soup.find(id="listing-page-cart")
    prices = results.find_all("p", class_="wt-text-title-03 wt-mr-xs-2")
    for price in prices: 
        price = (price.text.strip()[1:])
    print(price)
    return title,image,price