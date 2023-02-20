import streamlit as st # Import the streamlit library
from streamlit_option_menu import option_menu # Import the streamlit_option_menu library
from fronend.fd_display_app_inteface_conversor_bases import display_app_inteface_conversor_bases # Import the display_app_inteface_conversor_bases function from the fd_display_app_inteface_conversor_bases.py file
from fronend.fd_display_app_inteface_conversor_bases_ieee754 import display_app_inteface_conversor_bases_ieee754 # Import the display_app_inteface_conversor_bases_ieee754 function from the fd_display_app_inteface_conversor_bases_ieee754.py file
from fronend.fd_display_app_inteface_graficarbise_false import display_app_inteface_graficarbise_false # Import the display_app_inteface_graficarbise_false function from the fd_display_app_inteface_graficarbise_false.py file
from fronend.fd_display_home_page import display_home_page # Import the display_home_page function from the fd_display_home_page.py file
from fronend.fd_display_app_interface_logo import display_app_interface_logo # Import the display_app_interface_logo function from the fd_display_app_interface_logo.py file

# Create a function to display the app interface sidebar menu
def display_app_inteface_sidebar_menu():
    # Display the app interface logo
    display_app_interface_logo()
    
    # Create a sidebar menu
    selected = option_menu(
        menu_title="Menu Calculadora",
        options=["Home", "Conversor Bases", "Conversor Bases IEEE754", "Biseccion y regal falsa"],
        icons=["house", "bank", "align-center", "bar-chart-line"],
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
    elif selected == "Biseccion y regal falsa":
        display_app_inteface_graficarbise_false()
            
# Create a controller displays interface of the app
def display_app_interface():
    display_app_inteface_sidebar_menu()

# Main function
def main():
    display_app_interface()

# Run the main function
main()
