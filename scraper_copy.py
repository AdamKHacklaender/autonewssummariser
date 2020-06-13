#!/usr/local/bin/python3

# Imports
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.html import HtmlParser
from sumy.summarizers.text_rank import TextRankSummarizer
import smtplib
import urllib.request
from bs4 import BeautifulSoup
from datetime import date
import schedule
import time
import requests
from urllib.request import urlopen

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

# Timed function to execute the .py every day at a certain time
def job(t):

today = date.today()
today_date = str(today)



    # Url from which it scrapes top three articles
url = "https://www.theguardian.com/uk/business"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, features='html.parser')
all_links = soup.find_all('hr')

# TOP ARTICLE 1

if len(all_links) > 100:

    business_1 = all_links[141]
    for url in business_1:
        check_url = url.get('href')
        print(check_url)


# TOP ARTICLE 2

if len(all_links) > 100:

    international_2 = all_links[142]
    for url in international_2:
        check_url2 = url.get('href')
        print(url.get('href'))



# TOP ARTICLE 3

if len(all_links) > 100:

    international_3 = all_links[143]
    for url in international_3:
        check_url3 = url.get('href')
        print(url.get('href'))
        check_url3 = str(check_url3)


url1 = check_url
url2 = check_url2
url3 = check_url3

# SCRAPE HEADLINE 1
page = requests.get(check_url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
html = urlopen(check_url)

bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all('h1')
title = str(titles)

title_new1 = title.replace('[<h1 class="content__headline" itemprop="headline">', " ")
title_new1_1 = (title_new1.replace('</h1>]', " "))
title_new1_2 = (title_new1_1.replace('[<h1 class="is-hidden" itemprop="headline">', " "))
title_new1_3 = (title_new1_2.replace(
    '</h1>, <h1 class="content__headline content__headline--immersive content__headline--immersive--with-main-media content__headline--immersive-article">',
    " "))
title_new1_4 = (title_new1_3.replace('[<h1 class="content__headline js-score" itemprop="headline">', " "))
title_new1_5 = (title_new1_4.replace('[<h1 class="css-rtdfvn"></h1>][<h1 class="css-rtdfvn">', " "))


# SCRAPE HEADLINE 2
page = requests.get(check_url2, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
html = urlopen(check_url2)

bs = BeautifulSoup(html, "html.parser")
titles_2 = bs.find_all('h1')
title_2 = str(titles_2)

title_new2 = (title_2.replace('[<h1 class="content__headline" itemprop="headline">', " "))
title_new2_1 = (title_new2.replace('</h1>]', " "))
title_new2_2 = (title_new2_1.replace('[<h1 class="is-hidden" itemprop="headline">', " "))
title_new2_3 = (title_new2_2.replace('</h1>, <h1 class="content__headline content__headline--immersive content__headline--immersive--with-main-media content__headline--immersive-article">'," "))
title_new2_4 = (title_new2_3.replace('[<h1 class="content__headline js-score" itemprop="headline">', " "))
title_new2_5 = (title_new2_4.replace('[<h1 class="css-rtdfvn"></h1>][<h1 class="css-rtdfvn">', " "))

# SCRAPE HEADLINE 3
page = requests.get(check_url3, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
html = urlopen(check_url3)

bs = BeautifulSoup(html, "html.parser")
titles3 = bs.find_all('h1')
title3 = str(titles3)

title_new_3 = (title3.replace('[<h1 class="content__headline" itemprop="headline">', " "))
title_new3_1 = (title_new_3.replace('</h1>]', " "))
title_new3_2 = (title_new3_1.replace('[<h1 class="is-hidden" itemprop="headline">', " "))
title_new3_3 = (title_new3_2.replace('</h1>, <h1 class="content__headline content__headline--immersive content__headline--immersive--with-main-media content__headline--immersive-article">',
    " "))
title_new3_4 = (title_new3_3.replace('[<h1 class="content__headline js-score" itemprop="headline">', " "))
title_new4 = (title_new3_4.replace('[<h1 class="css-rtdfvn"></h1>][<h1 class="css-rtdfvn">', " "))

page = urllib.request.urlopen(url3)
soup = BeautifulSoup(page, features='html.parser')
all_links = soup.find_all('a')

# Language and number of sentences
language = "english"
url1 = check_url
url2 = check_url2
sentence_count = 2

# TextRank summarizer article 1
parser = HtmlParser.from_url(url1, Tokenizer(language))
summarizer = TextRankSummarizer()
summary = ' '

for sentence in summarizer(parser.document, sentence_count):
    summary += str(sentence)

# TextRank summarizer article 2
parser = HtmlParser.from_url(url2, Tokenizer(language))
summarizer2 = TextRankSummarizer()
summary2 = ' '

for sentence in summarizer2(parser.document, sentence_count):
    summary2 += str(sentence)

# TextRank summarizer article 3
parser = HtmlParser.from_url(url3, Tokenizer(language))
summarizer3 = TextRankSummarizer()
summary3 = ' '

for sentence in summarizer3(parser.document, sentence_count):
    summary3 += str(sentence)


# Send Mail Function - sends summary(ies) to an email address
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Credentials
    sender = 'XXXXX'
    recipient = 'YYYY'
    google_app_password = 'PASS'

    server.login(sender, google_app_password)

    subject = 'World News ' + today_date

    t1 = "1)" + title_new1_5
    t2 = "2)" + title_new2_5
    t3 = "3)" + title_new4

    email_msg = f"subject: {subject}\n\n{t1}\n\n{summary}\n\n{t2}\n{summary2}\n\n{t3}\n{summary3}"

    # Send Email + encoding for articles in different languages
    server.sendmail(
        sender,
        recipient,
        email_msg.encode('utf-8').strip()
    )

    server.quit()


send_mail()

print('Email Sent!!')
def job(t):

schedule.every(10).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute


