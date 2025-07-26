##这是一个使用 Python 编写的程序，它可以读取指定文件夹下的所有代码文件，并将它们的内容合并输出到一个 `.txt` 文件中。

### 如何使用

1. **保存代码**:
```bash
github clone https://github.com/fuserh/combine_code_files.git
```
2. **打开终端/命令行**: 导航到 `combine_code_files` 目录。
3. **运行程序**:
    *   **基本用法**: 扫描默认支持的代码文件类型。
        ```bash
        python combine_code_files.py /path/to/your/code_folder combined_code.txt
        ```
        - 将 `/path/to/your/code_folder` 替换为你想要扫描的文件夹的实际路径。
        - `combined_code.txt` 是你希望生成的输出文件名，可以自定义。
    *   **指定文件类型**: 只合并特定扩展名的文件。
        ```bash
        python combine_code_files.py ./my_project output.txt -e .py .js .html .css
        ```
        - `./my_project` 是当前目录下的 `my_project` 文件夹。
        - `-e .py .js .html .css` 指定了只处理 Python、JavaScript、HTML 和 CSS 文件。
4. **查看结果**: 程序运行完毕后，在指定的输出路径下会生成一个 `.txt` 文件，里面包含了所有被扫描到的代码文件的内容，每个文件之间用 `--- 文件: ... ---` 分隔。

这个程序具有以下特点：
*   **递归扫描**: 会进入指定文件夹的所有子文件夹进行查找。
*   **可配置扩展名**: 可以通过 `-e` 参数指定要合并哪些类型的代码文件，默认包含了常见的编程语言和标记语言扩展名。
*   **错误处理**: 对无法读取的文件（如编码问题）会给出警告并跳过，不会中断整个程序。
*   **清晰输出**: 在终端会打印正在处理的文件名，方便跟踪进度。

## 许可证

本项目采用GPLv3许可证 - 详见 [LICENSE](LICENSE) 文件。

