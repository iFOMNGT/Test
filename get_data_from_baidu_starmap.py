from DrissionPage import ChromiumPage, ChromiumOptions
import re
import os

class get_data:
    #初始化浏览器，设置浏览器在电脑上的路径，需根据自身实际情况修改path
    def __init__(self, path=None):
        if path is None:    
            path = "C:\\Program Files (x86)\\Microsoft\\Edge\Application\\msedge.exe"                   #根据自身浏览器位置修改路径，可使用chrome内核的浏览器

        co = ChromiumOptions()
        co = ChromiumOptions.set_browser_path(co, path)
        
        self.my_edge = ChromiumPage(co)
        
    def get_greenTea_starmap(self, url=None):
        #定位到绿茶的星图
        if url is None:
            url = 'https://baike.baidu.com/starmap/view?nodeId=753cd009fea02f26a0c031e0&lemmaTitle=%E7%BB%BF%E8%8C%B6&lemmaId=13497&starMapFrom=lemma_starMap&fromModule=lemma_starMap'
            
        self.my_edge.get(url)
        
        #得到绿茶的主要品种名称列表
        names = self.get_data_from('绿茶的主要品种')
        
        #保存绿茶名称数据
        self.save_data('绿茶', '绿茶主要品种', names)
        self.my_edge.wait(1, 3)
        
        #得到各地特色的绿茶的名称列表
        names = self.get_data_from('各地特色绿茶')
        
        #保存绿茶名称数据
        self.save_data('绿茶', '各地特色绿茶', names)
        self.my_edge.wait(1, 3)

    
    def get_blackTea_starmap(self, url=None):
        if url is None:
            url = 'https://baike.baidu.com/starmap/view?nodeId=07a8754d09c8e39367449603&lemmaTitle=%E7%BA%A2%E8%8C%B6&lemmaId=185424&starMapFrom=lemma_starMap&fromModule=lemma_starMap'
        self.my_edge.get(url)
        
        #得到红茶的主要品种名称列表
        names = self.get_data_from('红茶的主要品种')
        
        #保存红茶名称数据
        self.save_data('红茶', '红茶主要品种', names)
        self.my_edge.wait(1, 3)
        
        #得到各地特色的红茶的名称列表
        names = self.get_data_from('各地特色红茶')
        
        #保存红茶名称数据
        self.save_data('红茶', '各地特色红茶', names)
        self.my_edge.wait(1, 3)
        
    def get_oolongTea_starmap(self, url=None):
        if url is None:
            url = 'https://baike.baidu.com/starmap/view?nodeId=222bebc5d9305924b0bd5e1b&lemmaTitle=%E4%B9%8C%E9%BE%99%E8%8C%B6&lemmaId=1072&starMapFrom=lemma_starMap&fromModule=lemma_starMap'
        self.my_edge.get(url)
        names = self.get_data_from('中国著名乌龙茶')
        self.save_data('乌龙茶', '中国著名乌龙茶', names)
        self.my_edge.wait(1, 3)
        
    
    def get_yellowTea_starmap(self, url=None):
        #黄茶没有星图，没办法爬取
        pass
            
    def get_whiteTea_starmap(self, url=None):
        if url is None:
            url = 'https://baike.baidu.com/starmap/view?nodeId=aaf4a9d8b366047f83861512&lemmaTitle=%E7%99%BD%E8%8C%B6&lemmaId=522348&starMapFrom=lemma_starMap&fromModule=lemma_starMap'
        
        self.my_edge.get(url)
        names = self.get_data_from('各地特色白茶')
        self.save_data('白茶', '各地特色白茶', names)
        self.my_edge.wait(1, 3)
        
        
    def get_darkTea_starmap(self, url=None):
        if url is None:
            url = 'https://baike.baidu.com/starmap/view?nodeId=f97c8e265f36aa02f5c2c2ef&lemmaTitle=%E9%BB%91%E8%8C%B6&lemmaId=522584&starMapFrom=lemma_starMap&fromModule=lemma_starMap'
        
        self.my_edge.get(url)
        names = self.get_data_from('黑茶的主要品种')
        self.save_data('黑茶', '黑茶主要品种', names)
        self.my_edge.wait(1, 3)
            
    def get_scentedTea_starmap(self, url=None):
        if url is None:
            url = 'https://baike.baidu.com/starmap/view?nodeId=5c986f702da336feacc8f0e6&lemmaTitle=%E8%8A%B1%E8%8C%B6&lemmaId=481&starMapFrom=lemma_starMap&fromModule=lemma_starMap'
        
        self.my_edge.get(url)
        names = self.get_data_from('各地特色花茶')
        self.save_data('花茶', '各地特色花茶', names)
        self.my_edge.wait(1, 3)
            
            
    def get_pressedTea_starmap(self, url=None):
        #紧压茶没有星图，也要考虑通过网页进行爬取数据
        pass
            
            
    def get_extractedTea_starmap(self, url=None):
        #萃取茶没有星图，同样额外考虑爬取
        pass
            
    def get_medicinal_and_health_care_tea_starmap(self, url=None):
        #药用保健茶无星图，分类需另外看
        pass
            
    def Tea_based_Beverages(self, url=None):
        #含茶饮料在百科中同样没有星图，需要额外查找资料
        pass
    
    
    def get_all_tea_names(self):
        self.get_greenTea_starmap()
        self.get_blackTea_starmap()
        
        self.get_oolongTea_starmap()
        self.get_whiteTea_starmap()
        self.get_darkTea_starmap()
        self.get_scentedTea_starmap()
    
    
    #传入指定的分类茶类名字，将数据保存
    def save_data(self, kind_of_tea, titleName, names):
        path = os.path.join(os.path.split(__file__)[0], f'百度星图\\{kind_of_tea}星图')
        if not os.path.exists(path):
            os.mkdir(path)
            
        with open(os.path.join(path, f'{titleName}.txt'), 'w', encoding='utf-8') as f:
            for name in names:
                f.write(name + '\n')
    
    
    #获取星图界面的数据
    def get_data_from(self, titleName):
        self.my_edge.ele(f'text={titleName}').click()
        print(f'正在获取{titleName}数据')
        
        #获取当前页面共有多少条信息
        length = int(self.my_edge.ele('.sc-cCsOjp cdhAzH').text.split('个')[0][1:])
        
        print(f'共计有{length}条数据，正在获取数据...')
        
        #定位到绿茶品种的容器位置
        target = self.my_edge.ele('@@id=scroll-ref@@class=sc-csvncw iAUKwY')
        
        #根据星图显示的词条数量，获取所有词条的名称
        names = []
        while len(names) != length:
            target.scroll.to_bottom()                                           #当获取到的词条数量与星图显示的词条数量不一致时，则需对目标容器进行滚动，滚动到底部时再进行一次判断
            names = self.my_edge.eles('.sc-GVOUr sc-dwLEzm elxMLl llcknL')
            print(f'获得{len(names)}条数据!')
        
        
        return [name.text for name in names]
    
    
    
    #退出浏览器窗口
    def quit(self):
        self.my_edge.quit()
        

def main():
    #从百度星图上抓取所有茶类的品种名称
    gt = get_data()
    gt.get_all_tea_names()
    gt.quit()
    print('爬取完成！')
    
    
if __name__ == '__main__':
    main()
