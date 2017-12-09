# coding=utf-8

from get_data_from_baike import get_page_from_baike
from get_data_from_ccf import get_name_from_ccf_tc
from settings import mongodb_ip,mongodb_port

import pymongo

if __name__ == '__main__':
    # get_name_from_ccf_tc()
    conn = pymongo.MongoClient(mongodb_ip, mongodb_port)
    db = conn.admin
    collection = db.baike

    get_name_from_ccf_tc()

    # with open(name_file_dir,'r') as f:
    #     for name in f:
    #         get_page_from_baike(collection,name.strip())