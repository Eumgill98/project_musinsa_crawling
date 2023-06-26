#base library
from collections import defaultdict
from argparse import ArgumentParser

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
        'Onepiece': '020',
        'Skirt': '022'
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
    config['CATEGORY'] = args.category
    config['SAVE_PATH'] = args.save_path

    return config


        
                    
        

