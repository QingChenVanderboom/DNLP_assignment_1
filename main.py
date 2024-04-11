import math
import re
import time

import jieba


class TraverF():

    # 1 初始化
    def __init__(self, DirS):
        self.DirS = DirS

    def DirT(self):
        return TraverF.ArticleG(self, self.DirS)

    def ArticleG(self, DirS):
        article = []
        count = 0
        r1 = u'[a-zA-Z0-9’!"#$%&\'()（）*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
        with open(DirS, "r", encoding='GB18030') as file:
            filecontext = file.read();
            filecontext = re.sub(r1, '', filecontext)
            filecontext = filecontext.replace("\n", '')
            filecontext = filecontext.replace(" ", '')
            filecontext = filecontext.replace("牋", '')
            filecontext = filecontext.replace(
                "本书来自www.cr173.com免费txt小说下载站\n更多更新免费电子书请关注www.cr173.com", '')
            count += len(filecontext)
            article.append(filecontext)
        return article, count


# 词频统计，方便计算信息熵
def wordTf(tfDic, words):
    for i in range(len(words) - 1):
        tfDic[words[i]] = tfDic.get(words[i], 0) + 1


def bigramTfG(tfDic, words):
    for i in range(len(words) - 1):
        tfDic[(words[i], words[i + 1])] = tfDic.get((words[i], words[i + 1]), 0) + 1


def trigramTfG(tfDic, words):
    for i in range(len(words) - 2):
        tfDic[((words[i], words[i + 1]), words[i + 2])] = tfDic.get(((words[i], words[i + 1]), words[i + 2]), 0) + 1


def unigramC(article, count):
    print("unigramC start")
    before = time.time()
    lineC = 0
    wordsTf = {}
    wordsS = []
    wordsL = 0

    for line in article:
        # for x in jieba.cut(line):
        #     wordsS.append(x)
        #     wordsL += 1
        # wordTf(wordsTf, wordsS)

        wordsS = list(line)
        wordsL = len(wordsS)
        wordTf(wordsTf, wordsS)


        wordsS = []
        lineC += 1

    print("1")
    print("Corpus word count:", count)
    print("Word number:", wordsL)
    entropy = []
    for uni_word in wordsTf.items():
        entropy.append(-(uni_word[1] / wordsL) * math.log(uni_word[1] / wordsL, 2))
    after = time.time()
    print("Time:", round(after - before, 5), "s")
    print("Chinese information entropy of unitary model:", round(sum(entropy), 5), "bit/word")


def bigramC(article, count):
    before = time.time()
    wordsS = []
    wordsL = 0
    lineC = 0
    wordsTf = {}
    bigramTf = {}

    for line in article:
        # for x in jieba.cut(line):
        #     wordsS.append(x)
        #     wordsL += 1

        wordsS = list(line)
        wordsL = len(wordsS)
        wordTf(wordsTf, wordsS)
        bigramTfG(bigramTf, wordsS)

        wordsS = []
        lineC += 1

    bigramL = sum([dic[1] for dic in bigramTf.items()])
    print("2")
    print("Corpus word count:", count)
    print("Word number:", wordsL)

    entropy = []
    for bigramW in bigramTf.items():
        jp_xy = bigramW[1] / bigramL  # 计算联合概率p(x,y)
        cp_xy = bigramW[1] / wordsTf[bigramW[0][0]]  # 计算条件概率p(x|y)
        entropy.append(-jp_xy * math.log(cp_xy, 2))  # 计算二元模型的信息熵
    after = time.time()
    print("Time:", round(after - before, 5), "s")
    print("Chinese information entropy for binary models:", round(sum(entropy), 5), "bit/word")


def trigramC(article, count):
    before1 = time.time()
    wordsS = []
    wordsL = 0
    lineC = 0
    wordsTf = {}
    trigramTf = {}

    for line in article:
        # for x in jieba.cut(line):
        #     wordsS.append(x)
        #     wordsL += 1

        wordsS = list(line)
        wordsL = len(wordsS)

        bigramTfG(wordsTf, wordsS)
        trigramTfG(trigramTf, wordsS)

        wordsS = []
        lineC += 1
    trigramL = sum([dic[1] for dic in trigramTf.items()])

    print("3")
    print("Corpus word count:", count)
    print("Word number:", wordsL)

    entropy = []
    for trigramW in trigramTf.items():
        jp_xy = trigramW[1] / trigramL  # 计算联合概率p(x,y)
        cp_xy = trigramW[1] / wordsTf[trigramW[0][0]]  # 计算条件概率p(x|y)
        entropy.append(-jp_xy * math.log(cp_xy, 2))  # 计算三元模型的信息熵

    after1 = time.time()
    print("Time:", round(after1 - before1, 5), "s")
    print("Chinese information entropy of ternary model:", round(sum(entropy), 5), "bit/word")


if __name__ == '__main__':
    tra = TraverF("./data/merge.txt")
    article, count = tra.DirT()
    unigramC(article, count)
    bigramC(article, count)
    trigramC(article, count)
