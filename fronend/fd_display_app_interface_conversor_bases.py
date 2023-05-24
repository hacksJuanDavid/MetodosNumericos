
import streamlit as st  # Import the streamlit library
# Import the convert function from the conversor_bases.py file
from backend.conversor_bases import convert

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
    st.header(
        "Esto es una calculadora de bases numericas decimal,octal,hexadecimal,binaria.")

    # Create tables to display the conversion bases
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📈📟 Base decimal", "🧮 Base octal", "⌨️ Base hexadecimal", "🖥 Base binaria"])

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
        st.markdown('<h1 class="big-font">Conversion Decimal</h1>',
                    unsafe_allow_html=True)
        
        # Instrucciones de uso
        intrucciones_decimal = f'''
            <h3>Para convertir un número decimal a otras bases, sigue estos pasos:</h3>
            <ol>
                <li>Escribe el número decimal que deseas convertir en el input.</li>
                <li>Despues oprime el boton calcular</li>
                <li>Y te retornara los resultados obtenidos en las bases numerica</li>
            </ol>
        '''
        st.sidebar.markdown(intrucciones_decimal, unsafe_allow_html=True)


        # Add a text input for decimal
        # Decimal_input is a variable that is used to store the value entered by the user in the input
        # box.
        decimal_input = st.text_input("Ingresar Numero:", value=0, key=0)

        # If input is string and number not convert to float
        try:
            # Convert input to float
            decimal_input_float = float(decimal_input)

            # Create a button conversion
            if st.button("Calcular", key=101):
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
                st.markdown(
                    '<h1 class="big-font">Resultado Conversion Decimal todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases decimal
                st.text_input(":green[Resultado decimal a binario]:", value=convert(
                    decimal_input_float, 'decimal', 'binary'), key="result_binary_1")
                st.text_input(":green[Resultado decimal a octal:]", value=convert(
                    decimal_input_float, 'decimal', 'octal'), key="result_octal_1")
                st.text_input(":green[Resultado decimal a hexadecimal:]", value=convert(
                    decimal_input_float, 'decimal', 'hexadecimal'), key="result_hexadecimal_1")
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
            st.markdown(
                '<h1 class="big-font">Error: Ingrese un numero decimal o entero, sin caracteres string.</h1>', unsafe_allow_html=True)
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
        st.markdown('<h1 class="big-font">Conversion Octal</h1>',
                    unsafe_allow_html=True)

        # Instrucciones de uso
        intrucciones_octal = f'''
            <h3>Para convertir un número octal a otras bases, sigue estos pasos:</h3>
            <ol>
                <li>Escribe el número octal que deseas convertir en el input.</li>
                <li>Despues oprime el boton calcular</li>
                <li>Y te retornara los resultados obtenidos en las bases numerica</li>
            </ol>
        '''
        st.sidebar.markdown(intrucciones_octal, unsafe_allow_html=True)

        # Add a text input for Octal
        octal_input = st.text_input("Ingresar Numero:", value=0, key=1)

        # Create a button conversion
        if st.button("Calcular", key=102):
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
                st.markdown(
                    '<h1 class="big-font">Resultado Conversion Octal todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases octal
                st.text_input(":green[Resultado octal a decimal]:", value=convert(
                    octal_input, 'octal', 'decimal'), key="result_decimal_1")
                st.text_input(":green[Resultado octal a binario:]", value=convert(
                    octal_input, 'octal', 'binary'), key="result_binary_2")
                st.text_input(":green[Resultado octal a hexadecimal:]", value=convert(
                    octal_input, 'octal', 'hexadecimal'), key="result_hexadecimal_2")
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
            st.markdown(
                '<h1 class="big-font">Error: Ingrese un numero octal, sin caracteres string.</h1>', unsafe_allow_html=True)
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
        st.markdown('<h1 class="big-font">Conversion Hexadecimal</h1>',
                    unsafe_allow_html=True)

        # Instrucciones de uso
        intrucciones_hexadecimal = f'''
            <h3>Para convertir un número hexadecimal a otras bases, sigue estos pasos:</h3>
            <ol>
                <li>Escribe el número hexadecimal que deseas convertir en el input.</li>
                <li>Despues oprime el boton calcular</li>
                <li>Y te retornara los resultados obtenidos en las bases numerica</li>
            </ol>
        '''
        st.sidebar.markdown(intrucciones_hexadecimal, unsafe_allow_html=True)

        # Add a text input for hexadecimal
        hexadecimal_input = st.text_input("Ingresar Numero:", value=0, key=2)

        # Create a button conversion
        if st.button("Calcular", key=103):
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
                st.markdown(
                    '<h1 class="big-font">Error: Ingrese un numero hexadecimal valido.</h1>', unsafe_allow_html=True)
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
                st.markdown(
                    '<h1 class="big-font">Resultado Conversion Hexadecimal todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases hexadecimal
                st.text_input(":green[Resultado hexadecimal a decimal]:", value=convert(
                    hexadecimal_input, 'hexadecimal', 'decimal'), key="result_decimal_2")
                st.text_input(":green[Resultado hexadecimal a octal]:", value=convert(
                    hexadecimal_input, 'hexadecimal', 'octal'), key="result_octal_2")
                st.text_input(":green[Resultado hexadecimal a binario]:", value=convert(
                    hexadecimal_input, 'hexadecimal', 'binary'), key="result_binary_3")

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
        st.markdown('<h1 class="big-font">Conversion Binaria</h1>',
                    unsafe_allow_html=True)

        # Instrucciones de uso
        intrucciones_binaria = f'''
            <h3>Para convertir un número binario a otras bases, sigue estos pasos:</h3>
            <ol>
                <li>Escribe el número binario que deseas convertir en el input.</li>
                <li>Despues oprime el boton calcular</li>
                <li>Y te retornara los resultados obtenidos en las bases numerica</li>
            </ol>
        '''
        st.sidebar.markdown(intrucciones_binaria, unsafe_allow_html=True)

        # Add a text input for binaria
        binaria_input = st.text_input("Ingresar Numero:", value=0, key=3)

        # Create a button conversion
        if st.button("Calcular", key=104):
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
                st.markdown(
                    '<h1 class="big-font">Error: Ingrese un numero estandar, sin caracteres 0 y 1.</h1>', unsafe_allow_html=True)
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
                st.markdown(
                    '<h1 class="big-font">Resultado Conversion Binaria todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases binaria
                st.text_input(":green[Resultado binario a decimal]:", value=convert(
                    binaria_input, 'binary', 'decimal'), key="result_decimal_3")
                st.text_input(":green[Resultado binario a octal]:", value=convert(
                    binaria_input, 'binary', 'octal'), key="result_octal_3")
                st.text_input(":green[Resultado binario a hexadecimal]:", value=convert(
                    binaria_input, 'binary', 'hexadecimal'), key="result_hexadecimal_3")
