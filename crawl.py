from lxml import etree
import sys
import os
import re
import random
import time
from selenium.webdriver.common.proxy import ProxyType
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

youtube_site = 'https://www.youtube.com'
query = ['lecture','video']

with open('user_agent.txt', 'r') as f:
    text = f.read()
    user_agent_list = text.split('\n')

def start_browser():
    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format('User-Agent')] = random.choice(user_agent_list)
    browser = webdriver.PhantomJS()
    # proxy = webdriver.Proxy()
    # proxy.proxy_type = ProxyType.MANUAL
    # proxy.http_proxy = '127.0.0.1:56923'
    # proxy.add_to_capabilities( webdriver.DesiredCapabilities.PHANTOMJS)
    browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
    browser.implicitly_wait(120)
    browser.set_page_load_timeout(120)
    return browser

def main(query):
    file_links = open('video_links_%s.txt'%query, "a+")
    file_links.seek(0)
    links = [item for item in file_links.read().split('\n') if item != '']
    links_append_ind = len(links)

    file_pages = open('visited_page_%s.txt'%query, "a+")
    file_pages.seek(0)
    visited_page = [item for item in file_pages.read().split('\n') if item != '']

    page_url = 'https://www.youtube.com/results?search_query=' + query
    browser = start_browser()

    while True:
        print('\nvisiting page :    %s \n'%page_url)
        try:
            browser.get( page_url)
        except TimeoutException as e:
            continue

        page = browser.page_source
        ss = etree.HTML(page)
        list = ss.xpath("//a[contains(@href,'/watch?v=') and @title]")
        for i in list:
            href = i.xpath('@href')[0]
            href = youtube_site + href
            #print('href',href)
            if href not in links:
                links.append(href)

        if links_append_ind != len(links):
            file_links.write('\n'.join(links[links_append_ind::]) + '\n')
            file_links.flush()
            for l in links[links_append_ind::]:
                print('find video link :',l)
            links_append_ind = len(links)

        visited_page.append(page_url)
        file_pages.write(page_url + '\n')
        file_pages.flush()

        href = ss.xpath('//a[contains(@href,"/results?")]')[-1].xpath('@href')[0]
        page_url = youtube_site + href
        if page_url in visited_page:
            break

        time.sleep(random.randint(3,4))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please give some words as a query')
    else:
        query = '+'.join( sys.argv[1::] )
        print('query is %s\n' % query)
        main(query)
