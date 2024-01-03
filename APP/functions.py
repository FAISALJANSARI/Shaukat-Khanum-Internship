# Defining function for using in main.py file


# function for reading and concatenating  multiple text files 
def concatenate_text_files(uploaded_files):
    concatenated_text = ""
    for uploaded_file in uploaded_files:
        content = uploaded_file.read()
        # Decode content from bytes to string
        decoded_content = content.decode('utf-8')
        concatenated_text += decoded_content + '\n'
    return concatenated_text


# function to initialize all 3 models at once
def my_models():
    from transformers import pipeline
    model_t5=pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
    # model_bart=pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn", framework="tf")
    # model_pegasus=pipeline("summarization", model="google/pegasus-large", tokenizer="google/pegasus-large", framework="tf")
    
    return model_t5

# function to genrate summary
def my_summary(model,text):
    modelsummary = model(text, max_length=150, min_length=30, early_stopping=True , num_beams=4 , do_sample=True)
    gen_text=modelsummary[0]['summary_text']
    return gen_text


# building main function for this file
if __name__ == "__main__":
    print("*****--Inside Main Functions--*****")

