import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":Home:",
)



custom_css = """
    <style>
[data-testid="stAppViewContainer"]{
background-color: white;

}
[data-testid="stSidebar"]{
  background-image: linear-gradient(to bottom right, green, white);


}
    </style>
"""
# Display the custom CSS using st.markdown
st.markdown(custom_css, unsafe_allow_html=True)

st.header("C'EST QUOI UN SIGNIAL ECG", divider='green')
st.title('Electrocardiogramme :chart:')

st.markdown(
    """
   Un électrocardiogramme est une représentation graphique de l’activation électrique du cœur à l’aide d’un électrocardiographe.
    Cette activité est recueillie sur un patient allongé, au repos, par des électrodes posées à la surface de la peau. 
    Ces électrodes enregistrent des signaux électriques (déflexions) dans au moins douze dérivations, 
   dont six dans le plan frontal (électrodes des membres) et six dans le plan horizontal (électrodes précordiales).
   L’activité électrique peut être enregistrée et reproduite sur papier millimétré ou numérisée. Un tracé ECG standard correspond généralement à l’activité électrique du coeur pendant 10 sec. 
   L’étalonnage usuel du signal ECG est 1 mV = 10 mm et la vitesse de déroulement du papier millimétré de 25 mm/sec.
    Un filtre pour les fréquences trop basses ou trop hautes est recommandé : 0,05 Hz et 150 Hz chez l’adulte, mais il faut l’adapter à chaque situation en cas de parasites [1]. 
    Attention l’usage d’un filtre modifie le tracé (cf. Filtre).
   Ces réglages sont modifiables avant ou après enregistrement grâce aux ECG numérisés.
  
""",
)

st.image('pages/ECGIMAGE.jpg')
st.divider()
st.markdown(
    """
  L’électrocardiogramme (ECG) est un outil diagnostique dont la performance (sensibilité, spécificité) est variable selon les indications (voir ci-dessous) pour très nombreuses maladies cardiaques ou extracardiaques en association avec les données cliniques et souvent biologiques ou échocardiographiques [2].
   Il est parfois le point de départ du traitement de nombreuses maladies parfois mortelles. 
   Il est utilisé par presque tous les spécialistes médicaux, en particulier à l’hôpital (cardiologues, mais aussi urgentistes, anesthésistes, réanimateurs, pneumologues, internistes, psychiatres, pédiatres, gériatres, médecins du sport…).
    C’est un outil indispensable partout et encore plus dans certaines parties du monde. L’enseignement universitaire pour la lecture de l’ECG est malheureusement sommaire.

Sa performance (sensibilité, spécificité) varie selon les indications… Le diagnostic ou le dépistage.

""",
)
st.divider()
url ="https://www.youtube.com/watch?v=OtUPjnj_zC4"
st.video(url, format="video/mp4", start_time=0)
st.divider()
st.markdown(
    """
    Le signal ECG permet de vérifier le bon fonctionnement du cœur chez un patient. Grâce à l’électrocardiographe,
     le personnel soignant peut visualiser la représentation graphique de l’activité électrique du cœur.
    L’analyse du signal ECG est utile dans le but de diagnostiquer des anomalies cardiaques telles qu’une arythmie,
     un risque d’infarctus, de maladie cardiaque cardiovasculaire ou encore extracardiaque. 
    ### Want to learn more?
    - Check out [msdmanuals.com](https://www.msdmanuals.com/fr/professional/troubles-cardiovasculaires/tests-et-proc%C3%A9dures-cardiovasculaires/%C3%A9lectrocardiographie)

""",
)
