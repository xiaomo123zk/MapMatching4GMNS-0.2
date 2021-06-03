# @author       Kai (Frank) Zhang (zhangk2019@seu.edu.cn)
# @time         2021/5/20 9:40
# @desc         [script description]


#!/usr/bin/python
# coding:utf-8

import requests
import io
import pandas as pd
import csv
import os
import threading
import shutil


def _download_url(url, filename, loc_dir):
    try:
        import requests
    except ImportError:
        print('please print requests to preceed downloading!!')

    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(loc_dir+filename, 'wb') as f:
            f.write(r.content)
    except requests.HTTPError:
        print('file not existing: '+url)
    except requests.ConnectionError:
        raise Exception(
            'check your connectcion!!! Then, if the input data exists, copy the data from local system')
        if(os.path.exists("./testdata")):
            filePath = os.path.join('./testdata/')
            currentPath = os.path.join('./')
            shutil.copy(filePath+'node.csv', currentPath)
            shutil.copy(filePath+'link.csv', currentPath)
            shutil.copy(filePath+'trace.csv', currentPath)
    except Exception as e:
        raise e


def first_way():
    #              raw.githubusercontent.com/username/repo-name/branch-name/path
    url = 'https://raw.githubusercontent.com/xiaomo123zk/MapMatching4GMNS-0.2.14/master/MapMatching4GMNS/'

    data_sets = [
        "testdata"
    ]

    files = [
        "node.csv",
        "link.csv",
        "trace.csv"
    ]

    print('downloading starts')

    # data folder under cdw
    loc_data_dir = 'data'
    if not os.path.isdir(loc_data_dir):
        os.mkdir(loc_data_dir)

    for ds in data_sets:
        web_dir = url + ds + '/'
        loc_sub_dir = os.path.join(loc_data_dir, ds) + '/'

        if not os.path.isdir(loc_sub_dir):
            os.mkdir(loc_sub_dir)

        # multi-threading
        threads = []
        for x in files:
            t = threading.Thread(
                target=_download_url,
                args=(web_dir+x, x, loc_sub_dir)
            )
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    print('downloading completes')

    print('check '+os.path.join(os.getcwd(), loc_data_dir) +
          ' for downloaded data sets')

    # then, copy the input data to current path
    if(os.path.exists("./data/testdata/")):
        filePath = os.path.join("./data/testdata/")
        currentPath = os.path.join(os.getcwd())
        shutil.copy(filePath+'/node.csv', currentPath)
        shutil.copy(filePath+'/link.csv', currentPath)
        shutil.copy(filePath+'/trace.csv', currentPath)


def second_way():
    node_url = 'https://raw.githubusercontent.com/asu-trans-ai-lab/MapMatching4GMNS/blob/master/release/node.csv'
    s = requests.get(node_url).content
    pd_url = pd.read_csv(io.StringIO(s.decode('utf-8')))
    pd_url.head()
    pd_url.to_csv("node.csv", index=True, encoding='utf-8')

    link_url = 'https://raw.githubusercontent.com/asu-trans-ai-lab/MapMatching4GMNS/blob/master/release/link.csv'
    s = requests.get(link_url).content
    pd_url = pd.read_csv(io.StringIO(s.decode('utf-8')))
    pd_url.head()
    pd_url.to_csv("link.csv", index=True, encoding='utf-8')

    trace_url = 'https://raw.githubusercontent.com/asu-trans-ai-lab/MapMatching4GMNS/master/release/trace.csv'
    s = requests.get(trace_url).content
    pd_url = pd.read_csv(io.StringIO(s.decode('utf-8')))
    pd_url.head()
    pd_url.to_csv("trace.csv", index=True, encoding='utf-8')


if __name__ == "__main__":

    # 1, download the sample data set from GitHub,
    # note: if the user does not download data from the Web successfully,
    #  please manually copy the data to the current path from "https://github.com/xiaomo123zk/MapMatching4GMNS-0.2.14/tree/main/MapMatching4GMNS/"

    first_way()

    # second_way()
