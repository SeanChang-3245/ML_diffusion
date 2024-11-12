import streamlit as st
import pandas as pd

options = ['紅嘴黑鵯', '白頭翁']
image_paths = {
    '紅嘴黑鵯': './blackbulbul.jpeg',
    '白頭翁': './white.jpeg',
}
audio_paths = {
    '紅嘴黑鵯': './black.mp3',
    '白頭翁': './white.mp3',
}

selected_option = st.radio("Choose one bird species and generate its sound", options)

# Display the corresponding image and audio
if selected_option:
    st.image(image_paths[selected_option], caption=selected_option)
    audio_file_path = audio_paths[selected_option]
    with open(audio_file_path, "rb") as audio_file:
        st.audio(audio_file.read(), format='audio/mp3')

# Create one-hot vector
one_hot_vector = [1 if option == selected_option else 0 for option in options]
