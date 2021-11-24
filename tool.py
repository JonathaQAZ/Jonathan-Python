import word
import streamlit as st


def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


# 加载英语翻译中文的数据集，并保存成字典
@st.cache(allow_output_mutation=True)
def load_EN_CN():
    words = {}

    skip = 0
    with open('ecdict.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if skip > 0:
                data = line.split(",")
                single_word = word.EN_CN_Word(data[0].lower(), data[1], data[2], data[3])
                data[0] = data[0].lower()
                words[data[0]] = single_word
            skip = skip + 1

    return words


# 加载中文翻译英文的数据集，并保存成字典
@st.cache(allow_output_mutation=True)
def load_CN_EN():
    words = {}
    skip = 0
    with open('cedict_ts.u8', 'r', encoding='utf-8') as file:
        for line in file:
            if skip > 0:
                line = line.strip()
                data = line.split("[")
                china_word = data[0].split(' ')[1]
                china_pronouciation = '['+data[1].split('/')[0]
                china_translation = [x for x in data[1].split('/')[1:] if x != '']
                single_word = word.CN_EN_Word(china_word, china_pronouciation, china_translation)
                words[china_word] = single_word
            skip = skip + 1

    return words
