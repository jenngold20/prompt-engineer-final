import pathlib
import streamlit as st
import textwrap

#pip install streamlit
#pip install IPython
#pip install google-generativeai

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown



def to_markdown(text):
  text= text.replace('•', ' *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY= ''


genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model= genai.GenerativeModel('gemini-1.0-pro')


def consulta(context, prompt):
     response = model.generate_content(context + prompt)
     archivo = response.text
     with open('archivo.txt', 'w') as f:
         f.write(archivo)

     return response.text
  

# Titulo de la aplicación

st.title("Consultorio Online")

#Texto de introducción

st.write("Bienvenido al consultorio online, aquí podras consultar con el modelo GEMINI, un asistente virtual que te ayudara a aprender mas sobre lo que quieras.")

#Entrada del prompt del usuario
prompt = st.text_area("Escribe tu estado de ánimo en una sola palabra aquí ")

context= "Eres un especialista analizando personas. Quiero que te comportes como un analista de estados de ánimo y que puedas dar un consejo que pueda dar calma, animo, fuerza o consuelo, segun corresponda. El estado de sensacion que quiero que anlaices es:"

#Boton para mostrar el nombre:

if st.button("Analiza"):
    if prompt:
        #llamar a la api y obtener respuesta
        response = consulta(context, prompt)
        #visualizar respuesta
        st.write(response)
    else:
        st.write("Por favor, escribe una prompt")