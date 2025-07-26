import os
import argparse

def is_code_file(filename, extensions):
    """检查文件是否为指定扩展名的代码文件"""
    return any(filename.lower().endswith(ext) for ext in extensions)

def read_and_combine_code_files(folder_path, output_file, extensions):
    """
    递归读取文件夹下的所有代码文件，并将内容写入输出文件。
    
    :param folder_path: 要扫描的文件夹路径
    :param output_file: 输出的文本文件路径
    :param extensions: 要包含的代码文件扩展名列表
    """
    try:
        # 使用 'w' 模式打开文件，这会清空文件（如果已存在）或创建新文件
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # os.walk 递归遍历目录树
            for root, dirs, files in os.walk(folder_path):
                # 遍历当前目录下的所有文件
                for file in files:
                    # 检查文件是否为代码文件
                    if is_code_file(file, extensions):
                        # 构造文件的完整路径
                        file_path = os.path.join(root, file)
                        try:
                            # 以 UTF-8 编码读取文件内容
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                print(f"正在处理文件: {file_path}")
                                # 写入分隔符和文件名作为标题
                                outfile.write(f"\n\n--- 文件: {file_path} ---\n\n")
                                # 读取并写入文件内容
                                outfile.write(infile.read())
                        except UnicodeDecodeError:
                            # 如果 UTF-8 解码失败，尝试使用 'latin-1' 或忽略错误
                            print(f"警告: 无法以 UTF-8 解码文件 {file_path}，跳过此文件。")
                            # 如果需要，可以取消下面的注释来尝试其他编码
                            # with open(file_path, 'r', encoding='latin-1', errors='ignore') as infile:
                            #     outfile.write(f"\n\n--- 文件: {file_path} (编码可能不正确) ---\n\n")
                            #     outfile.write(infile.read())
                        except Exception as e:
                            # 捕获其他可能的IO错误
                            print(f"处理文件 {file_path} 时出错: {e}")
        
        print(f"所有代码文件已成功合并到 '{output_file}'")
    
    except Exception as e:
        print(f"程序执行出错: {e}")

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description="将文件夹下的所有代码文件内容合并到一个文本文件中。",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
使用示例:
  python combine_code_files.py /path/to/your/code_folder combined_code.txt
  python combine_code_files.py ./my_project output.txt -e .py .js .html .css
        """
    )
    parser.add_argument("folder_path", help="要扫描的代码文件夹路径")
    parser.add_argument("output_file", help="输出的合并后文本文件名")
    parser.add_argument(
        "-e", "--extensions",
        nargs='+',
        default=['.py', '.js', '.java', '.cpp', '.c', '.cs', '.go', '.rb', '.php', '.swift', '.kt', '.ts', '.sql', '.html', '.htm', '.xml', '.css', '.scss', '.sass', '.less'],
        help="要包含的代码文件扩展名列表 (默认: 常见代码文件扩展名)"
    )
    
    # 解析命令行参数
    args = parser.parse_args()

    # 获取参数
    folder_path = args.folder_path
    output_file = args.output_file
    extensions = args.extensions

    # 检查输入文件夹是否存在
    if not os.path.isdir(folder_path):
        print(f"错误: 指定的文件夹路径 '{folder_path}' 不存在或不是一个目录。")
    else:
        # 调用主函数执行合并操作
        read_and_combine_code_files(folder_path, output_file, extensions)
