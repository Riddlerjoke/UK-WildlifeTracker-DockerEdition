# la connection avec l'API
import pandas as pd
import requests
import streamlit as st


API_URL = "http://192.168.0.100:8000"  # Utilisez le nom du service du conteneur Docker, pas localhost

# Faire une requête GET à l'API pour obtenir les données de la base de données
response = requests.get(f"{API_URL}/all_species")
data = response.json()
print(data)

# Créer un DataFrame à partir des données
df = pd.DataFrame(data, index=[0])

st.write(df.columns)
