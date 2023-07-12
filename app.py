import streamlit as st
import requests
import random
import base64

URL_API = "https://sarcasme-uwd4nnxq3a-ew.a.run.app/predict?"

def home_page():
    st.markdown(
    """
    <style>
    .header-text {
        color: #B31129		;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    # Affichage de l'en-tête avec la classe CSS personnalisée
    st.markdown('<h1 class="header-text">Welcome to Sarcasm Analysis\U0001F916</h1>', unsafe_allow_html=True)


    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('photos/Sans-titre_3_-modified.png')

        #if st.checkbox('Inject CSS'):




    with st.sidebar.expander("USER GUIDE"):
            st.write("You and I both know that politicians always tell the truth and are always serious in their statements. With this application, you will finally have the opportunity to prove it to yourself. For that, all you need to do is enter a sentence, press the button, and at your own risk, discover the truth.")

    with st.sidebar.expander("WHAT IS SARCASM"):
            st.write("Sarcasm is a form of sharp or mocking irony that aims to ridicule or criticize something or someone. It is a way of expressing oneself in a caustic or satirical manner, often with a humorous intention, but also to convey contempt, indignation, or disdain. Sarcasm is typically characterized by the use of remarks or replies that say the opposite of what one actually thinks, but in an obvious and provocative way, in order to convey a critical or sarcastic message.")

    with st.sidebar.expander("THE MOST USEFUL TAB ON THIS PAGE"):
            st.write("You've got it, it's sarcarsm!!!!")


        # Obtenez l'entrée de l'utilisateur à partir de la boîte de saisie de texte
    text_mixed = "<span style='color: #B31129; font-weight: bold;'>Enter your sentence</span>"
    # Afficher la phrase avec la couleur personnalisée
    st.markdown(text_mixed, unsafe_allow_html=True)
    user_input = st.text_area("", value="In the course of my life I have often had to eat my words, and I must confess that I have always found it a wholesome diet.", key="user_input",height=3)
    if st.button('Is it Sarcastic? 🙄'):
            # Utilisez l'entrée de l'utilisateur dans votre appel API
            with st.spinner('Requeting API ...'):

                response = requests.get(URL_API, params={"sentence": user_input})
            if response.status_code == 200:
                st.balloons()
                data = response.json()
                # Utilisez 'data' pour faire quelque chose d'utile ici
                # result = data["sentence"] # Assurez-vous que votre API renvoie un 'result' dans la réponse
                print(data)
                if data < 0.5:
                    st.image('https://i.kym-cdn.com/entries/icons/original/000/035/497/Walter.jpg', caption='SERIOUS', width=300)
                else:
                    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQppCDrdgehIjzHPQ5Zw_YRgh6MtwBIiErO0w&usqp=CAU', caption='SARCASM', width=300)
                st.write('Powered by the best Team')
            else:
                st.write('Error: Unable to retrieve data from API.')
    else:
            st.write('')

def other_page():
    st.header("Welcome to the most epic\
    sarcasm competetion \U0001F525 ")
    sarcasm_text = """Oh, wow! A sarcasm competition. How utterly thrilling and enthralling.
I can hardly contain my excitement. Sarcasm is, after all, the pinnacle of sophisticated humor.
I'm absolutely dying to participate in such a prestigious event. My heart is racing with anticipation.
Can you sense the overwhelming sarcasm in my words? It's practically dripping off the screen.
Oh, what a marvelous occasion this is. Truly, a dream come true."""

    st.write(sarcasm_text)

    CSS = """
        h1 {
            color: #ffffff 	;
        }
        .stApp {
            background-image: url(https://images.theconversation.com/files/374303/original/file-20201210-18-elk4m.jpg?ixlib=rb-1.1.0&rect=0%2C22%2C7500%2C5591&q=45&auto=format&w=926&fit=clip);
            background-size: cover;
        }
        """
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
    st.header("The Game \U0001F47E")
    with st.sidebar.expander("USER GUIDE"):
            st.write("""Player 1 enters a sentence, and then Player 2 takes their turn to enter a sentence.
                        After that, you need to press the 'OK' button.""")
            st.write("""Please note that the first loading may take some time, but since you're here, it seems like you don't have much else to do.
                        The winner will be displayed below the two blocks of text.
                        """)

    # Créer deux colonnes côte à côte

    #Créer deux colonnes côte à côte
    col1, col2 = st.columns(2)

    # Variables pour stocker les phrases et les scores
    phrase_1 = ""
    phrase_2 = ""
    score = 0

    # Champ de saisie de texte pour la première colonne
    with col1:
        phrase_1 = st.text_area("PLAYER 1 \U0001FAC0", value="If stupid could fly, you would be a jet",  height=3)

    # Champ de saisie de texte pour la deuxième colonne
    with col2:
        phrase_2 = st.text_area("PLAYER 2 \U0001F9E0", value="You are so mean that your standard deviation is zero", height=3)

    # Vérifier si les deux phrases ont été saisies et si le bouton "OK" a été cliqué
    if phrase_1 and phrase_2 and st.button("PLAY"):
        # Effectuer l'appel API pour la première phrase
        response_1 = requests.get(URL_API, params={"sentence": phrase_1})
        if response_1.status_code == 200:
            data_1 = response_1.json()
            #score_1 = data_1.get("score", 0)

        # Effectuer l'appel API pour la deuxième phrase
        response_2 = requests.get(URL_API, params={"sentence": phrase_2})
        if response_2.status_code == 200:
            data_2 = response_2.json()
            #score_2 = data_2.get("score", 0)

        # Mettre à jour le score en fonction des scores renvoyés par l'API
        if data_1 > data_2:
            col_1, col_2 ,col_3, col4=st.columns(4)
            with col_2:
                st.title('Player 1 ')
                # st.write(data_1)
                # st.write(data_2)
            st.image("https://us.v-cdn.net/cdn-cgi/image/fit=scale-down,/http://i.qkme.me/3ogxbr.jpg",width=500)



        else:
            col_1, col_2 ,col_3=st.columns(3)
            with col_2:
                st.header('Player 2 ')
                # st.write(data_1)
                # st.write(data_2)
            st.image("https://us.v-cdn.net/cdn-cgi/image/fit=scale-down,width=1600/http://i.qkme.me/3ogxbr.jpg",width = 500)
def lastpages():
    st.title("La TEAM \U0001F680 ")
    col1, col2, col3,col4 = st.columns(4)

    image_width = 200

    with col1:
        st.markdown("[Aminata](http://www.linkedin.com/in/aminata-traore-31b171156)")
        st.image('photos/teammember1.png',width=250)


    with col2:

        st.markdown("[Afaf](https://www.linkedin.com/in/afafjaber/)")
        st.image('photos/teammember2.png',width=image_width)



    with col3:
        st.markdown("[Cédric](https://www.linkedin.com/in/cédric-najdek-17569114b)")
        st.image('photos/teammember3.png', width=image_width)





pages = {
        "Home": home_page,
        "The Game": other_page,
        "La Team" : lastpages,

    }

selection = st.sidebar.radio("Navigation", list(pages.keys()))

pages[selection]()
