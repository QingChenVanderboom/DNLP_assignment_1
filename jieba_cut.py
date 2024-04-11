import jieba

# 待分词的文本
text = "结巴分词是一个常用的中文分词工具，它可以将中文文本切分成一个个有意义的词语。"

# 精确模式分词（默认模式）
seg_list = jieba.cut(text, cut_all=False)

# 输出分词结果
print("精确模式分词结果：", "/ ".join(seg_list))

# 全模式分词
seg_list = jieba.cut(text, cut_all=True)

# 输出分词结果
print("全模式分词结果：", "/ ".join(seg_list))

# 搜索引擎模式分词
seg_list = jieba.cut_for_search(text)

# 输出分词结果
print("搜索引擎模式分词结果：", "/ ".join(seg_list))
