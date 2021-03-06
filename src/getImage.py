from pymongo import MongoClient
import requests
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from PIL import Image
import urllib
import boto
import boto.s3
import sys
from boto.s3.key import Key
import boto.s3.connection
import os




def main():
    '''Run throught the mongo database to scrape images then add them to s3 bucket'''
    AWS_ACCESS_KEY_ID = str(os.environ.get("AWS_ACCESS_KEY"))
    AWS_SECRET_ACCESS_KEY = str(os.environ.get("AWS_SECRET"))

    conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY)
    nameList = ['fish', 'bacon', 'hotdog', 'beef', 'chicken', 'steak', 'burrito', 'enchilada', 'salmon', 'tacos']
    for name in nameList:
        filepath = '../data/'+ name +'.pickle'
        d = pd.read_pickle("../data/"+name+".pickle")
        df = pd.DataFrame(d)
        bucket = conn.get_bucket('dis-capstone-seefood')

        for key,url in df[['key','image_url']].itertuples(index=False):
            key_name = str(key) +'.jpg'
            response = urllib.request.urlopen(url)
            data = response.read()      # a `bytes` object
            #Directory Under which file should get upload
            k = bucket.new_key(name+'/'+key_name)
            k.set_contents_from_string(data)
        print('Done next step....')





if __name__ == '__main__':
    main()
