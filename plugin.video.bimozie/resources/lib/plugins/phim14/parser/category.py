#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class Parser:
    def get(self, response):
        category = []
        soup = BeautifulSoup(response, "html.parser")

        for item in soup.select('div.nav_content > ul.menu > li.child'):
            menu = item.select_one('> a')
            category.append({
                'title': menu.text.encode("utf-8"),
                'link': menu.get("href"),
                'subcategory': self.getsubmenu(item)
            })

        return category

    def getsubmenu(self, xpath):
        category = []
        for item in xpath.select('ul.sub-menu > li > a'):
            category.append({
                'title': item.text.encode("utf-8"),
                'link': item.get('href')
            })

        return category

