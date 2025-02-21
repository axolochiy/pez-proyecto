import http.client
import streamlit as st
st.title("Fish Researcher")
pez=st.text_input("dime un pez")
conn = http.client.HTTPSConnection("fish-species.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "417803d52amsh70b9a59d7a1f2f8p14a948jsn848d9069d72a",
    'x-rapidapi-host': "fish-species.p.rapidapi.com"
}

conn.request("GET", f"/fish_api/fish/{pez}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
st.title(data.decode("utf-8","name"))