import streamlit as st
from streamlit_lottie import st_lottie
import os
from PIL import Image
import requests

st.set_page_config(page_title="Serah Portfolio", page_icon=":stars:",layout="wide")
image = Image.open(f'{os.getcwd()}/pics/serah1.jpg')
left_column,c2,right_column = st.columns(3)
with left_column:
    url4 = requests.get("https://assets7.lottiefiles.com/packages/lf20_txli4cbw.json") #working
    if url4.status_code == 200:
        url4_json = url4.json()
        st_lottie(url4_json,speed=1,loop=True,quality="low",height=300,width=300)
    else:
        st.write("Error in the URL")
with c2:
        st.title("**A Journey of Ambition and Adventure: Trading, Beauty, Fashion, and Novels**")
with right_column:
    st.image(image, width=200,use_column_width= 500)

hide_st_style="""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

left_column,right_column = st.columns(2)
with left_column:
    st.markdown(
    """

In the vibrant tapestry of life, my story unfurls as that of a fun-loving, ambitious, and hardworking lady who embarked on a journey fueled by her passions for trading, adventure, beauty products, fashion, and the enchanting world of novels. Through the highs and lows, I've woven together a life that's both a reflection of my inner desires and a testament to the power of determination.

From a young age, my heart was captivated by the thrill of trading. The dynamic interplay of markets, the rush of decision-making, and the potential for growth ignited a fire within me. Armed with determination and an insatiable thirst for knowledge, I immersed myself in the world of finance. With each success and setback, I honed my skills and learned to navigate the intricate landscape of stocks and commodities. The fast-paced nature of trading mirrored my energetic spirit, and I found myself thriving in this ever-evolving realm.


""", unsafe_allow_html=True
) 

with right_column:
    image2 = Image.open(f'{os.getcwd()}/pics/s2.jpg')
    st.image(image2, width=200,use_column_width= 500)


left_column,right_column = st.columns(2)
with left_column:
    image3 = Image.open(f'{os.getcwd()}/pics/s3.jpg')
    st.image(image3, width=200,use_column_width= 500)
with right_column:
    st.markdown("""However, life's journey is rarely singular, and I discovered another facet of my identity – a passion for adventure. Exploring new horizons, be it through travel or personal challenges, became an integral part of who I am. Whether it was trekking through remote mountains, diving into uncharted waters, or simply embarking on a solo road trip, I embraced the unknown with an open heart. These adventures not only enriched my life but also instilled in me a sense of resilience and adaptability that proved invaluable in both my trading pursuits and personal growth.

Beyond the world of numbers and charts, my heart also danced to the rhythm of beauty and fashion. The allure of beauty products and the creative canvas of fashion allowed me to express myself in a whole new way. Experimenting with colors, textures, and styles, I discovered that beauty and fashion were not just superficial, but powerful tools for self-confidence and self-expression. This realization led me to explore the industry further, from studying skincare formulations to curating my own wardrobe. The artistry of beauty and fashion merged seamlessly with my ambitious spirit, inspiring me to blend creativity with entrepreneurship.
""")
        
left_column,right_column = st.columns(2)
with left_column:
    st.markdown("""While my days were often filled with numbers, adventure, beauty, and fashion, my nights were dedicated to the enchanting worlds woven by authors' words. Novels became my escape, my sanctuary, and my source of endless inspiration. From the classics to contemporary fiction, each book transported me to different times, places, and perspectives. This love for literature nurtured my imagination and honed my communication skills, enabling me to connect with people from all walks of life. As I delved into the intricacies of plots and characters, I realized that the worlds of trading, adventure, beauty, fashion, and novels were all interconnected – each providing a unique lens through which to view the tapestry of life.

Throughout this remarkable journey, I learned that ambition without hard work is like a ship without a sail – directionless and adrift. The pursuit of my passions was never without its challenges, but I met each obstacle with determination and a belief in my abilities. The camaraderie I found within communities of traders, adventurers, beauty enthusiasts, fashionistas, and book lovers fueled my perseverance. Their support, coupled with my unwavering self-belief, turned dreams into realities.

""")
with right_column:
    image4 = Image.open(f'{os.getcwd()}/pics/s4.jpg')
    st.image(image4, width=200,use_column_width= 500)


left_column,right_column = st.columns(2)
with left_column:
    image5 = Image.open(f'{os.getcwd()}/pics/serahimage.jpg')
    st.image(image5, width=200,use_column_width= 500)
    
with right_column:
    st.markdown("""

As the chapters of my life continue to unfold, I remain committed to the pursuit of knowledge, the thrill of adventure, the artistry of beauty and fashion, and the enchantment of novels. My journey stands as a testament to the power of embracing one's passions, and the endless possibilities that emerge when ambition meets dedication. From trading floors to mountain peaks, from makeup brushes to the pages of a novel, my life is a symphony of diverse passions harmoniously entwined, creating a melody that resonates with the very essence of who I am.
    
""")
