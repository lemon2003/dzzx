import os
import re


def clean_tbody_content(file_path):
    """
    删除HTML文件中<tbody>到</tbody>标签之间的所有内容
    保留<tbody>和</tbody>标签本身
    """
    try:
        # 尝试多种编码打开文件
        encodings = ['utf-8', 'gbk', 'latin-1']
        content = None

        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue

        if content is None:
            print(f"⚠️ 无法解码文件: {file_path}")
            return False

        # 使用正则表达式删除<tbody>和</tbody>之间的内容
        # 保留标签本身
        pattern = r'(<tbody\b[^>]*>)(.*?)(</tbody>)'
        cleaned_content = re.sub(
            pattern,
            r'\1\3',  # 保留开始标签和结束标签
            content,
            flags=re.DOTALL  # 使.匹配包括换行符的所有字符
        )

        # 如果内容有变化才写入
        if cleaned_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            print(f"✅ 已清理: {file_path}")
            return True
        else:
            print(f"🔍 未找到<tbody>标签: {file_path}")
            return False

    except Exception as e:
        print(f"❌ 处理文件出错 {file_path}: {str(e)}")
        return False


def main():
    # 目标文件名
    target_file = "zhuanye.html"

    # 检查文件是否存在
    if not os.path.exists(target_file):
        print(f"❌ 文件不存在: {target_file}")
        return

    # 检查是否是文件而不是目录
    if not os.path.isfile(target_file):
        print(f"❌ 路径不是文件: {target_file}")
        return

    print(f"🔍 正在处理文件: {target_file}")
    print("-" * 50)

    # 处理文件
    if clean_tbody_content(target_file):
        print("-" * 50)
        print(f"✅ 成功清理 {target_file} 中的<tbody>内容")
    else:
        print("-" * 50)
        print(f"ℹ️ 未对 {target_file} 进行修改")


if __name__ == "__main__":
    main()