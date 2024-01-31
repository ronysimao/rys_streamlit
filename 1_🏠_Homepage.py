import streamlit as st

st.set_page_config(
    page_title="Multipage",
    page_icon="👋",
)

st.title('Main Page')
st.sidebar.success('Selecione a demonstração acima.')

if "my_input" not in st.session_state:
    st.session_state["my_input"] = "Hello"

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit", type="primary")

if submit:
    st.session_state["my_input"] = my_input
    st.write("You :sunglasses: have enterede: ", my_input)