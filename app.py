from pathlib import Path

import streamlit as st
from PIL import Image

#  ----PATH SETTINGS--

current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file= current_dir / "styles" / "main.css"
resume_file= current_dir / "assets" / "Resume.pdf"
profile_pic= current_dir / "assets" / "profile-pic.png"


#---- General Settings----

PAGE_TITLE= "Digital Resume | Asutosh Rath"
PAGE_ICON = ":wave:"
NAME= "Asutosh Rath"
DESCRIPTION= """
Data Analyst and Machine Learning Entusiast

"""

EMAIL= "asutoshrath2000@gmail.com"

SOCIAL_MEDIA= {
    "LinkedIn": "https://www.linkedin.com/in/asutosh0213/",
    "GitHub": "https://github.com/Asutosh-R",
    "Kaggle": "https://www.kaggle.com/asutoshrath"
}

PROJECTS = {
    "Home Price Prediction - Predicting Price of House"
    "Books Recommendation System- Recommeding books as per user preference and also as per genre"
    
}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

# ---LOAD CSS, PDF & PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte= pdf_file.read()

profile_pic = Image.open(profile_pic)

# ------ HERO SECTION -----

col1,col2= st.columns(2, gap= "small")
with col1:
    st.image(profile_pic, width= 230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" Download Resume ",
        data= PDFbyte,
        file_name= resume_file.name,
        mime= "application/octet-stream",
    )
    st.write( "📧", EMAIL  )


# --- SOCIAL MEDIA ----
st.write("#")
cols= st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- EXPERIENCE & QUALIFICATIONS ----

st.write("#")
st.subheader("Experience & Qualification")
st.write(
    """
    - Fresher looking for jobs in Data Science and Machine Learning Field
    - Strong hands on experience and knowledge in Python, SQL, Machine Learning, R and Excel
    - Good understanding of statistical principles and their respective applications

    """

     
)



# --- HARD SKILLS ---

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - Programming: Python(Sklearn, Pandas, TensorFlow), SQL, VBA
    - Data Visualization: PowerBi, MS Excel
    - Modeling: Linear Regression, Logistic Regression

    """
         )