# import os
#from turtle import color
import streamlit as st
#import docx 
import os
from transformers import AutoModelWithLMHead, AutoTokenizer
from haystack.nodes import FARMReader
# import streamlit as st
# from haystack.nodes import FARMReader
# from transformers import AutoModelWithLMHead, AutoTokenizer

# st.title("Question Generation and Answering")
# st.write("Enter the context and specify the number of questions to generate.")

# new_reader = FARMReader(model_name_or_path="/content/drive/MyDrive/Colab Notebooks/Training Model")
# context = '''India, officially the Republic of India (Hindi: Bhārat Gaṇarājya),[25] is a country in South Asia. It is the seventh-largest country by area; the most populous country[26][27] and the world's most populous democracy.[28][29][30] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[j] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.'''

access_token = "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"



# a = st.number_input("Enter the number of questions to generate:", min_value=1, step=1)

# def generate_questions(context, num_questions=a, max_length=64):
#   input_text = "generate question: %s </s>" % context
#   features = tokenizer([input_text], return_tensors='pt')

#   outputs = model.generate(input_ids=features['input_ids'],
#                            attention_mask=features['attention_mask'],
#                            max_length=max_length,
#                            num_return_sequences=num_questions,
#                            num_beams=10
#                            ,  # Adjust the value of num_beams for more diverse questions
#                            early_stopping=True)
#   # questions = [tokenizer.decode(output) for output in outputs]
#   questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

#   return questions

# generated_questions = generate_questions(context, num_questions=a)
# for question in generated_questions:
#     st.write("Question:", question)
#     res = new_reader.predict_on_texts(question, [context])
#     for answer in res['answers']:
#         st.write("Answer:", answer.answer)
# if __name__ == "__main__":
#     generate_questions_app()


tokenizer = AutoTokenizer.from_pretrained("Kunjesh07/bert-base-answer-generation",use_auth_token=access_token)
model = AutoModelWithLMHead.from_pretrained("Kunjesh07/bert-base-answer-generation",use_auth_token=access_token)
#@st.cache(suppress_st_warning=True)
#def generate_questions(context, num_questions=1, max_length=64):
#        input_text = "generate question: %s </s>" % context
#        features = tokenizer([input_text], return_tensors='pt')
#
#        outputs = model.generate(input_ids=features['input_ids'],
#                                 attention_mask=features['attention_mask'],
#                                 max_length=max_length,
#                                 num_return_sequences=num_questions,
#                                 num_beams=a,  # Adjust the value of num_beams for more diverse questions
#                                 early_stopping=True)
#
#        questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
#
#        return questions

def generate_questions_app():
    new_reader = FARMReader(model_name_or_path="Kunjesh07/t5-base-question-generation-model",use_auth_token=access_token)
    st.set_page_config(
    page_title="Question Answer Generator",
    # page_icon="https://www.logolynx.com/images/logolynx/16/169ba0bcc2e57b032548eeb606e4e7d5.png",
    layout="wide"
    )
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.markdown(
        """
        <style>
        .block-container.css-1y4p8pa.egzxvld4,
        .main.css-uf99v8.egzxvld5{
            width: 100%;
            background-color:#00cc99;
        }
        .css-164nlkn.egzxvld1,
        .css-qcqlej.egzxvld3,
        .css-18ni7ap.e8zbici2{
        display:none;
        }
        h1{
        background-color:#009999;
        text-align:center;
        color:#ffffff;
        margin-bottom:30px;
        
        }
        h3,css-keje6w.e1tzin5v1
        {
        height:50px;
        background-color:#009999;
        text-align:center;
        color:#ffffff;
        padding:10px;
        margin-top:0px;
        }
        .css-keje6w.e1tzin5v1{
        background-color:#ffffff;
        }
        
        .css-1n543e5{
        background-color: #000000;
        color: #FFFFFF;
        padding: 8px 16px;
        border-radius: 4px;
        font-size: 14px;
        font-weight: bold;
        margin:20px;
        text-align: center;
        border: none;
        position: relative;
        left: 42%;
        
       
        
        }
        body{
        background-color:rgb(0, 204, 153);
        }
        
        .st-bi.st-b3.st-bj.st-bg.st-ar.st-bk.st-as.st-bl.st-bm.st-bn.st-au.st-av.st-ax.st-aw,
        .st-c0.st-ce.st-cf.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-cg.st-ch{
            font-size: 20px;
            font-family: math;
            font-weight: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Question Answer Generator")
    col1, col2 = st.columns(2)
    with col1:
      
      # st.write("Choose Option:")
      # st.write("1) Write Context to generate")
       # st.write("2) Upload File From Local Device")

       st.subheader("Choose option to give input text")
       option=st.radio("",["Input Paragraph"])
    with col2:
       if option == "Input Paragraph":
         st.subheader("Write a paragraph to generate the question and answers")
         user_input = st.text_area("",height=200)
         #st.write("Input Paragraph")
         #st.write('\n')
         #st.write(user_input)
   
      # else:
       #  st.subheader("Upload word document")
        # uploaded_file = st.file_uploader("", type=["docx"])
         #if uploaded_file is not None:
          # doc = docx.Document(uploaded_file)
           #user_input = " ".join([paragraph.text for paragraph in doc.paragraphs])
        # Read and process the uploaded Word document
          # file_contents = uploaded_file.read()
        # Do further processing with the file contents (e.g., extract text, analyze data, etc.)
           #st.write("File Uploaded Successfully!")
       val=st.button("Submit") 
        # else:
     
             
    col3,col4=st.columns(2)
    with col3:
       st.subheader("Input paragraph")
       if user_input!="":
             if option == "Input Paragraph":
                 
                 st.write(user_input)
             elif option == "Upload file":
                # st.subheader("Extracted text from file")
                 if uploaded_file is not None:
                     st.write(user_input)
    with col4:
       st.subheader("Output")
       a = st.number_input("Enter the number of questions to generate:", min_value=1, step=1)
       #@st.cache(suppress_st_warning=True)
       def generate_questions(context, num_questions=1, max_length=64):
               input_text = "generate question: %s </s>" % context
               features = tokenizer([input_text], return_tensors='pt')
       
               outputs = model.generate(input_ids=features['input_ids'],
                                        attention_mask=features['attention_mask'],
                                        max_length=max_length,
                                        num_return_sequences=num_questions,
                                        num_beams=a,  # Adjust the value of num_beams for more diverse questions
                                        early_stopping=True)
       
               questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
       
               return questions

       if st.button("Generate"):
                
                generated_questions = generate_questions(user_input, num_questions=a)
                for question in generated_questions:
                    st.write( question)
                    res = new_reader.predict_on_texts(question, [user_input])
                    for answer in res['answers']:
                        st.write("Answer:", answer.answer)



    

    

if __name__ == "__main__":
    generate_questions_app()
