import os


def merge_txt_files(folder_path, output_file):
    with open(output_file, 'w', encoding='gb18030') as outfile:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                filepath = os.path.join(folder_path, filename)
                with open(filepath, 'r', encoding='gb18030') as infile:
                    content = infile.read()
                    outfile.write(content)
                    outfile.write('\n')  # 添加一个换行符，以便在合并后的文件中区分不同文件的内容
    print("合并完成！")


# 示例用法
folder_path = "./data"
output_file = "./output.txt"
merge_txt_files(folder_path, output_file)
