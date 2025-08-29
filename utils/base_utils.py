import json
from decimal import Decimal, getcontext

def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print("JSON数据读取成功！")
        return data
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 未找到。")
        return None
    except json.JSONDecodeError:
        print(f"错误：文件 '{file_path}' 不是有效的JSON格式。")
        return None
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return None

def high_precision_sum(numbers, precision=20):
    # 设置计算精度
    getcontext().prec = precision

    total = Decimal(0)
    for num in numbers:
        if num is None:
            continue
        try:
            # 将元素转换为Decimal类型以保证精度
            decimal_num = Decimal(str(num))
            total += decimal_num
        except (ValueError, TypeError) as e:
            raise TypeError(f"列表中包含无法转换为数值的元素: {num}") from e

    return total
