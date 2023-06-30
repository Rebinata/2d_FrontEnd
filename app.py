import streamlit as st
import requests

URL_API = "http://localhost:8000"

# Effectuer une requête API et afficher la réponse
response = requests.get(f"{URL_API}/api/hello")
if response.status_code == 200:
    data = response.json()
    st.write(data["message"])
else:
    st.write("Erreur : Impossible de récupérer les données depuis l'API.")

st.title("Welcome to Sarcasm Analysis")

CSS = """
h1 {
    color: #c1c1c1;
}
.stApp {
    background-image: url(https://images.theconversation.com/files/374303/original/file-20201210-18-elk4m.jpg?ixlib=rb-1.1.0&rect=0%2C22%2C7500%2C5591&q=45&auto=format&w=926&fit=clip);
    background-size: cover;
}
"""

#if st.checkbox('Inject CSS'):
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

columns = st.columns(1)

# Appliquer le style personnalisé à la colonne
columns[0].markdown(
    """
    <div style="background-color: #f2f2f2; padding: 10px;">
        <label style="color: black;">Enter your sentence</label>
        <input type="text" style="width: 100%;">
    </div>
    """,
    unsafe_allow_html=True
)

if st.button('Sarcasm or NOT'):

    result = 0

    if result == 0:
        st.image('https://i.kym-cdn.com/entries/icons/original/000/035/497/Walter.jpg', caption='SERIOUS', width=300)
    elif result == 1:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQppCDrdgehIjzHPQ5Zw_YRgh6MtwBIiErO0w&usqp=CAU', caption='SARCASM', width=300)

    st.write('Powered by the best Team')
else:
    st.write('')




with st.sidebar.expander("USER GUIDE"):
    st.write("Contenu du panneau déroulant 1")

with st.sidebar.expander("WHAT IS SARCASM"):
    st.write("Sarcasm is a form of sharp or mocking irony that aims to ridicule or criticize something or someone. It is a way of expressing oneself in a caustic or satirical manner, often with a humorous intention, but also to convey contempt, indignation, or disdain. Sarcasm is typically characterized by the use of remarks or replies that say the opposite of what one actually thinks, but in an obvious and provocative way, in order to convey a critical or sarcastic message.")

with st.sidebar.expander("THE MOST USEFUL TAB ON THIS PAGE"):
    st.write("You've got it, it's sarcarsm!!!!")
