import streamlit as st

st.set_page_config(page_title="GenAI Demos", layout='wide')

col1, col2, col3 = st.columns([1, 50, 1])

with col1:
    st.write(' ')

with col2:
    st.image("https://www.vgen.it/wp-content/uploads/2021/04/logo-accenture-ludo.png", width=150)
    st.markdown("")
    st.markdown("")

    st.markdown("""
        <style>
            @keyframes gradientAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .animated-gradient-text {
                font-family: "Graphik Semibold";
                font-size: 42px;
                background: linear-gradient(45deg, rgb(245, 58, 126) 30%, rgb(200, 1, 200) 55%, rgb(197, 45, 243) 20%);
                background-size: 300% 200%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: gradientAnimation 6s ease-in-out infinite;
                color: #FFF;
                transition: color 0.5s, text-shadow 0.5s;
            }

            @keyframes glow {
                0%, 18%, 20%, 50.1%, 60%, 65.1%, 80%, 90.1%, 92% {
                    color: #0e3742;
                    text-shadow: none;
                }
                18.1%, 20.1%, 30%, 50%, 60.1%, 65%, 80.1%, 90%, 92.1%, 100% {
                    color: #fff;
                    text-shadow: 0 0 10px rgb(197, 45, 243), 0 0 20px rgb(197, 45, 243);
                }
            }

            .animated-gradient-text:hover {
                animation: glow 5s linear infinite;
            }

            .glow-on-hover {
                transition: transform 0.3s, filter 0.3s;
            }

            .glow-on-hover:hover {
                transform: scale(1.05);
                filter: drop-shadow(0 0 10px rgba(197, 45, 243, 0.8));
            }
        </style>
        <p class="animated-gradient-text" align="center">
            GN H&PS Generative AI PoCs
        </p>
    """, unsafe_allow_html=True)

with col3:
    st.write(' ')

st.markdown("")
st.markdown("")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("""
        <img src="https://raw.githubusercontent.com/pranavGenAI/mainpageGenAI/bidbooster.png" width="400" class="glow-on-hover">
    """, unsafe_allow_html=True)

with col2:
    st.write("Col2")

with col3:
    st.write("Col3")
