import streamlit as st
from PIL import Image
bigImage = Image.open("streamfeldpic.png")
image = bigImage.resize((250, 250))
st.image(image, caption='', use_column_width=False)


st.title("Streamfeld")
st.divider()
kramer_episodes = "'The Voice' (S9 E2), 'The Pool Guy' (S7 E8), 'The Muffin Tops' (S8 E21), 'The Butter Shave' (S9 E1), or 'The Merv Griffin Show' (S9 E6)."

george_episodes = "'The Marine Biologst' (S5 E14), 'The Opposite' (S5 E22), 'The Serenity Now' (S9 E3), 'The Abstinence' (S8 E9), or 'The Bubble Boy' (S4 E7)."

jerry_episodes = "'The Puffy Shirt' (S5 E2), 'The Rye' (S7 E11), 'The Keys' (S2 E23), 'The Soup' (S6 E7), or 'The Cafe' (S3 E7)."

elaine_episodes = "'The Soup Nazi' (S7 E9), 'The Pen' (S3 E3), 'The Little Kicks' (S8 E4), 'The Sponge' (S7 E9), or 'The Stall' (S5 E12)."

newman_episodes = "'The Bottle Deposit' (S7 E20), 'The Package' (S8 E5), 'The Engagement' (S7 E1), 'The Boyfriend' (S3 E17), or 'The Ticket' (S4 E4)."
prompt = f'Which Seinfeld character is your favorite: Kramer, George, Jerry, Elaine, or Newman? Enter Q to stop receiving episode recommendations: '
character = st.text_input(prompt)

if character == "Kramer":
    st.write("You should watch", kramer_episodes)
if character == "George": 
    st.write("You should watch", george_episodes)
if character == "Jerry":
    st.write("You should watch", jerry_episodes)
if character == "Elaine":
    st.write("You should watch", elaine_episodes)
if character == "Newman":
    st.write("You should watch", newman_episodes)
print("Enjoy watching!")
