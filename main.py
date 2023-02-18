import streamlit as st # Import the streamlit library
from streamlit_option_menu import option_menu # Import the streamlit_option_menu library
from conversor_bases import convert # Import the convert function from the conversor_bases.py file
from ieee754 import decimal_to_bin, decimal_to_hex , bin_to_decimal # Import the decimal_to_bin and decimal_to_hex functions from the ieee754.py file
from graficabise_false import bisection_method, false_position_method,solve_equation

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


# Create a function to display the app interface conversor bases
def display_app_inteface_conversor_bases():
    # Add a title
    st.title("Conversor de bases")
    # Add a subtitle and a text
    st.text("Esto es una calculadora de bases numericas decimal,octal,hexadecimal,binaria.")
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
            st.text(convert(decimal_input_float,"decimal","binary"))
            st.text("Conversion Decimal a Octal")
            st.text(convert(decimal_input_float,"decimal","octal"))
            st.text("Conversion Decimal a Hexadecimal")
            st.text(convert(decimal_input_float,"decimal","hexadecimal"))
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
            st.text("Conversion Octal a Decimal")
            st.text(convert(octal_input,"octal","decimal"))
            st.text("Conversion Octal a Binario")
            st.text(convert(octal_input,"octal","binary"))
            st.text("Conversion Octal a Hexadecimal")
            st.text(convert(octal_input,"octal","hexadecimal"))
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
            st.text("Conversion Binaria a Decimal")
            st.text(convert(binaria_input,"binary","decimal"))
            st.text("Conversion Binaria a Octal")
            st.text(convert(binaria_input,"binary","octal"))
            st.text("Conversion Binaria a Hexadecimal")
            st.text(convert(binaria_input,"binary","hexadecimal"))

# Create a function to display the app interface conversor bases format ieee754
def display_app_inteface_conversor_bases_ieee754():
    # Add a title
    st.title("Conversor Bases IEEE754")
    # Add a subtitle and a text
    st.text("Esto es una calculadora de  simple precisión y doble precisión.")
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
            st.text(f"Signo: {sign}")
            st.text(f"Exponente: {exponent} (decimal: {decimal_exponent})")
            st.text(f"Mantissa: {mantissa} (decimal: {decimal_mantissa_str})")
            st.text(f"Valor decimal equivalente: {decimal_equivalent}")
            st.text(f"Estandar: {sign}{exponent}{mantissa}")
            st.text(f"Hexadecimal: {hex_simple}")

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
            st.text(f"Signo: {sign}")
            st.text(f"Exponente: {exponent} (decimal: {decimal_exponent})")
            st.text(f"Mantissa: {mantissa} (decimal: {decimal_mantissa_str})")
            st.text(f"Valor decimal equivalente: {decimal_equivalent}")
            st.text(f"Estandar: {sign}{exponent}{mantissa}")
            st.text(f"Hexadecimal: {hex_doble}")

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
        
        # Add a text input for binary
        binary_input = st.text_input("Ingresar Numero Estandar:",value=0, key=6)

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
            st.text(f"Signo: {sign}")
            st.text(f"Exponente: {exponent} (decimal: {decimal_exponent})")
            st.text(f"Mantissa: {bin_num} (decimal: {decimal_mantissa_str})")
            st.text(f"Valor decimal equivalente: {round(decimal_equivalent,5)}")
            st.text(f"Hexadecimal: {decimal_to_hex(decimal_equivalent, 'simple')}")
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

        # Add a text input for binary
        binary_input_doble = st.text_input("Ingresar Numero Estandar:",value=0, key=7)

        # Verify if input is binaria
        if not is_binario_a_decimal(binary_input_doble):
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
            (sign, exponent, bin_num, decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent) = bin_to_decimal(binary_input_doble, "doble")
            st.text(f"Signo: {sign}")
            st.text(f"Exponente: {exponent} (decimal: {decimal_exponent})")
            st.text(f"Mantissa: {bin_num} (decimal: {decimal_mantissa_str})")
            st.text(f"Valor decimal equivalente: {round(decimal_equivalent,5)}")
            st.text(f"Hexadecimal: {decimal_to_hex(decimal_equivalent, 'doble')}")

def display_app_inteface_graficarbise_false():

    st.title("Graficar bisecciones y falsas")
    st.text("Esto es una calculadora para graficar ecuaciones con el metodo de biseccion y regla falsa.")

    method = st.selectbox("Selecciona un método", ['Bisection', 'False Position'])
    a = st.number_input("Límite izquierdo", value=-10.0)
    b = st.number_input("Límite derecho", value=10.0)
    tolerance = st.number_input("Tolerancia", value=0.001)

    if st.button("Calcular"):
    # Llamar a la función correspondiente
        if method == 'Bisection':
            root, error, iterations, fig, table = bisection_method(a, b, tolerance)
        elif method == 'False Position':
            root, error, iterations, fig, table = false_position_method(a, b, tolerance)
        else:
            st.error('Método no válido')

    # Mostrar los resultados
        if root is not None:
            st.success(f"Raíz encontrada en {root} con {iterations} iteraciones")
            st.write(f"Error: {error:.3e}")
            st.pyplot(fig)
            st.table(table)
        else:
                st.error("No se encontró la raíz")
 


   
# Create a function to display the app interface home page
def display_home_page():
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

    # add imagen to the app center
    st.image("./images/img.png", use_column_width=True)


# Create a function to display the app interface sidebar menu
def display_app_inteface_sidebar_menu():
    selected = option_menu(
        menu_title="Menu Calculadora",
        options=["Home", "Conversor Bases", "Conversor Bases IEEE754", "Biseyfalse"],
        icons=["house", "bank", "bank2", "bank2"],
        menu_icon="calculator",
        default_index=0,
        orientation="horizontal",
    )
    
    # Display the selected menu item
    if selected == "Home":
        display_home_page()
    elif selected == "Conversor Bases":
        display_app_inteface_conversor_bases()
    elif selected == "Conversor Bases IEEE754":
        display_app_inteface_conversor_bases_ieee754()
    elif selected == "Biseyfalse":
        display_app_inteface_graficarbise_false()
            
# Create a controller displays interface of the app
def display_app_interface():
    display_app_inteface_sidebar_menu()

# Main function
def main():
    display_app_interface()

# Run the main function
main()
