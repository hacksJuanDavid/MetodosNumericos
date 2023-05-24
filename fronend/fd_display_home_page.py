import base64
import io
import streamlit as st  # Import the streamlit library
from PIL import Image
# Create a function to display the app interface home page


def display_home_page():
    # add a title to the app
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
        text-align: center;
        color: #ffffff;
        margin: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h1 class="big-font">Core73🕵🏼</h1>', unsafe_allow_html=True)

    # add a subtitle to the app
    st.markdown("""
    <style>
    .medium-font {
        font-size:30px !important;
        text-align: center;
        color: #ffffff;
        margin: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h2 class="medium-font">CALULADORA METODOS NUMERICOS</h2>', unsafe_allow_html=True)
    
    # add lista integrantes
    st.markdown("""
    <style>
    .medium-font {
        font-size:20px !important;
        text-align: center;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h3 class="medium-font">Integrantes:</h3>', unsafe_allow_html=True)
    st.markdown('<h5 class="medium-font">- Juan David Jimenez</h5>', unsafe_allow_html=True)
    st.markdown('<h5 class="medium-font">- Santiago Restrepo</h5>', unsafe_allow_html=True)
    st.markdown('<h5 class="medium-font">- Andres Abadia</h5>', unsafe_allow_html=True)

    # Cargar la imagen de
    image = Image.open("images/img.png")

    # Convertir la imagen en un búfer de bytes
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")

    # Obtener el contenido de la imagen en base64
    b64_img = base64.b64encode(buffer.getvalue()).decode()

    # Crear el fragmento HTML para la imagen centrada
    img_logo_jjj = f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/jpeg;base64,{b64_img}" width="700" alt="Imagen de la juguetería">
    </div>
    """

    # Mostrar el fragmento HTML en la página
    st.markdown(img_logo_jjj, unsafe_allow_html=True)
