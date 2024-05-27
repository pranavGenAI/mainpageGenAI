import streamlit as st
from streamlit.components.v1 import html

# Set Streamlit page configuration
st.set_page_config(page_title="GenAI Demos", layout='wide')

# Define HTML content with canvas-particle-network script
html_content = """
<html>
<head>
   <script src="https://cdn.jsdelivr.net/npm/canvas-particle-network@1.5.0/particle-network.min.js"></script>
   <style>
      body {
         margin: 0;
         overflow: hidden;
         background-color: black;
      }
      canvas {
         position: fixed;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
      }
   </style>
</head>
<body>
   <canvas id="particle-canvas"></canvas>
   <script>
      const particleCanvas = new ParticleNetwork(document.getElementById('particle-canvas'), {
         particleColor: '#ffffff',
         background: 'transparent',
         interactive: true,
         speed: 0.8,
         density: 10000 // Adjust as needed for density of particles
      });
   </script>
</body>
</html>
"""

# Render the HTML content using the html component
html(html_content, unsafe_allow_html=True)

# Add Streamlit elements below
st.title("GenAI Demos")
st.write("Explore our interactive demos!")

# Add your additional Streamlit content as needed
# Example: Buttons, images, text, etc.
st.button("Click me")

# Styling adjustments if necessary
st.markdown("""
<style>
    .stButton > button {
        background-color: #ce026f;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #970e79;
    }
</style>
""", unsafe_allow_html=True)
