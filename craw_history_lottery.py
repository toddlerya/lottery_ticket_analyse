#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: qguo
# date: 20160524

import requests
from bs4 import BeautifulSoup
from collections import OrderedDict, defaultdict

def get_item_day(root_url):
    # 获取每一个根页面的所有开奖记录url
    item_url_dict = OrderedDict()
    super_url = "http://www.17500.cn/ssq/"
    root_content = requests.get(root_url).content
    # print root_content
    soup = BeautifulSoup(root_content,"html.parser")
    items_url = soup.body.div.table.p.find_all('a') #find_all 返回的是一个bs4.element.ResultSet, 列表中的每一项是一个 bs4.element.Tag 类.
    for i in items_url:
        # print  i.text, super_url+i['href'] # i['href']是一个str
        item_url_dict[i.text] = super_url+i['href']
    return item_url_dict

def get_ticket(url):
    # 获取每一期的中奖号码
    ticket_dict = defaultdict(list)
    ticket_html = requests.get(url).content
    tk_soup = BeautifulSoup(ticket_html,"html.parser")
    ticket_nums = tk_soup.body.tbody.find_all('td')
    for i in ticket_nums:
        if i.font:
            ticket_dict[i.font['color']].append(i.font.text)
    return ticket_dict

def craw(root_url_list):
    totl_dict = OrderedDict()
    for root_url in root_url_list:
        item_url_dict = get_item_day(root_url)
        # print len(item_url_dict)
        totl_dict.update(item_url_dict) # merge每一期的开奖记录url到一个总dict中
    with open("history_ticket.log","a+") as f:
        for j, url in enumerate(totl_dict.items()):
            ticket_date = url[0]
            ticket_url = url[1]
            ticket_dict = get_ticket(ticket_url)
            ticket_temp = [n for n in ticket_dict.items()]
            blue = ticket_temp[0]
            red = ticket_temp[1]
            ticket_res = str(blue[0]) + ':' + str(blue[1][0]) + ' - ' + str(red[0]) + ':' + str(map(int, [x for x in red[1]]))[1:-1]
            print j, ticket_res
            f.writelines(ticket_res+'\n')


if __name__ == "__main__":
    root_url_list = \
    ["http://www.17500.cn/ssq/all.php",
     "http://www.17500.cn/ssq/all2003.php",
     "http://www.17500.cn/ssq/all2004.php",
     "http://www.17500.cn/ssq/all2005.php"]
    craw(root_url_list)