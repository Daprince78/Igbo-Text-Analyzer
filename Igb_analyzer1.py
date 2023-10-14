import streamlit as st
import pandas as pd
from io import StringIO
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.corpus import stopwords

#To give the webpage a title
st.title('Igbo Text Analyzer Prototyping App')
Text = st.text_area('Type in a text')

# To get the length of sentences in the Text inputed
tokenize_sent = sent_tokenize(Text)
num_of_sent = len(tokenize_sent)

# To get the number of words in the Text inputed
tokenized_word = word_tokenize(Text)
word_freq = FreqDist(tokenized_word)
num_of_words = word_freq.N()

# To get the number of unique words in the Text inputed
unique_word = []
for w in tokenized_word:
    if w not in unique_word:
        unique_word.append(w)
num_of_Uwords = len(unique_word)


if st.button('submit', type="secondary"):
    st.write("Hello Word")
    st.write("There are", num_of_sent, "Sentences in the inputed Text")
    st.write("There are", num_of_words, "(Tokens) Words in the inputed Text")
    st.write("There are", num_of_Uwords, " Unique (Tokens) words in the Inputed text")


# Option2 if the user decides to upload a file insteat of entering a text
textfile = st.file_uploader('upload a file')
if textfile is not None:
    # convert file to a string
    text_string = StringIO(textfile.getvalue().decode("utf-8"))
    string_data = text_string.read()

    # To get the length of sentences in the file uploaded
    tokenize_sent = sent_tokenize(string_data)
    num_of_sent = len(tokenize_sent)

    # To get the number of words in the file uploaded
    tokenized_word = word_tokenize(string_data)
    word_freq = FreqDist(tokenized_word)
    num_of_words = word_freq.N()

    # To get the number of unique words in the file uploaded
    unique_word = []
    for w in tokenized_word:
        if w not in unique_word:
            unique_word.append(w)
    num_of_Uwords = len(unique_word)

if st.button('Readfile', type="primary"):
    st.write("Hello Word")
    st.write("There are", num_of_sent, "Sentences in the Uploaded file")
    st.write("There are", num_of_words, "(Tokens) Words in the Uploaded file ")
    st.write("There are", num_of_Uwords, " Unique (Tokens) words in the Uploaded file")


