# 关于茶叶品种相关的知识图谱构建项目
## 项目构建思路
### 构建茶类的知识图谱，首先需要先收集所有茶类的信息。
收集所有茶的信息，首先需要明确有哪些茶类——收集所有茶的种类名称，以至于能明确知道需要获取哪些茶的信息。  
而茶的种类大致可分为7种，**6大茶**（基本种类）与**再加工茶**，，6大茶分别是[绿茶][绿茶]、[红茶][红茶]、[乌龙茶][乌龙茶]、[白茶][白茶]、[黄茶][黄茶]、[黑茶][黑茶]，而再加工茶可分为[花茶][花茶]、[紧压茶][紧压茶]、[萃取茶][萃取茶]、[果味茶][果味茶]、*药用保健茶*([减肥茶][减肥茶]、[杜仲茶][杜仲茶]、[菊花茶][菊花茶])、*含茶饮料*([茶可乐][茶可乐]、[茶汽水][茶汽水])。（若图片显示不全，[请点击此]）(https://static.chayeji.com/chayeji/images/2023/09/06/ad0e400874544f64a8b49549948a710e~noop_5zxh0vacdpc.jpg)
    ![茶的分类图](https://static.chayeji.com/chayeji/images/2023/09/06/ad0e400874544f64a8b49549948a710e~noop_5zxh0vacdpc.jpg '茶叶集')

[绿茶]: https://baike.baidu.com/item/绿茶 '百度百科'
[红茶]: https://baike.baidu.com/item/红茶 '百度百科'
[乌龙茶]: https://baike.baidu.com/item/乌龙茶 '百度百科'
[白茶]: https://baike.baidu.com/item/白茶 '百度百科'
[黄茶]: https://baike.baidu.com/item/黄茶 '百度百科'
[黑茶]: https://baike.baidu.com/item/黑茶 '百度百科'
[花茶]: https://baike.baidu.com/item/花茶 '百度百科'
[紧压茶]: https://baike.baidu.com/item/紧压茶 '百度百科'
[萃取茶]: https://baike.baidu.com/item/萃取茶 '百度百科'
[果味茶]: https://baike.baidu.com/item/果味茶 '百度百科'
[减肥茶]: https://baike.baidu.com/item/减肥茶 '百度百科'
[杜仲茶]: https://baike.baidu.com/item/杜仲茶 '百度百科'
[菊花茶]: https://baike.baidu.com/item/菊花茶 '百度百科'
[茶可乐]: https://baike.baidu.com/item/茶可乐 '百度百科'
[茶汽水]: https://baike.baidu.com/item/茶汽水 '百度百科'


在百科中搜索6大茶分别可得到其对应的品种，根据**网页跳转**可以得到其品种对应的信息（存在部分茶类无法跳转网页），通过这个途径可以获取茶的种类与对应的信息。





## 知识学习部分
[对于反爬虫的应对技巧，可点击此处查看](https://blog.csdn.net/qq_38230663/article/details/116830990?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172177919516800186555470%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=172177919516800186555470&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-116830990-null-null.142^v100^pc_search_result_base5&utm_term=python%E5%8F%8D%E7%88%AC%E8%99%AB%E6%8A%80%E6%9C%AF%E4%BB%A3%E7%A0%81&spm=1018.2226.3001.4187 'CSDN')

[若爬取的网站需要登录账号，可参考此处做法](https://blog.csdn.net/qq_67344578/article/details/138147246?ops_request_misc=&request_id=&biz_id=102&utm_term=python%E5%8F%8D%E7%88%AC%E8%99%AB%E6%8A%80%E6%9C%AF%E4%BB%A3%E7%A0%81&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-138147246.142^v100^pc_search_result_base5&spm=1018.2226.3001.4187 'CSDN')

[markdown的基本语法介绍教学，可点击此处了解](https://www.bilibili.com/video/BV1eJ4m157kC/?p=10&spm_id_from=333.880.my_history.page.click&vd_source=7e8842e232b2923adc42e99aa17df57d 'bilibili')

[LTP4的基本介绍，可点击此处了解](https://github.com/HIT-SCIR/ltp 'GitHub')

基于复现的项目使用的是pyltp，故同样给出[pyltp](https://pypi.org/project/pyltp/)的说明文档  

[GitHub的入门教程，可点击此处了解](https://blog.csdn.net/black_sneak/article/details/139600633 'CSDN')

[Drissionpage爬虫官网文档点击此处](https://www.drissionpage.cn/ 'Drissionpage')



## 代码构建部分
### 对绿茶的品种进行爬取（测试）
根据观察网页结构可以知道绿茶品种名称部分为``<div class="para_zkl_P content_NyFnp MARK_MODULE" data-tag="paragraph" data-uuid="god6f0wxq8" data-idx="3-1">``这个容器下的内容，故我们爬取这个部分的内容可以得到绿茶的分类品种的名称。  
而这些名称当中有一些是可以点击跳转到相应的信息页面的，有一些则不行，故我们根据这个现象，将能跳转的名称统合一类，不能跳转的统合为另一类。
使用``requests``库获取网页结构，再使用``bs4``即``BeautifulSoup``对这个结构进行解析。  
```python
#首先找到指定div容器
target_div = soup.find('div', {'class':"para_zkl_P content_NyFnp MARK_MODULE", 'data-tag': "paragraph", 'data-uuid':"god6f0wxq8", 'data-idx':"3-1"})

#找到指定容器后，在容器中找符合条件的标签
able_to_jump_tea = target_div.find_all('a', {'class':'innerLink_OVf16'})                         # 找到可以跳转的品种
all_span = target_div.find_all('span', {'class':'text_MIW8T'})                                  # 找到无法进行跳转的品种的名称
unable_to_jump_tea = []
for span in all_span:
    if not span.find_all(True):
        unable_to_jump_tea.append(span)


#针对无法跳转的品种，爬取到的信息包含“；”这个符号，将“；”作为分割符，同时确保列表中不会出现空项
uab_list = ""
for tea in unable_to_jump_tea:
    uab_list += tea.get_text()
uab_list = list(set(uab_list.replace('。', '').replace(' ','').split('；')))                                # 将无法进行跳转的品种名称进行去重，同时移除分割时可能产生的空项
uab_list = [x for x in uab_list if x is not None and x != ""]
```
最终可以获取到两个数据集
```python
#可跳转的绿茶品种部分结果展示
英山云雾茶
西湖龙井
峨眉雪芽
湄潭翠芽
兰馨雀舌
惠明茶
洞庭碧螺春
马边云雾茶
日照绿茶
顾渚紫茶
午子仙毫
黄山毛峰
六安瓜片
信阳毛尖
云雾毛尖
曾侯银剑
平水珠茶
宝洪茶
上饶白眉
径山茶
```

```python
#不可跳转的绿茶品种全部结果展示
狗脑贡茶
韶峰
晒青
剑叶
山岩翠绿
关山云雾
峨眉春语
房县绿茶
大悟绿茶
盘安云峰
华顶云雾
神农绿茶
南山白毛芽
云峰与蟠毫
翠螺
中岳仙茶
```
根据这些可以跳转的绿茶品种名称，再去到相应的百科页面抓取数据；其他品种的茶也是一样的做法。  
**以上仅为一个思路尝试**，**未必**是最终实现项目的思路，在这仅作分享。




### 对绿茶页面的开头段落信息做LTP分析（测试）
这段测试目的是测试LTP4几个模型对绿茶在百度百科的信息的第一段进行分词、词性标注、命名实体识别等功能的效果。LTP4的库请自行运行命令``pip install ltp``下载。而LTP的默认模型为在线模型，需要链接到固定的服务器上，故需要科学上网，为了方便测试，本例使用在线模型，在线模型可通过Happy Funny或在GitHub上下载。通过引用库，并且指定模型路径（不指定则为默认的在线模型），即可使用LTP的功能。
```python
from ltp import LTP
myltp = LTP('模型的路径(注意只需精确到文件夹如：LTP/small)')
```
同样通过``requests``库获取网页结构，再使用``bs4``对这个结构进行解析，获取目标文本。
```python
html_bs = BeautifulSoup(response.text, 'html.parser')
target_div = html_bs.find('div', attrs={'class': 'lemmaSummary_XiayJ J-summary'})

the_first_text = target_div.get_text() 
```

将从网页获得的文本进行输出。  
> 绿茶，山茶科山茶属灌木或小乔木植物，绿茶形态自然、色泽鲜绿，采取茶树的新叶或芽，经杀青、整形、烘干等工艺制作而成，保留了鲜叶的天然物质；茶叶尖而细，表面光滑；开白色花，花朵较小，呈多边形；花期10月-次年2月。绿茶因其干茶呈绿色、冲泡后的茶汤呈碧绿、叶底呈翠绿色而得名。 [9-10]绿茶原产于中国，在中国河南、贵州、浙江等地广泛分布，也分布于日本、泰国、朝鲜、韩国等国。绿茶喜湿润、温暖的环境，不耐阳光、高温、湿气，种植时以肥沃疏松的微酸性 土壤为宜。绿茶的繁殖方法主要有播种繁殖和扦插繁殖，一般采用扦插繁殖。 [11-13]《雷公炮制药性解》中记载绿茶：“绿茶，性微寒，味苦、甘。”绿茶具有收敛、利尿、提神的功效，用于治疗神疲多眠、头痛目昏、烦渴、小便不利、酒毒等病症。绿茶是中国历史上出现最早的茶类，有着悠久的生产历史；唐代时期中国已流行用蒸青法制造绿茶，后传入日本，并被许多国家所采用；明代时期，发明了炒青茶制造绿茶。绿茶香高味长、品质优异，且造型独特，具有较高的艺术欣赏价值。绿茶是中国产量最高的茶类，也是品种最丰富、名茶最多的茶类，经济价值丰富。 [11] [14-16]

当指明模型为Base时，得到的``["cws", "pos", "ner", "srl", "dep"]``任务结果如下
> 根据Base模型的cws任务，LTP分析结果如下：  
> ['绿茶', '，', '山茶科', '山茶', '属', '灌木', '或', '小', '乔木', '植物', '，', '绿茶', '形态', '自然', '、', '色泽', '鲜绿', '，', '采取', '茶树', '的', '新', '叶', '或', '芽', '，', '经', '杀青', '、', '整形', '、', '烘干', '等', '工艺', '制作', '而', '成', '，', '保留', '了', '鲜', '叶', '的', '天然', '物质', '；', '茶叶', '尖', '而', '细', '，', '表面', '光滑', '；', '开', '白色', '花', '，', '花朵', '较', '小', '，', '呈', '多边形', '；', '花期', '10月', '-', '次年', '2月', '。', '绿茶', '因', '其', '干茶', '呈', '绿色', '、', '冲泡', '后', '的', '茶汤', '呈', '碧绿', '、', '叶底', '呈', '翠绿色', '而', '得', '名', '。 ', '[', '9', '-10', ']', '绿茶', '原', '产', '于', '中国', '，', '在', '中国', '河南', '、', '贵州', '、', '浙江', '等', '地', '广泛', '分布', '，', '也', '分布', '于', '日本', '、', '泰国', '、', '朝鲜', '、', '韩国', '等', '国', '。', '绿茶', '喜', '湿润', '、', '温暖', '的', '环境', '，', '不', '耐', '阳光', '、', '高温', '、', '湿气', '，', '种植', '时', '以', '肥沃', '疏松', '的', '微酸性', '土壤', '为宜', '。', '绿茶', '的', '繁殖', '方 法', '主要', '有', '播种', '繁殖', '和', '扦插', '繁殖', '，', '一般', '采用', '扦插', '繁殖', '。 ', '[', '11', '-13', ']', '《', '雷公', '炮制', '药性', '解', '》', '中', '记载', '绿茶', '：', '“', '绿茶', '，', ' 性', '微', '寒', '，', '味', '苦', '、', '甘', '。', '”', '绿茶', '具有', '收敛', '、', '利尿', '、', '提神', '的', '功效', '，', '用于', '治疗', '神疲', '多', '眠', '、', '头痛', '目', '昏', '、', '烦渴', '、', '小 便', '不利', '、', '酒毒', '等', '病症', '。', '绿茶', '是', '中国', '历史', '上', '出现', '最', '早', '的', '茶类', '，', '有着', '悠久', '的', '生产', '历史', '；', '唐代', '时期', '中国', '已', '流行', '用', '蒸青法', '制造', '绿茶', '，', '后', '传入', '日本', '，', '并', '被', '许多', '国家', '所', '采用', '；', '明代', '时期', '，', '发明', '了', '炒青茶', '制造', '绿茶', '。', '绿茶', '香', '高', '味', '长', '、', '品质', '优异', '，', '且', '造型', '独特', '，', '具有', '较', '高', '的', '艺术', '欣赏', '价值', '。', '绿茶', '是', '中国', '产量', '最高', '的', '茶类', '，', '也', '是', '品种', '最', '丰富', '、', '名茶', '最', '多', '的', '茶类', '，', '经济', '价值', '丰富', '。 ', '[', '11', '] ', '[', '14', '-16', ']']

> 根据Base模型的pos任务，LTP分析结果如下：  
> ['n', 'wp', 'n', 'n', 'v', 'n', 'c', 'a', 'n', 'n', 'wp', 'n', 'n', 'a', 'wp', 'n', 'a', 'wp', 'v', 'n', 'u', 'a', 'n', 'c', 'n', 'wp', 'p', 'v', 'wp', 'v', 'wp', 'v', 'u', 'n', 'v', 'c', 'v', 'wp', 'v', 'u', 'a', 'n', 'u', 'b', 'n', 'wp', 'n', 'a', 'c', 'a', 'wp', 'n', 'a', 'wp', 'v', 'n', 'n', 'wp', 'n', 'd', 'a', 'wp', 'v', 'n', 'wp', 'nt', 'nt', 'wp', 'nt', 'nt', 'wp', 'n', 'p', 'r', 'n', 'v', 'n', 'wp', 'v', 'nd', 'u', 'n', 'v', 'z', 'wp', 'n', 'v', 'n', 'c', 'v', 'n', 'wp', 'wp', 'm', 'm', 'wp', 'n', 'd', 'v', 'p', 'ns', 'wp', 'p', 'ns', 'ns', 'wp', 'ns', 'wp', 'ns', 'u', 'n', 'a', 'v', 'wp', 'd', 'v', 'p', 'ns', 'wp', 'ns', 'wp', 'ns', 'wp', 'ns', 'u', 'n', 'wp', 'n', 'v', 'a', 'wp', 'a', 'u', 'n', 'wp', 'd', 'v', 'n', 'wp', 'n', 'wp', 'n', 'wp', 'v', 'n', 'p', 'a', 'a', 'u', 'n', 'n', 'v', 'wp', 'n', 'u', 'v', 'n', 'd', 'v', 'v', 'v', 'c', 'v', 'v', 'wp', 'a', 'v', 'v', 'v', 'wp', 'wp', 'm', 'm', 'wp', 'wp', 'nh', 'v', 'n', 'n', 'wp', 'nd', 'v', 'n', 'wp', 'wp', 'n', 'wp', 'n', 'a', 'a', 'wp', 'n', 'a', 'wp', 'a', 'wp', 'wp', 'n', 'v', 'v', 'wp', 'v', 'wp', 'v', 'u', 'n', 'wp', 'v', 'v', 'a', 'a', 'v', 'wp', 'a', 'n', 'a', 'wp', 'a', 'wp', 'n', 'a', 'wp', 'n', 'u', 'n', 'wp', 'n', 'v', 'ns', 'n', 'nd', 'v', 'd', 'a', 'u', 'n', 'wp', 'v', 'a', 'u', 'v', 'n', 'wp', 'nt', 'n', 'ns', 'd', 'v', 'p', 'n', 'v', 'n', 'wp', 'nd', 'v', 'ns', 'wp', 'c', 'p', 'm', 'n', 'u', 'v', 'wp', 'nt', 'n', 'wp', 'v', 'u', 'n', 'v', 'n', 'wp', 'n', 'n', 'a', 'n', 'a', 'wp', 'n', 'a', 'wp', 'c', 'n', 'a', 'wp', 'v', 'd', 'a', 'u', 'n', 'v', 'n', 'wp', 'n', 'v', 'ns', 'n', 'a', 'u', 'n', 'wp', 'd', 'v', 'n', 'd', 'a', 'wp', 'n', 'd', 'a', 'u', 'n', 'wp', 'n', 'n', 'a', 'wp', 'wp', 'm', 'wp', 'wp', 'm', 'c', 'wp']    

> 根据Base模型的ner任务，LTP分析结果如下：  
> [('Ns', '中国', 100, 100), ('Ns', '中国', 103, 103), ('Ns', '河南', 104, 104), ('Ns', '贵州', 106, 106), ('Ns', '浙江', 108, 108), ('Ns', '日本', 117, 117), ('Ns', '泰国', 119, 119), ('Ns', '朝鲜', 121, 121), ('Ns', '韩国', 123, 123), ('Nh', '雷公', 175, 175), ('Ns', '中国', 228, 228), ('Ns', '中国', 245, 245), ('Ns', '日本', 255, 255), ('Ns', '中国', 296, 296)]

> 根据Base模型的srl任务，LTP分析结果如下：  
>[{'index': 4, 'predicate': '属', 'arguments': [('A0-PSR', '绿茶', 0, 0), ('A0', '山茶科山茶', 2, 3), ('A1', '灌木或小乔木植物', 5, 9)]}, {'index': 13, 'predicate': '自然', 'arguments': [('A0-PSR', '绿茶', 0, 0), ('A0-PSR', '绿茶', 11, 11), ('A0-PSE', '形态', 12, 12)]}, {'index': 16, 'predicate': '鲜绿', 'arguments': [('A0-PSR', '绿茶', 0, 0), ('A0-PSR', '绿茶', 11, 11), ('A0-PSE', '色泽', 15, 15), ('ARGM-LOC', '中国历史上', 228, 230), ('A0-PSR', '绿茶', 273, 273)]}, {'index': 18, 'predicate': '采取', 'arguments': [('A1', '茶树的新叶或芽', 19, 24)]}, {'index': 34, 'predicate': '制作', 'arguments': [('ARGM-MNR', '经杀青、整形、烘干等工艺', 26, 33), ('A0', '绿茶', 127, 127)]}, {'index': 38, 'predicate': '保留', 'arguments': [('A1', '鲜叶的天然物质', 40, 44), ('A0', '绿茶', 127, 127), ('A1', '阳光、高温、湿气', 137, 141), ('A1', '较高的艺术欣赏价值', 287, 292)]}, {'index': 47, 'predicate': '尖', 'arguments': [('A0', '茶叶', 46, 46), ('A0-PSE', '品种', 304, 304), ('ARGM-ADV', '最', 305, 305)]}, {'index': 49, 'predicate': '细', 'arguments': [('A0-PSR', '茶叶', 46, 46), ('A0-PSE', '性', 187, 187), ('A0-PSE', '品种', 304, 304), ('ARGM-ADV', '最', 305, 305), ('A0-PSR', '茶类', 312, 312)]}, {'index': 52, 'predicate': '光滑', 'arguments': [('A0-PSE', '表面', 51, 51), ('A0-PSE', '名茶', 308, 308), ('ARGM-ADV', '最', 309, 309), ('A0-PSR', '茶类', 312, 312)]}, {'index': 54, 'predicate': '开', 'arguments': [('A1', '白色花', 55, 56)]}, {'index': 60, 'predicate': '小', 'arguments': [('A0', '花朵', 58, 58), ('ARGM-ADV', '较', 59, 59)]}, {'index': 62, 'predicate': '呈', 'arguments': [('A0', '花朵', 58, 58), ('A1', '多边形', 63, 63)]}, {'index': 75, 'predicate': '呈', 'arguments': [('A0', '其干茶', 73, 74), ('A1', '绿 色', 76, 76)]}, {'index': 86, 'predicate': '呈', 'arguments': [('A0', '叶底', 85, 85), ('A1', '翠绿色', 87, 87)]}, {'index': 89, 'predicate': '得', 'arguments': [('A1', '绿茶', 71, 71), ('ARGM-PRP', '因其干茶呈绿色', 72, 76), ('A1', '名', 90, 90)]}, {'index': 98, 'predicate': '产', 'arguments': [('A0', '绿茶', 96, 96), ('ARGM-ADV', '原', 97, 97), ('A1', '于中国', 99, 100)]}, {'index': 115, 'predicate': '分布', 'arguments': [('ARGM-ADV', '也', 114, 114)]}, {'index': 128, 'predicate': '喜', 'arguments': [('A1', '茶树的新叶或芽', 19, 24)]}, {'index': 129, 'predicate': '湿润', 'arguments': [('A0', '环境', 133, 133)]}, {'index': 131, 'predicate': '温暖', 'arguments': [('A0', '环境', 133, 133)]}, {'index': 136, 'predicate': '耐', 'arguments': [('A0', '绿茶', 127, 127), ('ARGM-ADV', '不', 135, 135), ('A1', '阳光、高温、湿气', 137, 141)]}, {'index': 146, 'predicate': '肥沃', 'arguments': [('A0', '土壤', 150, 150), ('A0', '茶类', 312, 312)]}, {'index': 147, 'predicate': '疏松', 'arguments': [('A0', '土壤', 150, 150), ('A0', '茶类', 312, 312)]}, {'index': 151, 'predicate': '为宜', 'arguments': [('ARGM-TMP', '种植时', 143, 144), ('A1', '以肥沃疏松的微酸性土壤', 145, 150)]}, {'index': 158, 'predicate': '有', 'arguments': [('A1', '白色花', 55, 56), ('A0', '绿茶的繁殖方法', 153, 156), ('ARGM-ADV', '主要', 157, 157), ('A1', '播种繁殖和扦插繁殖', 159, 163)]}, {'index': 166, 'predicate': '采用', 'arguments': [('ARGM-ADV', '一般', 165, 165), ('A1', '扦插繁殖', 167, 168)]}, {'index': 176, 'predicate': '炮 制', 'arguments': [('A0', '雷公', 175, 175), ('A1', '药性', 177, 177)]}, {'index': 181, 'predicate': '记载', 'arguments': [('A1', '白色花，花朵较小，呈多边形；花期10月-次年2月', 55, 69), ('A1', '因其干茶呈绿色、冲泡 后的茶汤呈碧绿、叶底呈翠绿色而得名', 72, 90), ('A1', '绿茶的繁殖方法主要有播种繁殖和扦插繁殖，一般采用扦插繁殖', 153, 168), ('A2', '《雷公炮制药性解》中', 174, 180), ('A1', '绿茶：“绿茶，性微寒，味苦、甘。”绿茶具有收敛、利尿、提神的功效，用于治疗神疲多眠、头痛目昏、烦渴、小便不利、酒毒等病症', 182, 224)]}, {'index': 189, 'predicate': '寒', 'arguments': [('A0-PSE', '性', 187, 187), ('A0-PSE', '品种', 304, 304), ('ARGM-ADV', '最', 305, 305), ('A0-PSR', '茶类', 312, 312)]}, {'index': 192, 'predicate': '苦', 'arguments': [('A0-PSE', '表面', 51, 51), ('A0-PSE', '味', 191, 191)]}, {'index': 194, 'predicate': '甘', 'arguments': [('A0-PSE', '味', 191, 191)]}, {'index': 198, 'predicate': '具有', 'arguments': [('A1', '收敛、利尿、提神的功效', 199, 205)]}, {'index': 207, 'predicate': '用于', 'arguments': [('ARGM-ADV', '一般', 165, 165)]}, {'index': 208, 'predicate': '治疗', 'arguments': [('A1', '神疲多眠、头痛目昏、烦渴、小便不利、酒毒等病症', 209, 224)]}, {'index': 220, 'predicate': '不利', 'arguments': [('A0', '小便', 219, 219)]}, {'index': 227, 'predicate': '是', 'arguments': [('A0', '绿茶', 226, 226), ('A1', '中国历史上出现最早的茶类', 228, 235), ('A1', '用蒸青法制造绿茶', 248, 251)]}, {'index': 231, 'predicate': '出现', 'arguments': [('ARGM-LOC', '中国历史上', 228, 230)]}, {'index': 233, 'predicate': '早', 'arguments': [('A0-PSR', '绿茶', 11, 11), ('ARGM-LOC', '中国历史上', 228, 230), ('A0-PRD', '出现', 231, 231), ('ARGM-ADV', '最', 232, 232), ('A0-PSR', '茶类', 235, 235), ('A0-PRD', '用蒸青法', 248, 249), ('A0-PSE', '味', 276, 276)]}, {'index': 237, 'predicate': '有着', 'arguments': [('A1', '悠久的生产历史', 238, 241), ('A1', '较高的艺术欣赏价值', 287, 292)]}, {'index': 247, 'predicate': '流行', 'arguments': [('A1', '茶树的新叶或芽', 19, 24), ('ARGM-TMP', '唐代时期', 243, 244), ('A0', '中国', 245, 245), ('ARGM-ADV', '已', 246, 246)]}, {'index': 250, 'predicate': '制造', 'arguments': [('ARGM-LOC', '中国历史上', 228, 230), ('A1', '绿茶', 251, 251)]}, {'index': 254, 'predicate': '传入', 'arguments': [('A0', '绿茶', 127, 127), ('ARGM-TMP', '后', 253, 253), ('A2', '日本', 255, 255)]}, {'index': 262, 'predicate': '采用', 'arguments': [('A0', '许多国家', 259, 260)]}, {'index': 270, 'predicate': '制造', 'arguments': [('A1', '绿茶', 271, 271)]}, {'index': 277, 'predicate': '长', 'arguments': [('A0-PSR', '绿茶', 11, 11), ('A0-PSR', '环境', 133, 133), ('ARGM-LOC', '中国历史上', 228, 230), ('A0-PSR', '茶类', 235, 235), ('A0-PSR', '绿茶', 273, 273), ('A0-PSE', '味', 276, 276), ('A0-PSE', '品质', 279, 279)]}, {'index': 280, 'predicate': '优异', 'arguments': [('A0-PSR', '绿茶', 11, 11), ('A0-PSR', '绿茶', 273, 273), ('A0-PSE', '品质', 279, 279), ('A0-PSR', '茶类', 300, 300)]}, {'index': 284, 'predicate': '独特', 'arguments': [('A0-PSR', '绿茶', 11, 11), ('A0-PSR', '绿茶', 273, 273), ('A0-PSE', '品质', 279, 279), ('A0-PSE', '造型', 283, 283)]}, {'index': 286, 'predicate': '具有', 'arguments': [('A1', '鲜叶的天然物质', 40, 44), ('A1', '较高的艺术欣赏价值', 287, 292)]}, {'index': 288, 'predicate': '高', 'arguments': [('ARGM-ADV', '较', 287, 287)]}, {'index': 303, 'predicate': '是', 'arguments': [('A1', '种植时以肥沃疏松的微酸性土壤', 143, 150), ('A0', '绿茶', 294, 294), ('ARGM-ADV', '也', 302, 302), ('A1', '品种最丰富、名茶最多的茶类', 304, 312)]}, {'index': 306, 'predicate': '丰富', 'arguments': [('A1-PSR', '茶叶', 46, 46), ('A1-PSE', '性', 187, 187), ('A1-PSR', '绿茶', 273, 273), ('A1-PSE', '品种', 304, 304), ('ARGM-ADV', '最', 305, 305), ('A1-PSR', '茶类', 312, 312)]}, {'index': 310, 'predicate': '多', 'arguments': [('A0-PSE', '表面', 51, 51), ('A0-PSR', '土壤', 150, 150), ('A0-PSR', '绿茶', 273, 273), ('A0-PSE', '名茶', 308, 308), ('ARGM-ADV', '最', 309, 309), ('A0-PSR', '茶类', 312, 312)]}, {'index': 316, 'predicate': '丰富', 'arguments': [('ARGM-ADV', '一般', 165, 165), ('A1-PSE', '经济价值', 314, 315)]}]

> 根据Base模型的dep任务，LTP分析结果如下：
{'head': [5, 1, 4, 5, 0, 10, 9, 9, 6, 5, 248, 13, 248, 248, 17, 17, 14, 248, 248, 23, 20, 23, 19, 25, 23, 19, 35, 34, 30, 28, 32, 28, 28, 27, 248, 37, 35, 248, 248, 39, 42, 45, 42, 45, 39, 248, 48, 248, 50, 48, 48, 53, 48, 48, 48, 57, 55, 55, 61, 61, 55, 61, 55, 63, 248, 70, 70, 70, 70, 99, 99, 90, 90, 75, 76, 73, 76, 83, 80, 83, 80, 83, 76, 83, 87, 87, 83, 87, 90, 99, 90, 99, 94, 99, 94, 94, 99, 99, 182, 99, 100, 99, 113, 105, 111, 107, 105, 109, 105, 105, 103, 113, 99, 99, 116, 99, 116, 126, 120, 118, 122, 118, 124, 118, 118, 117, 99, 129, 182, 134, 132, 130, 130, 129, 129, 137, 129, 137, 140, 138, 142, 138, 129, 145, 152, 152, 151, 147, 147, 151, 146, 129, 129, 157, 154, 157, 159, 159, 129, 161, 159, 164, 164, 161, 159, 167, 159, 169, 167, 182, 172, 179, 172, 172, 179, 177, 179, 177, 181, 179, 182, 248, 182, 182, 190, 188, 186, 190, 190, 248, 190, 193, 190, 195, 190, 199, 199, 199, 248, 206, 202, 200, 204, 200, 200, 199, 199, 199, 208, 225, 214, 214, 214, 210, 216, 214, 218, 210, 221, 221, 210, 223, 221, 210, 209, 228, 228, 248, 230, 231, 232, 228, 234, 232, 232, 228, 228, 248, 242, 239, 242, 238, 248, 245, 248, 248, 248, 5, 248, 249, 248, 251, 248, 255, 248, 255, 248, 263, 263, 261, 259, 263, 248, 248, 266, 268, 266, 248, 268, 248, 248, 271, 248, 276, 276, 248, 278, 276, 281, 281, 276, 276, 285, 285, 276, 248, 248, 289, 293, 289, 292, 293, 287, 248, 296, 248, 301, 299, 301, 299, 296, 296, 304, 296, 307, 307, 313, 311, 311, 311, 307, 307, 304, 296, 316, 317, 296, 248, 320, 5, 320, 320, 320, 320, 320], 'label': ['SBV', 'WP', 'ATT', 'SBV', 'HED', 'ATT', 'LAD', 'ATT', 'COO', 'VOB', 'WP', 'ATT', 'SBV', 'COO', 'WP', 'SBV', 'COO', 'WP', 'COO', 'ATT', 'RAD', 'ATT', 'VOB', 'LAD', 'COO', 'WP', 'ADV', 'ATT', 'WP', 'COO', 'WP', 'COO', 'RAD', 'POB', 'COO', 'ADV', 'COO', 'WP', 'COO', 'RAD', 'ATT', 'ATT', 'RAD', 'ATT', 'VOB', 'WP', 'SBV', 'COO', 'LAD', 'COO', 'WP', 'SBV', 'COO', 'WP', 'COO', 'ATT', 'VOB', 'WP', 'SBV', 'ADV', 'COO', 'WP', 'COO', 'VOB', 'WP', 'ATT', 'ATT', 'WP', 'ATT', 'COO', 'WP', 'SBV', 'ADV', 'ATT', 'SBV', 'POB', 'VOB', 'WP', 'ATT', 'ADV', 'RAD', 'SBV', 'COO', 'VOB', 'WP', 'SBV', 'COO', 'VOB', 'ADV', 'COO', 'VOB', 'WP', 'WP', 'ADV', 'ATT', 'WP', 'SBV', 'ADV', 'COO', 'CMP', 'POB', 'WP', 'ADV', 'ATT', 'ATT', 'WP', 'COO', 'WP', 'COO', 'RAD', 'POB', 'ADV', 'COO', 'WP', 'ADV', 'COO', 'CMP', 'ATT', 'WP', 'COO', 'WP', 'COO', 'WP', 'COO', 'RAD', 'POB', 'WP', 'SBV', 'COO', 'ATT', 'WP', 'COO', 'RAD', 'VOB', 'WP', 'ADV', 'COO', 'VOB', 'WP', 'COO', 'WP', 'COO', 'WP', 'ATT', 'ADV', 'ADV', 'ATT', 'COO', 'RAD', 'ATT', 'POB', 'COO', 'WP', 'ATT', 'RAD', 'ATT', 'SBV', 'ADV', 'COO', 'ADV', 'VOB', 'LAD', 'ADV', 'COO', 'WP', 'ADV', 'COO', 'ADV', 'VOB', 'WP', 'WP', 'ATT', 'ATT', 'WP', 'WP', 'SBV', 'ATT', 'FOB', 'ATT', 'WP', 'ADV', 'COO', 'IOB', 'WP', 'WP', 'ATT', 'WP', 'SBV', 'ADV', 'COO', 'WP', 'SBV', 'COO', 'WP', 'COO', 'WP', 'WP', 'SBV', 'COO', 'ATT', 'WP', 'COO', 'WP', 'COO', 'RAD', 'VOB', 'WP', 'COO', 'COO', 'ATT', 'COO', 'COO', 'WP', 'COO', 'SBV', 'COO', 'WP', 'COO', 'WP', 'SBV', 'COO', 'WP', 'SBV', 'RAD', 'VOB', 'WP', 'SBV', 'COO', 'ATT', 'ATT', 'ADV', 'VOB', 'ADV', 'CMP', 'RAD', 'VOB', 'WP', 'COO', 'ATT', 'RAD', 'ATT', 'VOB', 'WP', 'ATT', 'ADV', 'SBV', 'ADV', 'COO', 'VOB', 'VOB', 'VOB', 'VOB', 'WP', 'ADV', 'COO', 'VOB', 'WP', 'ADV', 'ADV', 'ATT', 'POB', 'LAD', 'COO', 'WP', 'ATT', 'ADV', 'WP', 'COO', 'RAD', 'VOB', 'COO', 'VOB', 'WP', 'SBV', 'SBV', 'COO', 'SBV', 'COO', 'WP', 'SBV', 'COO', 'WP', 'ADV', 'SBV', 'COO', 'WP', 'COO', 'ADV', 'ATT', 'RAD', 'ATT', 'ATT', 'VOB', 'WP', 'SBV', 'COO', 'ATT', 'SBV', 'ATT', 'RAD', 'VOB', 'WP', 'ADV', 'COO', 'SBV', 'ADV', 'ATT', 'WP', 'SBV', 'ADV', 'COO', 'RAD', 'VOB', 'WP', 'ATT', 'SBV', 'COO', 'WP', 'WP', 'COO', 'WP', 'WP', 'ATT', 'LAD', 'WP']}

### 根据百度星图的数据进行爬取（测试失败）
尝试爬取 https://baike.baidu.com/starmap/view?nodeId=753cd009fea02f26a0c031e0&lemmaTitle=%E7%BB%BF%E8%8C%B6&lemmaId=13497&starMapFrom=lemma_starMap&fromModule=lemma_starMap
抓取含有js的内容，只用``requests``库无法正确爬取所有信息，即无法爬取所需数据，需考虑别的方法抓取数据 ~~(3小时白干QAQ)~~


### 根据百度星图的数据进行爬取（再次尝试，这次成功）
汲取上次的经验，``requests``无法爬取js动态渲染的内容，故通过学习``Drissionpage``库的知识，在知识学习部分已经将``Drissionpage``的链接放出，故这里不进行详细介绍，总的来说``Drissionpage``可操控浏览器、收发数据包，且语法相较``selenium``更为简单，对新手更加友好。  
**以下只介绍代码过程（以爬取绿茶的星图为例）**。首先通过``pip install Drissionpage``下载``Drissionpage``库，在使用``Drissionpage``时需指定chrome内核浏览器的路径（因为这个库**只支持chrome内核的浏览器**）可以根据下列代码进行指定。
```python
from DrissionPage import ChromiumPage, ChromiumOptions

path = "C:\\Program Files (x86)\\Microsoft\\Edge\Application\\msedge.exe"                   #根据自身浏览器位置修改路径，使用chrome内核的浏览器

co = ChromiumOptions()
co = ChromiumOptions.set_browser_path(co, path)

my_edge = ChromiumPage(co)
```

这个库使用简单的语法即可控制浏览器打开指定url的页面
```python
url = 'https://baike.baidu.com/starmap/view?nodeId=753cd009fea02f26a0c031e0&lemmaTitle=%E7%BB%BF%E8%8C%B6&lemmaId=13497&starMapFrom=lemma_starMap&fromModule=lemma_starMap'
my_edge.get(url)
```


以下是对抓取百度星图茶类名字代码的解释。
定义一个类``class get_data``，本代码的操作统合成一个类，首先可以传入浏览器路径``path``，不传入就会使用下列这个默认的路径，首先基于设置创建一个浏览器窗口``my_edge``。
```python
class get_data:
    #初始化浏览器，设置浏览器在电脑上的路径，需根据自身实际情况修改path
    def __init__(self, path=None):
        if path is None:    
            path = "C:\\Program Files (x86)\\Microsoft\\Edge\Application\\msedge.exe"                   #根据自身浏览器位置修改路径，可使用chrome内核的浏览器

        co = ChromiumOptions()
        co = ChromiumOptions.set_browser_path(co, path)
        
        self.my_edge = ChromiumPage(co)
```

定义函数获取绿茶品种名称数据。首先将星图的路径传入``url``同样未传入则使用默认路径。``self.my_edge.get(url)``可控制窗口打开指定路径的网页。
```python
def get_greenTea_starmap(self, url=None):
        #定位到绿茶的星图
        if url is None:
            url = 'https://baike.baidu.com/starmap/view?nodeId=753cd009fea02f26a0c031e0&lemmaTitle=%E7%BB%BF%E8%8C%B6&lemmaId=13497&starMapFrom=lemma_starMap&fromModule=lemma_starMap'
            
        #得到绿茶的主要品种名称列表
        names = self.get_data_from('绿茶的主要品种')
        
        #保存绿茶名称数据
        self.save_data('绿茶', '绿茶主要品种', names)
        self.my_edge.wait(3)
        
        #得到各地特色的绿茶的名称列表
        names = self.get_data_from('各地特色绿茶')
        
        #保存绿茶名称数据
        self.save_data('绿茶', '各地特色绿茶', names)
        self.my_edge.get(url)
```

对于函数``get_data_from``的解释如下。传入要获取路径的``title``名，控制浏览器点击这个``title``确保我们获取的列表``target``是对应的数据。其次确定这个列表中有多少条数据，后续需要根据这个数值``length``确保将所有的名字都爬取成功。找到存放名字的元素，将含有名字的列表传回来。
```python
def get_data_from(self, titleName):
        self.my_edge.ele(f'text={titleName}').click()
        print('正在获取{titleName}数据')
        
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
```

获取到数据后，则将这个名字数据保存起来。传入茶的种类``kind_of_tea``，再将名字``names``数据传入。将数据保存在指定的文件目录下，若不存在这个目录则创建。将名字一行一行的保存下来。
```python
    #传入指定的分类茶类名字，将数据保存
    def save_data(self, kind_of_tea, titleName, names):
        path = os.path.join(os.path.split(__file__)[0], f'百度星图\\{kind_of_tea}星图')
        if not os.path.exists(path):
            os.mkdir(path)
            
        with open(os.path.join(path, f'{titleName}.txt'), 'w', encoding='utf-8') as f:
            for name in names:
                f.write(name + '\n')
```


当然在打开浏览器窗口之后，不要忘记关闭这个浏览器窗口。
```python
    #退出浏览器窗口
    def quit(self):
        self.my_edge.quit()
```

根据以上代码即可获得绿茶在星图上，有关品种的所有名称。  
此外注意，文件夹中的数据已经为所有能在星图上爬取到的茶类的名称，其他的茶类需要额外在网页进行爬取（还没做）。  
在之后，可以考虑将浏览器的打开方式调整为无头模式（即不需要渲染GUI），可提高运行速度 ~~（虽然现在要爬取的数据还不多）~~。




## 项目目标计划
- [ ] 需要找到包含某行业关键术语的网站
- [ ] 创建知识图谱时，既需要爬取结构化数据，也要爬取非结构化数据
- [ ] 养成编写README的习惯，记录每次修改
- [ ] 应对网站反爬虫的技巧学习
- [ ] 了解GraphRAG的基本信息
- [ ] 从知网上寻找有关大模型与知识图谱相结合的论文，最好是有关于问答系统的，每组需要汇报一篇论文的思路或系统构建过程  





## 项目组会内容记录
- 7月16日，每个小组自行选择有关知识图谱的小项目并实现，在会议上汇报实现情况
- 7月23日，每个小组从[华东师范大学有关农业知识图谱项目][华东师范大学有关农业知识图谱项目]与[个人（可能吧）农业知识图谱项目][个人（可能吧）农业知识图谱项目]中分别选择一项进行复现，在会议上汇报复现进度与成果展示


[华东师范大学有关农业知识图谱项目]: https://github.com/qq547276542/Agriculture_KnowledgeGraph 'GitHub'
[个人（可能吧）农业知识图谱项目]: https://github.com/zhangyqCS/KnowledgeGraph_Agriculture 'GitHub'