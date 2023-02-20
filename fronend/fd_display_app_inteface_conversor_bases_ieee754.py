import streamlit as st # Import the streamlit library
from backend.ieee754 import decimal_to_bin, decimal_to_hex , bin_to_decimal # Import the decimal_to_bin and decimal_to_hex functions from the ieee754.py file
from fronend.fd_display_app_inteface_conversor_bases import is_binario_a_decimal

# Create a function to display the app interface conversor bases format ieee754
def display_app_inteface_conversor_bases_ieee754():
    # Add a title
    st.title("Conversor Bases IEEE754")
    # Add a subtitle and a text
    st.header("Esto es una calculadora de  simple precisión y doble precisión.")
    # Create tables to display the conversion bases
    tab1, tab2, tab3, tab4 = st.tabs(["📟 Simple precisión", "🖥 Doble precisión","📟 Estandar precisión simple", "🖥 Estandar precisión doble"])

    with tab1:
        # Add text conversion methot simple precision
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Simple Precisión 32bits</h1>', unsafe_allow_html=True)

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
        decimal_input = st.text_input("Ingresar Numero:",value=0, key=4)
        
        # try convert input to float
        try:
            decimal_input_float_simple = float(decimal_input)

            # Create a button convert
            if st.button("Calcular", key=105):
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
                st.markdown('<h1 class="big-font">Resultado Conversion Decimal a Simple Precisión</h1>', unsafe_allow_html=True)
                # conversor bases decimal to simple precision
                (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent) = decimal_to_bin(decimal_input_float_simple, "simple")
                hex_simple = decimal_to_hex(decimal_input_float_simple, "simple")
                st.subheader(f":red[Signo]: {sign}")
                st.subheader(f":violet[Exponente]: {exponent} (decimal: {decimal_exponent})")
                st.subheader(f":orange[Mantissa]: {mantissa} (decimal: {decimal_mantissa_str})")
                st.subheader(f":green[Valor decimal equivalente]: {decimal_equivalent}")
                st.subheader(f":green[Estandar]: :red[signo] :{sign} + :violet[exponente] :{exponent} + :orange[mantissa] :{mantissa}")
                st.subheader(f":green[bits]: {len(sign+exponent+mantissa)}")
                st.subheader(f":green[Hexadecimal]: {hex_simple}")
         

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
            st.markdown('<h1 class="big-font">Error: Ingrese un numero decimal, sin caracteres string.</h1>', unsafe_allow_html=True)
            # Reset value input
            decimal_input = 0    

    with tab2:
        # Add text conversion methot double precision
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Doble Precisión 64bits</h1>', unsafe_allow_html=True)
        
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
        decimal_input = st.text_input("Ingresar Numero:",value=0, key=5)

        # try convert input to float
        try:
            # conversor bases decimal to double precision
            decimal_input_float_doble = float(decimal_input)

            # Create a button convert
            if st.button("Calcular", key=106):
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
                st.markdown('<h1 class="big-font">Resultado Conversion Decimal a Doble Precisión</h1>', unsafe_allow_html=True)
                # conversor bases decimal to double precision
                (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent) = decimal_to_bin(decimal_input_float_doble, "doble")
                hex_doble = decimal_to_hex(decimal_input_float_doble, "doble")
                st.subheader(f":red[Signo]: {sign}")
                st.subheader(f":violet[Exponente]: {exponent} (decimal: {decimal_exponent})")
                st.subheader(f":orange[Mantissa]: {mantissa} (decimal: {decimal_mantissa_str})")
                st.subheader(f":green[Valor decimal equivalente]: {decimal_equivalent}")
                st.subheader(f":green[Estandar]: :red[signo] :{sign} + :violet[exponente] :{exponent} + :orange[mantissa] :{mantissa}")
                st.subheader(f":green[bits]: {len(sign+exponent+mantissa)}")
                st.subheader(f":green[Hexadecimal]: {hex_doble}")

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
            st.markdown('<h1 class="big-font">Error: Ingrese un numero decimal, sin caracteres string.</h1>', unsafe_allow_html=True)
            # Reset value input
            decimal_input = 0

    with tab3:
        # Add text conversion methot binary to decimal
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Estandar a Decimal Presición Simple 32bits:</h1>', unsafe_allow_html=True)

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

        # add form for input binary number simple precision 32bits        
        st.form(key='my_form_32')
        col1, col2 = st.columns(2)
        with col1:
            signo = st.text_input('Signo:', key="signo32")
        with col2:
            exponente = st.text_input('Exponente:', key="exponente32")
        with col1:
            mantissa = st.text_input('Mantissa:', key="mantissa32")

        # Concatenar valores
        binary_input = signo + exponente + mantissa

        # Create a button convert
        if st.button("Calcular", key=107):
            # Verify if input is binaria
            if not is_binario_a_decimal(binary_input):
                # If input is string and number not convert to float mensaje error
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Error: Ingrese un numero Estandar, sin caracteres, 0 y 1 de 32bits.</h1>', unsafe_allow_html=True)
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
                st.markdown('<h1 class="big-font">Resultado Conversion Estandar a Decimal</h1>', unsafe_allow_html=True)
                (sign, exponent, bin_num, decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent) = bin_to_decimal(binary_input, "simple")
                st.subheader(f":red[Signo]: {sign}")
                st.subheader(f":violet[Exponente]: {exponent} (decimal: {decimal_exponent})")
                st.subheader(f":orange[Mantissa]: {bin_num} (decimal: {decimal_mantissa_str})")
                st.subheader(f":green[Valor decimal equivalente]: {round(decimal_equivalent,5)}")
                st.subheader(f":green[Hexadecimal]: {decimal_to_hex(decimal_equivalent, 'simple')}")
    with tab4:
        # Add text conversion methot binary to decimal
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Estandar a Decimal Presición Doble 64bits:</h1>', unsafe_allow_html=True)

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

        # add form for input binary number doble precision 64bits        
        st.form(key='my_form_64')
        col1, col2 = st.columns(2)
        with col1:
            signo = st.text_input('Signo:', key="signo64")
        with col2:
            exponente = st.text_input('Exponente:', key="exponente64")
        with col1:
            mantissa = st.text_input('Mantissa:', key="mantissa64")

        # Concatenar valores
        binary_input = signo + exponente + mantissa

        # Create a button convert
        if st.button("Calcular", key=108):
            # Verify if input is binaria
            if not is_binario_a_decimal(binary_input):
                # If input is string and number not convert to float mensaje error
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Error: Ingrese un numero Estandar, sin caracteres, 0 y 1 de 64bits.</h1>', unsafe_allow_html=True)
                # Reset value input
                binaria_input_doble = 0
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
                st.markdown('<h1 class="big-font">Resultado Conversion Estandar a Decimal Doble</h1>', unsafe_allow_html=True)
                (sign, exponent, bin_num, decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent) = bin_to_decimal(binary_input, "doble")
                st.subheader(f":red[Signo]: {sign}")
                st.subheader(f":violet[Exponente]: {exponent} (decimal: {decimal_exponent})")
                st.subheader(f":orange[Mantissa]: {bin_num} (decimal: {decimal_mantissa_str})")
                st.subheader(f":green[Valor decimal equivalente]: {round(decimal_equivalent,5)}")
                st.subheader(f":green[Hexadecimal]: {decimal_to_hex(decimal_equivalent, 'doble')}")