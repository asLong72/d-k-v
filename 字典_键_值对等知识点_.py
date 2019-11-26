
#键-值对

alien_0={'color':'green','points':5}             #alien_0字典中的两个键-值对, 在调用信息时分别每对键值都存在对应关系, 调用(名称)[键], 就给予值
                                                 #值可以是元素或列表(字典中嵌套列表), 甚至可以是字典(字典中嵌套字典)
                                                 #嵌套: 字典中嵌套列表 / 字典中嵌套字典
                                                 #同样,列表中也可以嵌套字典
                                                 #字典中的键值对之间无先后顺序

#访问字典中的值
print(alien_0['color'])
print(alien_0['points'])

new_gets_point=alien_0['points']                 #将键对应值赋给变量

#对字典中键值对的修改
a={ }

a['a']='a'                                       #分行为字典增加键值对
a['a']='A'                                       #对字典中键值对的关联关系的修改
del a['a']                                       #删除字典中键值对

#遍历
#遍历对
for key,value in alien_0.items():
    print(key,value)

#遍历键
for key in alien_0.keys():                       #遍历建的方法1,keys()函数返回一个列表
     print(key)
for key in alien_0:                              #两种遍历键的方法效果一样
     print(key)
#可以用公共函数: sorted()函数对私有函数: keys()函数生成的由键的名字组成的列表进行排序
if 's' not in alien_0.keys():                    #检查字典中有无键's',无则输出's'
    print('s')

#遍历值
p=alien_0.values()                               #同样,values()函数返回一个列表
for value in p:   
    print(value)
print(p)