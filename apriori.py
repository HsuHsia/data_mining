pip install efficient-apriori #安装apriori包

from efficient_apriori import apriori
# 实验使用的数据集
data = [('牛奶','面包','尿不湿','啤酒','榴莲'),
        ('可乐','面包','尿不湿','啤酒','牛仔裤'),
        ('牛奶','尿不湿','啤酒','鸡蛋','咖啡'),
        ('面包','牛奶','尿不湿','啤酒','睡衣'),
        ('面包','牛奶','尿不湿','可乐','鸡翅')]
# 调用apriori
itemsets, rules = apriori(data, min_support=0.6,  min_confidence=1)
# print(itemsets)
# print(rules)
