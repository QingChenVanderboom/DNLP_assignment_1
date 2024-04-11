import re
import numpy as np
import matplotlib.pyplot as plt

# 读取 merge.txt 文件并统计词频
word_freq = {}
with open("data/merge.txt", "r", encoding="GB18030") as file:
    text = file.read()
    words = re.findall(r'\w+', text)  # 使用正则表达式找到所有单词
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

# 加载停用词列表
stopwords = set()
with open("cn_stopwords.txt", "r", encoding="utf-8") as stopword_file:
    for line in stopword_file:
        stopwords.add(line.strip())

# 过滤词频统计结果
filtered_word_freq = {}
for word, freq in word_freq.items():
    if word not in stopwords:
        filtered_word_freq[word] = freq

# 将过滤后的词频按降序排序
sorted_filtered_word_freq = sorted(filtered_word_freq.items(), key=lambda x: x[1], reverse=True)

# 计算过滤后词频排名和频率
filtered_freq = np.array([item[1] for item in sorted_filtered_word_freq])
filtered_rank = np.arange(1, len(filtered_freq)+1)

# 将词频记录在文本文件中
with open('filtered_word_frequency.txt', 'w', encoding='utf-8') as output_file:
    for word, freq in sorted_filtered_word_freq:
        output_file.write(f"{word}: {freq}\n")

# 绘制词频分布图（过滤后）
plt.figure(figsize=(10, 6))
plt.plot(filtered_rank, filtered_freq, marker='o', linestyle='-')
plt.title("Zipf's Law: Word Frequency Distribution (Filtered)")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale('log')  # 使用对数坐标轴
plt.yscale('log')
plt.grid(True)
plt.show()
