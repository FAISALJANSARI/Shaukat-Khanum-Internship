from functions import concatenate_text_files,gen_summary
import streamlit as st

# # for wide display mode
st.set_page_config(layout="wide")



# ------------------------------------------Sidebar Menue----------------------------------------------
# titile on main page
st.title("Text Summarization App")

# side bar for model selection and file uploadingh

with st.sidebar:
    st.header("Select Model")

    # Multiselect widget
    model_option = st.selectbox('Select Options:', ['Gemini-pro','T5-Base', 'Bart-Large', 'Pegasus-Larg', 'LLAMA-2']) #using'Bart-Large-cnn'

    # file uploadings
    st.header("Upload files")
    # Multifile uploader widget
    uploaded_files = st.file_uploader('Drag Files:', type=['txt'], accept_multiple_files=True)

# input text on main page from uploaded
if uploaded_files is not None:
    concatenated_text = concatenate_text_files(uploaded_files)

#----------------------------------Main Page--------------------------------------------
#******************** nput-textarea and processtext button*************************
# Main page columns 
# input text area
st.header("Input Text")
# input text-area
input_text=st.text_area(f"Your selected model is {model_option}", height=300, value=concatenated_text )
if input_text != '':
    st.text('your text is processed for summarization')
input_button=st.button("Process Text")
    
#------------------------Process text button (Model_Loding & Summary_text)--------------


# prosess after clicking input_button 
# checking button is clicked
if input_button :
 # checking input text is empty after clicking preceed text button 
    if input_text != '':
        # checking for selected model and model loding and making summary for file
        #  # t5 model
        if model_option == 'Gemini-pro' :
            # --------------calling function to genrate summary---------
            with st.spinner('Wait generating summary...'):
                summary=gen_summary(input_text)
            # showing output 
            st.header("Summary")
            # output text-area
            otput_text=st.text_area(f"Summary is genrated using {(model_option)}", height=300, value=summary)

        elif model_option == 'T5-Base' :
            st.warning("Bart-Larg model is not available currently")
        # bart model
        elif model_option == 'Bart-Large':
            st.warning("Bart-Larg model is not available currently")
        # pegasus model
        elif model_option == 'Pegasus-Larg':
            st.warning("Pegasus-Larg model is not available currently")
        # llama model
        elif model_option == 'LLAMA-2':
            st.warning("LLAMA-2 model is not available currently")







    #input text is empty warning 
    else:
        st.warning("Input text area is empty | input text for summary")

