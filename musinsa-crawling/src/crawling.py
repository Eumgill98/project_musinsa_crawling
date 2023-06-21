#base library
import time
import os
import pandas as pd
import progressbar

#crawling library
import selenium
from selenium import webdriver as wd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import datetime

#custom crawling method
from utils import parse_args, setting_url, config_setting, crwaling_want_page, find_something


if __name__ == "__main__":
    #parser 설정
    args = parse_args()

    #기본 정보 설정
    config = config_setting(args)

    #저장할 정보 list 생성
    linkes = []
    names = []
    images = []
    images_path = []

    start_url = config['URL']
    idx = 1

    bar = progressbar.ProgressBar(maxval=args.crawling_num).start()
    #원하는 데이터 수만큼 크롤링
    while len(linkes) < config['NUM']:
        try:
            start_url = setting_url(idx, args.category)
            #html 정보 Crawling
            soup = crwaling_want_page(start_url)

            #soup에서 원하는 정보 추출
            find_something(bar, soup, args, linkes, names, images, images_path)
            idx +=1

            #linkes, names, images, images_path의 길이 체크 (안맞을 시 오류)
            linkes_len, names_len, images_len, images_path_len = len(linkes), len(names), len(images), len(images_path)
            if linkes_len != names_len and names_len != images_len and images_len != images_path_len:
                raise ValueError('All list len must same!!')
            print(f'중복 체크 - 링크: {linkes_len}, 이름:{ names_len}, 이미지:{images_len}, 이미지경로:{images_path_len}')
        except:
            pass
        time.sleep(1)

    bar.finish()            

    #추출한 정보로 CSV 구성
    df = pd.DataFrame()
    df['link'] = linkes
    df['name'] = names
    df['image_link'] = images
    df['path'] = images_path

    if not os.path.exists(os.path.join(args.save_path, 'csv')):
        os.makedirs(os.path.join(args.save_path, 'csv'))

    #크롤링정보 저장
    df.to_csv(os.path.join(args.save_path, 'csv', f'{args.category}.csv'), index=False)
