import streamlit as st # Import the streamlit library
from streamlit_option_menu import option_menu # Import the streamlit_option_menu library
from fronend.fd_display_app_interface_conversor_bases import display_app_inteface_conversor_bases # Import the display_app_inteface_conversor_bases function from the fd_display_app_inteface_conversor_bases.py file
from fronend.fd_display_app_interface_conversor_bases_ieee754 import display_app_inteface_conversor_bases_ieee754 # Import the display_app_inteface_conversor_bases_ieee754 function from the fd_display_app_inteface_conversor_bases_ieee754.py file
from fronend.fd_display_app_interface_graficarbise_false import display_app_inteface_graficarbise_false # Import the display_app_inteface_graficarbise_false function from the fd_display_app_inteface_graficarbise_false.py file
from fronend.fd_display_home_page import display_home_page # Import the display_home_page function from the fd_display_home_page.py file
from fronend.fd_display_app_interface_logo import display_app_interface_logo # Import the display_app_interface_logo function from the fd_display_app_interface_logo.py file
from fronend.fd_display_app_interface_m_secante import display_m_secante # Import the display_m_secante function from the fd_display_app_interface_m_secante.py file
from fronend.fd_display_app_interface_derivative_calculator import display_derivative_calculator # Import the display_derivative_calculator function from the fd_display_app_interface_derivative_calculator.py file
from fronend.fd_display_app_interface_raicesPolinomios import display_raicesPolinomios # Import the display_raicesPolinomios function from the fd_display_app_interface_raicesPolinomios.py file
from fronend.fd_display_app_interface_newton_raphson import display_newtonRaphson # Import the display_newtonRaphson function from the fd_display_app_interface_newton_raphson.py file


# Create a function to display the app interface sidebar menu
def display_app_inteface_sidebar_menu():
    # Display the app interface logo
    display_app_interface_logo()
    
    # Create a sidebar menu
    selected = option_menu(
        menu_title="Menu Calculadora",
        options=["Home", "Conversor Bases", "Conversor Bases IEEE754", "Biseccion y regla falsa","Método de la secante", "Derivadas", "Raices de polinomios","Newton Raphson"],
        icons=["house", "bank", "align-center", "bar-chart-line", "bar-chart-line"],
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
    elif selected == "Biseccion y regla falsa":
        display_app_inteface_graficarbise_false()
    elif selected == "Método de la secante":
        display_m_secante() 
    elif selected == "Derivadas":
        display_derivative_calculator()
    elif selected == "Raices de polinomios":
        display_raicesPolinomios()
    elif selected == "Newton Raphson":
        display_newtonRaphson()    
            
# Create a controller displays interface of the app
def display_app_interface():
    display_app_inteface_sidebar_menu()

# Main function
def main():
    display_app_interface()

# Run the main function
main()
