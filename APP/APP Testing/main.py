import streamlit as st

# for wide mode
st.set_page_config(layout="wide")

# ----------------------------------------functions-------------------------------------------

def concatenate_text_files(uploaded_files):
    concatenated_text = ""
    for uploaded_file in uploaded_files:
        content = uploaded_file.read()
        # Decode content from bytes to string
        decoded_content = content.decode('utf-8')
        concatenated_text += decoded_content + '\n'
    return concatenated_text






# ------------------------------------------Side bar----------------------------------------------
# titile on main page
st.title("Text Summarization App")

# side bar for model selection and file uploadingh

with st.sidebar:
    st.header("Select Model")

    # Multiselect widget
    model_option = st.selectbox('Select Options:', ['T5-Base', 'Bart-large-cnn', 'pegasus-larg', 'LLAMA-2'])

    # file uploadings
    st.header("Upload files")
    # Multifile uploader widget
    uploaded_files = st.file_uploader('Upload Text Files:', type=['txt'], accept_multiple_files=True)

# input text on main page
if uploaded_files is not None:
    concatenated_text = concatenate_text_files(uploaded_files)

#----------------------------------Main Page---------------------------------------------

# Main page columns
col1, col2 = st.columns(2)

# Main page column=1
with col1:
   st.header("Input Text")
   # input text-area
   input_text=st.text_area(f"Your selected model is {model_option}", height=300, value=concatenated_text)
   # input  proceed button
   input_button=st.button("Process Text")

# Main page column=2
with col2:
    st.header("Summary")
    # output text-area
    st.text_area(f"Input Text Length is {len(input_text)}", height=300,)

