import pandas as pd

# 读取CSV文件
df = pd.read_csv('2024-spring-DB-Project/dbLab2024/lectures_final.xlsx')

# 假设我们要处理的列名为 'column_to_split'
def split_column(data):
    first_part = data[:3]  # 前三个字符
    second_part = data[3:]  # 第四个字符及之后
    return first_part, second_part