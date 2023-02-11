import streamlit as st # Import the streamlit library
from conversor_bases import convert # Import the convert function from the conversor_bases.py file

# Create a function to display the app interface conversor bases
def display_app_inteface_conversor_bases():
    # add a title to the app
    st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;
        text-align: center;
        color: #000000;
        
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h1 class="big-font">Metodos Númericos 🕵🏼</h1>',unsafe_allow_html=True)

    # Add a title
    st.title("Conversor de bases")
    # Add a subtitle and a text
    st.text("Esto es una calculadora de bases numericas decimal,octal,hexadecimal,binaria.")
    # Create tables to display the conversion bases
    tab1, tab2, tab3, tab4= st.tabs(["📈📟 base decimal", "🧮 base octal", "⌨️ base hexadecimal", "🖥 base binaria"])

    with tab1:
        # Add text conversion methot
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Decimal</h1>', unsafe_allow_html=True)

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #000000;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # Add a text input for decimal
        # Decimal_input is a variable that is used to store the value entered by the user in the input
        # box.
        decimal_input = st.number_input("Ingresar Numero:", value=0, key=0)

        # Add text result conversion
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Resultado Conversion Decimal todas las bases</h1>', unsafe_allow_html=True)
        # conversor bases decimal
        st.text("Conversion Decimal a Binario")
        st.text(convert(decimal_input,"decimal","binary"))
        st.text("Conversion Decimal a Octal")
        st.text(convert(decimal_input,"decimal","octal"))
        st.text("Conversion Decimal a Hexadecimal")
        st.text(convert(decimal_input,"decimal","hexadecimal"))

    with tab2:
        # Add text conversion methot
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Octal</h1>', unsafe_allow_html=True)

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #000000;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # Add a text input for Octal
        octal_input = st.text_input("Ingresar Numero:", value=0 ,key=1)
        # Add text result conversion
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Resultado Conversion Octal todas las bases</h1>', unsafe_allow_html=True)
        # conversor bases octal
        st.text("Conversion Octal a Decimal")
        st.text(convert(octal_input,"octal","decimal"))
        st.text("Conversion Octal a Binario")
        st.text(convert(octal_input,"octal","binary"))
        st.text("Conversion Octal a Hexadecimal")
        st.text(convert(octal_input,"octal","hexadecimal"))
        


    with tab3:
        # Add text conversion methot
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Hexadecimal</h1>', unsafe_allow_html=True)

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #000000;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # Add a text input for hexadecimal
        hexadecimal_input = st.text_input("Ingresar Numero:", value=0 ,key=2)
        # Add text result conversion
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Resultado Conversion Hexadecimal todas las bases</h1>', unsafe_allow_html=True)
        # conversor bases hexadecimal
        st.text("Conversion Hexadecimal a Decimal")
        st.text(convert(hexadecimal_input,"hexadecimal","decimal"))
        st.text("Conversion Hexadecimal a Octal")
        st.text(convert(hexadecimal_input,"hexadecimal","octal"))
        st.text("Conversion Hexadecimal a Binario")
        st.text(convert(hexadecimal_input,"hexadecimal","binary"))

    with tab4:
        # Add text conversion methot
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Binaria</h1>', unsafe_allow_html=True)

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #000000;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # Add a text input for binaria
        binaria_input = st.text_input("Ingresar Numero:",value=0, key=3)
        # Add text result conversion
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Resultado Conversion Binaria a Decimal</h1>', unsafe_allow_html=True)
        # conversor bases binaria
        st.text("Conversion Binaria a Decimal")
        st.text(convert(binaria_input,"binary","decimal"))
        st.text("Conversion Binaria a Octal")
        st.text(convert(binaria_input,"binary","octal"))
        st.text("Conversion Binaria a Hexadecimal")
        st.text(convert(binaria_input,"binary","hexadecimal"))
    


# Create a function to display the app interface sidebar menu
def display_app_inteface_sidebar_menu():
    # sidebar menu
    st.sidebar.title("Menu Calculadora")
    st.sidebar.text("Metodos Númericos")


# Create a controller displays interface of the app
def display_app_interface():
    display_app_inteface_conversor_bases()
    display_app_inteface_sidebar_menu()


# Main function
def main():
    display_app_interface()

# Run the main function
main()
