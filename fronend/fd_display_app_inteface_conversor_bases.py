
import streamlit as st # Import the streamlit library
from backend.conversor_bases import convert # Import the convert function from the conversor_bases.py file

# function verification if input is binaria decimal to binaria
def is_binario_a_decimal(binaria_input):
    if all(char in "01." for char in binaria_input):
        binaria_input = binaria_input.replace(".", "")
        try:
            decimal = int(binaria_input, 2)
            return decimal
        except ValueError:
            return False
    return False


# Function verify if input is octal
def is_octal(octal_input):
    # Verify if input is octal and decimal octal
    if all(char in "01234567." for char in octal_input):
        octal_input = octal_input.replace(".", "")
        try:
           decimal = int(octal_input, 8)
           return decimal
        except ValueError:
           return False
    return False

# function verification if input is hexadecimal and decimal hexadecimal
def is_hexadecimal(hexadecimal_input):
    # Verify if input is hexadecimal and decimal hexadecimal
    if all(char in "0123456789ABCDEFabcdef." for char in hexadecimal_input):
        hexadecimal_input = hexadecimal_input.replace(".", "")
        try:
            decimal = int(hexadecimal_input, 16)
            return decimal
        except ValueError:
            return False
    return False

# Create a function to display the app interface conversor bases
def display_app_inteface_conversor_bases():
    # Add a title
    st.title("Conversor de bases")
    # Add a subtitle and a text
    st.header("Esto es una calculadora de bases numericas decimal,octal,hexadecimal,binaria.")
    # Create tables to display the conversion bases
    tab1, tab2, tab3, tab4= st.tabs(["📈📟 Base decimal", "🧮 Base octal", "⌨️ Base hexadecimal", "🖥 Base binaria"])

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
        decimal_input = st.text_input("Ingresar Numero:", value=0, key=0)

        # If input is string and number not convert to float
        try:
            # Convert input to float
            decimal_input_float = float(decimal_input)

            # Create a button conversion
            if st.button("Calcular", key= 101):
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
                st.subheader(f":green[Conversion Decimal a Binario:] {convert(decimal_input_float,'decimal','binary')}")
                st.subheader(f":green[Conversion Decimal a Octal:] {convert(decimal_input_float,'decimal','octal')}")
                st.subheader(f":green[Conversion Decimal a Hexadecimal:] {convert(decimal_input_float,'decimal','hexadecimal')}")
        except:
            # If input is string and number not convert to float mensaje error
            st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
                text-align: left;
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<h1 class="big-font">Error: Ingrese un numero decimal o entero, sin caracteres string.</h1>', unsafe_allow_html=True)
            # Reset value input
            decimal_input_float = 0

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
        
        # Create a button conversion
        if st.button("Calcular" , key=102):
            # If input is number convert octal
            if is_octal(octal_input):
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
                st.subheader(f":green[Conversion Octal a Decimal:] {convert(octal_input,'octal','decimal')}")
                st.subheader(f":green[Conversion Octal a Binario:] {convert(octal_input,'octal','binary')}")
                st.subheader(f":green[Conversion Octal a Hexadecimal:] {convert(octal_input,'octal','hexadecimal')}")
        else:
            # If input is string and number not convert to float mensaje error
            st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
                text-align: left;
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<h1 class="big-font">Error: Ingrese un numero octal, sin caracteres string.</h1>', unsafe_allow_html=True)
            # Reset value input
            octal_input = 0

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

        # Create a button conversion
        if st.button("Calcular" , key=103):
            # Verify if input is hexadecimal
            if not is_hexadecimal(hexadecimal_input):
                # If input is string and number not convert to float mensaje error
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Error: Ingrese un numero hexadecimal valido.</h1>', unsafe_allow_html=True)
                # Reset value input
                hexadecimal_input = 0
            else:
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
                st.subheader(f":green[Conversion Hexadecimal a Decimal:] {convert(hexadecimal_input,'hexadecimal','decimal')}")
                st.subheader(f":green[Conversion Hexadecimal a Binario:] {convert(hexadecimal_input,'hexadecimal','binary')}")
                st.subheader(f":green[Conversion Hexadecimal a Octal:] {convert(hexadecimal_input,'hexadecimal','octal')}")

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

        # Create a button conversion
        if st.button("Calcular" , key=104):
            # Verify if input is binaria
            if not is_binario_a_decimal(binaria_input):
                # If input is string and number not convert to float mensaje error
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Error: Ingrese un numero estandar, sin caracteres 0 y 1.</h1>', unsafe_allow_html=True)
                # Reset value input
                binaria_input = 0
            else:
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
                st.markdown('<h1 class="big-font">Resultado Conversion Binaria todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases binaria
                st.subheader(f":green[Conversion Binaria a Decimal:] {convert(binaria_input,'binary','decimal')}")
                st.subheader(f":green[Conversion Binaria a Octal:] {convert(binaria_input,'binary','octal')}")
                st.subheader(f":green[Conversion Binaria a Hexadecimal:] {convert(binaria_input,'binary','hexadecimal')}")
                
