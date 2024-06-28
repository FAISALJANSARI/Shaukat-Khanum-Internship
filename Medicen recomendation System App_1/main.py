import streamlit as st
import ast
from functions import symtoms_li,symptoms_dict,pkl_model_svc,get_predicted_value,helper

dis=None

st.title("Medicine Recommender")
syptoms_selected=st.multiselect('Select Symptoms :',symtoms_li)

if len(syptoms_selected) !=0:

    if st.button('Submit'):
        dis=get_predicted_value(syptoms_selected)
        disease_text=f"predicted disease is {dis}"
        st.subheader(disease_text)



        desc,pre,med,die,wrkout=helper(dis)
        # descriptio
        st.subheader('Description:')
        st.text(desc.values[0])
        # precaution
        st.markdown("""---""")
        st.subheader('Precautions:')
        for item in pre.values[0]:
            st.text(item)
        # workout
        st.markdown("""---""")
        st.subheader('Important Notes:')
        for nots in wrkout:
            st.text(nots)
        # diet
        st.markdown("""---""")
        st.subheader('Dite:')
        for diet in ast.literal_eval(die.values[0]):
            st.text(diet)
        # Medicens
        st.markdown("""---""")
        st.subheader('Medicens:')
        for mid in ast.literal_eval(med.values[0]):
            st.text(mid)





    
    # if st.button('Show Description'):
    #     print("**********")
    #     print('Values======>',desc)
    #     st.title(desc.values[0])
    #     if st.button('Show Precautions'):
    #     if st.button('Show diet'):
    #     if st.button('Show notes'):
    #     if st.button('Show Medicen'):
