# 假设KBC1文件的格式是规则按行存储，每行以'[ ]'包围，内容是'::'分隔的元素
def read_kbc1_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # 移除行首行尾的空白字符并去除可能存在的换行符
            line = line.strip()
            # 如果该行不是一个规则，则跳过
            if not line.startswith('[') or not line.endswith(']'):
                continue
            # 使用split方法分割每行的内容
            rule_elements = line[1:-1].split('::')
            # 打印或处理规则元素
            print(rule_elements)


# 使用函数读取KBC1文件
read_kbc1_file('hello.kbc1')