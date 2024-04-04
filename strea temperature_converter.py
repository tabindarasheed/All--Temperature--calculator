import streamlit as st

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def main():
    st.title("Temperature Converter")

    option = st.selectbox(
        "Select conversion type",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius")
    )

    if option == "Celsius to Fahrenheit":
        celsius_temp = st.number_input("Enter temperature in Celsius", value=0.0)
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        st.write("Temperature in Fahrenheit:", fahrenheit_temp)

    elif option == "Fahrenheit to Celsius":
        fahrenheit_temp = st.number_input("Enter temperature in Fahrenheit", value=0.0)
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        st.write("Temperature in Celsius:", celsius_temp)

    elif option == "Celsius to Kelvin":
        celsius_temp = st.number_input("Enter temperature in Celsius", value=0.0)
        kelvin_temp = celsius_to_kelvin(celsius_temp)
        st.write("Temperature in Kelvin:", kelvin_temp)

    elif option == "Kelvin to Celsius":
        kelvin_temp = st.number_input("Enter temperature in Kelvin", value=0.0)
        celsius_temp = kelvin_to_celsius(kelvin_temp)
        st.write("Temperature in Celsius:", celsius_temp)

if __name__ == "__main__":
    main()
