import os
import re


def replace_in_file(file_path):
    """在文件中替换指定字符串"""
    try:
        # 尝试多种编码格式打开文件
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

        # 执行替换操作
        new_content = content.replace("'河南书易教育'", "'河南书易教育'")

        # 如果内容有变化才写入
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 已更新: {file_path}")
            return True
        else:
            print(f"🔍 未找到匹配项: {file_path}")
            return False

    except Exception as e:
        print(f"❌ 处理文件出错 {file_path}: {str(e)}")
        return False


def main():
    # 获取当前工作目录
    current_dir = os.getcwd()
    print(f"🔍 正在扫描目录: {current_dir}")
    print("-" * 50)

    # 统计变量
    total_files = 0
    modified_files = 0

    # 遍历当前目录所有文件
    for filename in os.listdir(current_dir):
        file_path = os.path.join(current_dir, filename)

        # 跳过目录
        if os.path.isdir(file_path):
            continue

        # 跳过二进制文件（可选）
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.exe')):
            print(f"⏩ 跳过二进制文件: {filename}")
            continue

        total_files += 1
        if replace_in_file(file_path):
            modified_files += 1

    # 输出统计结果
    print("-" * 50)
    print(f"📊 扫描完成! 共检查 {total_files} 个文件")
    print(f"✨ 成功修改 {modified_files} 个文件")
    print(f"ℹ️ 未修改 {total_files - modified_files} 个文件")


if __name__ == "__main__":
    main()