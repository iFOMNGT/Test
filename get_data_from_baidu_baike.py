# -*- coding=utf-8 -*-

from DrissionPage import SessionPage
import os

# 首先明确，需要爬取的类别为，黄茶、紧压茶、萃取茶、药用保健茶、含茶饮料。
class get_data:
    def __init__(self):
        self.my_edge = SessionPage()

    def get_yellowTea(self, url=None):
        if url is None:
            url = 'https://baike.baidu.com/item/黄茶'
        self.my_edge.get(url)
        
        print('爬取黄茶分类···')
        target = self.my_edge.ele('@@class=para_mjfg6 content_v5HyT MARK_MODULE@@data-idx=3-1')
        target = target.text.replace('等。', '').split('：')[1].split('、')
        print('爬取到的黄茶分类为：\n', target)
        self.save_path('黄茶', target)

    
    def get_pressedTea(self, url=None):
        if  url is None:
            url = 'https://baike.baidu.com/item/紧压茶'
        self.my_edge.get(url)
        
        print('爬取紧压茶分类···')
        target = self.my_edge.eles('.text_v1llE bold_uJJZ5')
        target = [temp.text for temp in target]
        print('爬取到的紧压茶分类为：\n', target)
        self.save_path('紧压茶', target)
        
    def get_extractedTea(self, url=None):
        if url is None:
            url = 'https://baike.baidu.com/item/萃取茶'
        self.my_edge.get(url)
        
        print('爬取萃取茶分类···')
        target = self.my_edge.eles('tag=h3')
        target = [temp.text for temp in target]
        print('爬取到的萃取茶分类为：\n', target)
        self.save_path('萃取茶', target)
        
    def get_fruitTea(self, url=None):
        # if url is None:
        #     url = 'https://baike.baidu.com/item/果味茶'
        # self.my_edge.get(url)
        #说实话这几个分类的茶种类少，相关内容不多，要根据爬虫爬下来内容感觉不如人为筛选信息
        target = '荔枝红茶、柠檬红茶、猕猴桃茶、鲜桔汁茶、椰子茶、山楂茶、冬瓜茶、红枣花茶、苹果绿茶、梨茶、橘茶、葡萄红茶、罗汉果茶'.split('、')
        self.save_path('果味茶', target)
    
    def get_medicinal_and_health_care_tea(self):
        target = '减肥茶、杜仲茶、菊花茶'.split('、')
        self.save_path('药用保健茶', target)
        
        
        
    def get_all(self):
        self.get_extractedTea()
        self.get_fruitTea()
        self.get_medicinal_and_health_care_tea()
        self.get_pressedTea()
        self.get_yellowTea()
        
    def save_path(self, kind_of_tea, names):
        path = os.path.join(os.path.split(__file__)[0], f'百度百科\\{kind_of_tea}.txt')
        if not os.path.exists(os.path.split(path)[0]):
            os.mkdir(os.path.split(path)[0])
        
        with open(path, 'w', encoding='utf-8') as f:
            for name in names:
                f.write(name + '\n')
        print('保存完成！')
        
        
def main():
    gd = get_data()
    gd.get_all()

if __name__ == '__main__':
    main()