from functions import concatenate_text_files, my_models, my_summary 
import time
import streamlit as st

# # for wide display mode
# st.set_page_config(layout="wide")


# ------------------------------------------Variables defining----------------------------------------------

# creating variable for loading model
models_are_loaded=False

# # creating variable for summary
# summary=''


# ----------------------------------------functions calling-------------------------------------------





# ------------------------------------------Sidebar Menue----------------------------------------------
# titile on main page
st.title("Text Summarization App")

# side bar for model selection and file uploadingh

with st.sidebar:
    st.header("Select Model")

    # Multiselect widget
    model_option = st.selectbox('Select Options:', ['T5-Base', 'Bart-Large', 'Pegasus-Larg', 'LLAMA-2']) #using'Bart-Large-cnn'

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
    st.text(f'Input Text Length is {len(input_text)}')
input_button=st.button("Process Text")
    
#------------------------Process text button (Model_Loding & Summary_text)--------------


# prosess after clicking input_button 
# checking button is clicked
if input_button :
 # checking input text is empty after clicking preceed text button 
    if input_text != '':
        # checking for selected model and model loding and making summary for file
        #  # t5 model
        if model_option == 'T5-Base' :
            # checking model is loaded or not
            # loading all models
            if models_are_loaded==False:
                with st.spinner('Wait model is loading...'):
                    st.info('it will take some time')
                    t5=my_models()
                    models_are_loaded=True
            with st.spinner('Genrating Summary...'):
                # using inheteted funtion to genrate summary
                summary=my_summary(t5,input_text)
                # saving summary into file
                with open("summary.txt", "wt", encoding="utf-8") as file:
                    file.write(summary)
                st.success('Done!')

        # bart model
        elif model_option == 'Bart-Large':
            st.warning("Bart-Larg model is not available currently")
        # pegasus model
        elif model_option == 'Pegasus-Larg':
            st.warning("Pegasus-Larg model is not available currently")
        # llama model
        elif model_option == 'LLAMA-2':
            st.warning("LLAMA-2 model is not available currently")


        #**************OUTPUT Showing*************
        # inside above conditions
        # output text area
        st.header("Summary")
        # output text-area
        otput_text=st.text_area(f"Output Text Length is {len(summary)}", height=300, value=summary)
        # Button for downloading summary text
        # Provide a download link for the user
        if len(otput_text)>5:
            st.download_button('Download Summary', summary , file_name='summary.txt')
            st.text(f'Output Text Length is {len(summary)} and The Model You Used is {model_option}')


    #input text is empty warning 
    else:
        st.warning("Input text area is empty | input text for summary")

