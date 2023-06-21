#base library
import time
import os
from collections import defaultdict
from argparse import ArgumentParser

#crawling library
from selenium import webdriver as wd
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests

def parse_args():
    """_summary_

    Returns:
        args(parser) : base parser setting 
    """
    parser = ArgumentParser()

    parser.add_argument('--save_path', type=str, default='../save/', help='Crawling data save path')
    parser.add_argument('--category', type=str, default='Top', help='Goods category')
    parser.add_argument('--crawling_num', type=int, default=5000, help='Num of Crawling data')

    args = parser.parse_args()
    return args

def setting_url(idx, category):
    """_summary_

    Args:
        idx (int): setting page index
        category (str): goods category

    Returns:
        BASE_URL (str): changed page url
    """

    url_dict = {
        'Top': '001',
        'Outer': '002',
        'Pants': '003',
        'Onepiece': '004',
        'Skirt': '005'
    }

    BASE_URL = f'https://www.musinsa.com/categories/item/{url_dict[category]}?d_cat_cd=001&brand=&list_kind=small&sort=pop_category&sub_sort=&page={str(idx)}&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=/'

    return BASE_URL

def config_setting(args):
    """_summary_

    Args:
        args (parser): base parser setting

    Returns:
        config (defaultdict): config info
    """
    config = defaultdict()

    config['URL'] = setting_url(1, args.category)
    config['NUM'] = args.crawling_num

    return config

    
def crwaling_want_page(url):
    """_summary_

    Args:
        url (str): url that want to scrapy

    Returns:
        soup (BeautifulSoup) : url page html
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    return soup

def find_something(bar, soup, args, linkes, names, images, images_path):
    """_summary_

    Args:
        bar (progressbar): progressbar 
        soup (BeautifulSoup) : url page html
        args (parser): base parser setting 
        linkes (list): goods linkes info
        names (list): goods names info
        images (list): goods images info
        images_path (list): goods images save path info
    """
    #a 태그에 img-block class를 불러와서 list로 저장
    sorce = soup.find_all('a', attrs={'name':'goods_link'})

    #html에서 각 정보 빼내기
    for t in sorce:
        #제품 링크 추출
        if t['href'] in linkes:
            continue
        linkes.append(t['href'])
        

        good_key = t['href'].split('/')[5]
        img_path  = os.path.join(args.save_path, 'img', args.category)

        if not os.path.exists(img_path):
            os.makedirs(img_path)

        #이미지와 제품정도 추출
        temp_url = 'https:'+t['href']
        responses = requests.get(temp_url, headers={"User-Agent": "Mozilla/5.0"})
        time.sleep(1)

        #세부 상품 page로 이동
        other_soup = BeautifulSoup(responses.text, 'lxml')

        info = other_soup.find_all('div', attrs={'class':'product-img'})

        for i in info:
            for k in i:
                try:
                    names.append(k['alt'])
                    images.append(k['src'])

                    #img download
                    urlretrieve('https:' + k['src'], os.path.join(img_path, good_key+'.png'))
                    images_path.append(os.path.join(img_path, good_key+'.png')) 

                    #progressbar update
                    bar.update(len(images_path))
                except:
                    pass

        
                    
        

