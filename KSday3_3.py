# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:09:22 2023

@author: Lenovo
"""

'''
csv 
    逗号分割值文件格式  也是 excel表格一种形式
    
'''
# 导入csv模块
import csv

# 使用'w'模式打开一个名为'test.csv'的文件，如果文件不存在，则创建一个新的文件。
# 'utf-8-sig'编码方式可以在CSV文件中正确处理中文字符，newline=''可以防止在Windows系统下写入的行之间有额外的空行。
file = open('test.csv', 'w', encoding='utf-8-sig', newline='')

# 使用csv.writer()方法创建一个写入器对象。
# 这个对象有两个方法：writerow()和writerows()，它们分别用于写入单行和多行。
csv_file = csv.writer(file)

# 使用writerow()方法写入一行数据，参数是一个列表，列表的每个元素对应CSV文件中的一个单元格。
csv_file.writerow([1, 2, 3, 4, 5])
csv_file.writerow([6, 7, 8, 9, 10])

# 使用for循环和writerow()方法写入多行数据。
# range(11)会产生一个0到10的整数序列，每次循环都会写入一行新的数据。
for i in range(11):
    csv_file.writerow([i, i+1, i+2])

# 使用writerows()方法写入多行数据，参数是一个二维列表，外层列表的每个元素对应一行，内层列表的每个元素对应一个单元格。
csv_file.writerows(
    [
        ['法外狂徒·张三', '尼古拉斯·赵四', '富兰克林·狗蛋', '亚历山大·熊大'],
        ['王五','HelloWorld','TryAndTest'],
    ]
)

# 注意：在完成所有写入操作后，你应该调用file.close()方法关闭文件。这个操作在你的代码中没有显示，但在实际使用时需要注意。
file.close()