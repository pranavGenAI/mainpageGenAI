import streamlit as st
from streamlit.components.v1 import html


st.set_page_config(page_title="GenAI Demos", layout='wide')


html(
    """
<html>
<head>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/tsparticles/1.18.11/tsparticles.min.js"></script>
   <style>
      #particles {
         width: 100%;
         height: 100vh;
         background-color: #08000e;
      }
   </style>
</head>
<body>
   <div id="particles"></div>
   <script>
      tsParticles.load("particles", {
         particles: {
            number: {
               value: 50
            },
            size: {
               value: 2  // Adjust the particle size here (default is 3)
            },
            move: {
               enable: true,
               speed: 2
            },
            color: {
               value: "#f29fff"
            },
            links: {
               enable: true,
               distance: 150,
               color: "#ffffff",
               opacity: 0.4,
               width: 1
            },
            interactivity: {
               detectsOn: "canvas",
               events: {
                  onHover: {
                     enable: true,
                     mode: "grab"
                  },
                  onClick: {
                     enable: true,
                     mode: "push"
                  }
               },
               modes: {
                  grab: {
                     distance: 200,
                     links: {
                        opacity: 1
                     }
                  },
                  push: {
                     quantity: 4
                  }
               }
            }
         }
      });
   </script>
</body>
</html>
""",
    height=800,
    width=800,
)

# Add CSS to make the iframe fullscreen
st.markdown(
    """
<style>
    iframe {
        position: fixed;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        border: none;
        height: 100%;
        width: 100%;
    }
</style>
""",
    unsafe_allow_html=True,
)



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
                transition: transform 0.5s, filter 0.3s;
            }

            .glow-on-hover:hover {
                transform: scale(1.15);
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
        <a href="https://chatwithbidbooster.streamlit.app/">
            <img src="https://lh3.googleusercontent.com/drive-viewer/AKGpihaiLwB5hnQjwXzS8fm14y2v4-Hq2ZooZG2zqdWCmAk-sF2_h0N_aDpRWHLRkwtVkk0cL_Sq7pAiAhutX2pQQBqtyxmiqVVskQ=s1600-rw-v1" class="glow-on-hover" height=350 width=450>
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <a href="https://bidboosterjpn.streamlit.app/">
            <img src="https://lh3.googleusercontent.com/drive-viewer/AKGpihZu2SSBe5wM3ocA0WfBtlAjR-lwQ2Tn2CZAJaUQnAVjKfT6YeGzcN4cKSwGCwJQ4ImfFHrEOix8t2ul4LecjUh3fD1YURJB3S4=s1600-rw-v1" class="glow-on-hover" height=350 width=450>
        </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <a href="https://datavizanalyst.streamlit.app/">
            <img src="https://lh3.googleusercontent.com/drive-viewer/AKGpihYdnKU3WUMDKWU7-tUvo2Kka73CmAC5f8UGXxHeiPRkJZMtdAp21HDzg998B9nX65OAw2waL5c6qrQ0Vq82Zn4j_OgdzKyH3co=s1600-rw-v1" class="glow-on-hover" height=350 width=450>
        </a>
    """, unsafe_allow_html=True)


st.markdown("")
st.markdown("")
st.markdown("")

col1, col2, col3 = st.columns([1, 1,1])

with col1:
    st.markdown("""
        <a href="https://reportwhiz.streamlit.app/">
            <img src="https://lh3.googleusercontent.com/drive-viewer/AKGpihaq7mmRt5Vm2p1nY6KCdPuuxuEmvXHSVvR4F-UWtUBbW0gN4HyZyPFTlIGkZd2p_yhAca7-m0Z6V75tcb_1eCjM2Ht6qwKWkoo=s1600-rw-v1" class="glow-on-hover" height=350 width=450>
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <a href="https://genaipocs.streamlit.app/">
            <img src="https://lh3.googleusercontent.com/drive-viewer/AKGpihZEExouj3D9lCghjCrKQClfRJByTmfCE2IDpjLm9v2j_Xl3ZQFMjilR99dNpSfvYnpmnxOLQc2i_WattvfwJyhxCQlnsDRPwA=s1600-rw-v1" class="glow-on-hover" height=350 width=450>
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.write("")

 # .stApp > header {
 #        background-color: transparent;
 #    }
 #    .stApp {
 #        background: linear-gradient(45deg, #092035 20%, #0E1117 45%, #0E1117 55%, #3a5683 90%);
 #        animation: my_animation 20s ease infinite;
 #        background-size: 200% 200%;
 #        background-attachment: fixed;
 #    } 
#This code below 

st.markdown('''<style>
   
    @keyframes my_animation {
        0% {background-position: 0% 0%;}
        50% {background-position: 100% 100%;}
        100% {background-position: 0% 0%;}
    }
    [data-testid=stSidebar] {
        background: linear-gradient(360deg, #1a2631 95%, #161d29 10%);
    }
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #c9024b 45%, #ba0158 55%, #cd006d 70%);
        color: white;
        border: none;
    }
    div.stButton > button:hover {
        background: linear-gradient(45deg, #ce026f 45%, #970e79 55%, #6c028d 70%);
        background-color: #ce1126;
    }
    div.stButton > button:active {
        position: relative;
        top: 3px;
    }    
    
</style>''', unsafe_allow_html=True)
