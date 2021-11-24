import streamlit as st

import tool

words_EN_CN = tool.load_EN_CN()
words_CN_EN = tool.load_CN_EN()

if __name__ == '__main__':

    st.title("DICTIONARY")
    st.write("""
    by Jonathan&Frank&FourierYe
    """)
    input_text = st.text_input("""please input your word""","China")
    if tool.is_contains_chinese(input_text):
        if input_text in words_CN_EN:
            word = words_CN_EN[input_text]
            st.info("拼音："+word.pronouciation)
            st.info("释义："+','.join(word.translation))
        else:
            st.warning('dictionary doesn\'t exit this word!')
    else:
        input_text = input_text.lower()
        if input_text in words_EN_CN:
            word= words_EN_CN[input_text]
            st.info("Phonetic symbol:"+word.phonetic)
            st.info("Definition is:"+word.definition)
            st.info("Translation is:"+word.translation)




        else:
            st.warning('dictionary doesn\'t exit this word!')