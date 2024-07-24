# -*- coding=utf-8 -*-

import traceback
import requests
from bs4 import BeautifulSoup
import os
from fake_useragent import UserAgent
from tqdm import tqdm

#本文件代码的目的是获取绿茶这个根节点的所有子节点（仅限于茶叶品种），同时根据能否在百科获取子节点信息与否分成两类

def get_tea_from_greenTea():
    try:
        url = 'https://baike.baidu.com/item/绿茶'
        ua = UserAgent().edge                                                                                 # 使用fake_useragent库，随机生成User-Agent     
        #useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
        
        headers = {
            'User-Agent': ua,
            'Referer': 'https://baike.baidu.com/',                                                        # 设置Referer（表明自己是从哪个页面链接过来的） 
            #'cookie': XXX                                                                                # 若需要登录，则需要添加cookie
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            file_path_dir = os.path.split(__file__)[0]                                                      # 获取当前文件所在目录
            tea_save_path = os.path.join(file_path_dir, 'GreenTeaKinds')

            if os.path.exists(tea_save_path):
                print(f'绿茶品种的信息将保存在路径：\n{tea_save_path}', end='\n\n')
            else:
                os.mkdir(tea_save_path)
                print(f'已创建路径，绿茶品种的信息将保存在路径：\n{tea_save_path}', end='\n\n')
                
                
            soup = BeautifulSoup(response.text, 'html.parser')
            target_div = soup.find('div', {'class':"para_zkl_P content_NyFnp MARK_MODULE", 'data-tag': "paragraph", 'data-uuid':"god6f0wxq8", 'data-idx':"3-1"})
            able_to_jump_tea = target_div.find_all('a', {'class':'innerLink_OVf16'})                         # 找到可以跳转的品种
            all_span = target_div.find_all('span', {'class':'text_MIW8T'})                                  # 找到无法进行跳转的品种的名称
            unable_to_jump_tea = []
            for span in all_span:
                if not span.find_all(True):
                    unable_to_jump_tea.append(span)
            
            
            with open(os.path.join(tea_save_path, 'able_jump_greenTea.txt'), 'w', encoding='utf-8') as ab:
                for tea in tqdm(able_to_jump_tea, desc='正在保存可以跳转信息的绿茶品种'):
                    if tea.get_text() != None:
                        ab.write(tea.get_text()+'\n')                                                                   #将可以进行跳转的品种名称保存文件
                    
            
            uab_list = ""
            for tea in unable_to_jump_tea:
                uab_list += tea.get_text()
            uab_list = list(set(uab_list.replace('。', '').replace(' ','').split('；')))                                # 将无法进行跳转的品种名称进行去重，同时移除分割时可能产生的空项
            uab_list = [x for x in uab_list if x is not None and x != ""]


            with open(os.path.join(tea_save_path, 'unable_jump_greenTea.txt'), 'w', encoding='utf-8') as uab:
                for tea in tqdm(uab_list, desc='正在保存无法跳转信息的绿茶品种'):                                               # 将无法跳转的品种名称保存文件  
                    if tea != None:
                        uab.write(tea+'\n') 
    
        else:
            print(f'请求失败，状态码：{response.status_code}')
    
    except Exception:
        traceback.print_exc()
        

def main():
    get_tea_from_greenTea()


if __name__ == '__main__':
    main()
    
