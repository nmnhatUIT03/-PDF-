import streamlit as st
import PyPDF2
import numpy as np
import pickle as pkl

class_list = {'0': 'Benign', '1': 'Malicious'}

st.title('PDF Malware Detection')

input_model = open('xgb_model.pkl', 'rb')
model = pkl.load(input_model)

st.header('Upload a PDF file')

pdf_file = st.file_uploader('Choose a PDF file', type=['pdf'])

if pdf_file is not None:
    # Read the content of the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = ""

    # Concatenate all pages' text
    for page_num in range(len(pdf_reader.pages)):
        pdf_text += pdf_reader.pages[page_num].extract_text()

    # Display the text content of the PDF
    st.text(pdf_text)

    if st.button('Predict'):
        # Process the PDF text (you may need to customize this part based on your PDF content)
        # For example, you can convert text to image or apply natural language processing (NLP) techniques.
        # For simplicity, let's consider the length of the text as a feature for demonstration purposes.
        text_length = len(pdf_text)

        # Convert the text length to a NumPy array
        vector = np.array([[text_length]])

        # Make a prediction
        label = str(model.predict(vector)[0])

        st.header('Result')
        st.text(class_list[label])
