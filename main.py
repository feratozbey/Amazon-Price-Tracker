import requests
import bs4
import smtplib
import lxml
import os


headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
response = requests.get(
    'https://www.amazon.com/RK-ROYAL-KLUDGE-Mechanical-Ultra-Compact/dp/B089GN2KBT/ref=sr_1_2_sspa?keywords'
    '=gaming+keyboard&pd_rd_r=ff9780ab-ce03-4428-a875-e0995d6763eb&pd_rd_w=IajFQ&pd_rd_wg=IjZRj&pf_rd_p'
    '=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=MK89H7Y7R7NKKZC0ZRY3&qid=1662641078&sr=8-2-spons&psc=1', headers=headers)

html = response.text
soup = bs4.BeautifulSoup(html, 'lxml')
price_with = soup.find('span', class_='a-offscreen')
price_with_span = price_with.text
price = float(price_with_span.replace('$', ''))

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=os.environ['USER'], password=os.environ['PASSWORD'])
    connection.sendmail(from_addr=os.environ['USER'], to_addrs='example@gmail.com', msg=f'Price of that '
                                                                                              f'keyboard from amazon '
                                                                                              f'is {price}')
