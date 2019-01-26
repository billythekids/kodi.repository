#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import urllib
import re


class Parser:
    def get(self, response):
        category = []
        soup = BeautifulSoup(response, "html.parser")
        for item in soup.select('ul.navbar-nav > li'):
            menu = item.select_one('a')
            if menu.get('target') is None:
                category.append({
                    'title': menu.text.encode("utf-8"),
                    'link': "",
                    'subcategory': self.getsubmenu(item)
                })

        return category

    def getsubmenu(self, xpath):
        category = []
        for item in xpath.select('ul > li'):
            link = urllib.quote(item.select_one('a').get('href').encode('utf-8'))
            parts = re.search("phimmedia\.tv\/(.*)\.html", link)
            category.append({
                'title': item.select_one('a').text.encode("utf-8"),
                'link': parts.group(1)
            })

        return category

