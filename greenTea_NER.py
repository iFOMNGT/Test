# -*- coding=utf-8 -*-

import traceback
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from ltp import LTP
import os

#本文件的目的，测试LTP对百度百科获取到的绿茶部分信息的实体识别情况

def myLTPTest(input_model_path):
    try:
        #检查传入的模型路径是否存在
        if not os.path.exists(input_model_path):
            raise Exception(f'模型路径{input_model_path}不存在！')
        
        #首先需要获取绿茶的网页信息
        url = 'https://baike.baidu.com/item/绿茶'
        ua = UserAgent().edge
        
        headers = {
            'User-Agent': ua,
            'Referer': 'https://baike.baidu.com/',                                                        # 设置Referer（表明自己是从哪个页面链接过来的） 
            #'cookie': XXX                                                                                # 若需要登录，则需要添加cookie
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print('网页请求成功！')
            
            html_bs = BeautifulSoup(response.text, 'html.parser')
            target_div = html_bs.find('div', attrs={'class': 'lemmaSummary_XiayJ J-summary'})
            if target_div == None:
                raise Exception('爬取目标div失败！，未找到指定结构的div')
            
            the_first_text = target_div.get_text()                                              #获取目标段落的文本数据，将数据用于LTP分析
            
            myltp = LTP(input_model_path)                                                       #初始化LTP对象
            tasks = ["cws", "pos", "ner", "srl", "dep", "sdp", "sdpg"]                          #创建任务列表
            output = myltp.pipeline(the_first_text, tasks=tasks)
            
            for task in tasks:
                print(f'根据{os.path.realpath(input_model_path).split('\\')[-1]}模型的{task}任务，LTP分析结果如下：')
                print(output[task], end='\n\n')
            
            
            
        else:
            raise Exception(f'网页请求失败，返回编码为{response.status_code}')
            
    
    except Exception:
        print(f'错误!捕捉到异常:{Exception}')
        
        
def main():
    myLTPTest("E:\LTP_models\Base")
    
if __name__ =='__main__':
    main()