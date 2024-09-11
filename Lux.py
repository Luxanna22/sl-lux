import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

# main
def main():
    st.sidebar.title("Projects")
    page = st.sidebar.selectbox("Choose a project", ["Home", "Graphs", "Lux Bot"])
    if page == "Home":
        home()
    elif page == "Graphs":
        graphs()
    elif page == "Lux Bot":
        chatbot()

def home():
    st.title("Greetings!")
    col1, col2 = st.columns([2, 2]) 
    with col1:
        st.image("https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lux_0.jpg", caption="Lady of Luminosity")
    with col2:
        st.write("\n\n\nI am :blue[Lux]. \n\n\nPlease select a project from the sidebar to get started.")
        st.divider()
        st.subheader("Get in Touch")
        st.write("If you have any questions or need further information, please feel free to contact me.")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<a href='https://www.facebook.com/Lux.SG.22'><img src='https://img.icons8.com/color/48/000000/facebook.png'/></a>Lux Reyes ✨", unsafe_allow_html=True)
        with col2: 
            st.markdown("<a href='tel:+639123456789'><img src='https://img.icons8.com/color/48/000000/phone.png'/></a> +639123456789", unsafe_allow_html=True)            
            
def graphs():
    code = "Console.WriteLine(\"Hello World\");"
    st.title("Ecommerce Customers")
    # st.image("https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lux_0.jpg")
    df = pd.read_excel("Book1.xlsx")
    df = df.drop("Email", axis=1)
    def graphSelect():
        chart_type = st.selectbox("Select Chart Type", ["Select Chart Type","Line Chart", "Bar Chart", "Area Chart"], label_visibility="collapsed")
        if chart_type == "Line Chart":
            st.line_chart(df.set_index('Name'))
        elif chart_type == "Bar Chart": 
            st.bar_chart(df.set_index('Name'))
        elif chart_type == "Area Chart":
            st.area_chart(df.set_index('Name'))
            
    graphSelect()
def get_chatbot_response(query):
    # api_url = "https://hiroshi-api.onrender.com/ai/gpt3?ask=" + query
    # api_url = "https://markdevs-api.onrender.com/gpt4?prompt="+query+"&uid=01012"
    api_url = "https://nash-rest-api-production.up.railway.app/Mixtral?userId=010110&message="+query
    response = requests.get(api_url)
    if response.status_code == 200:
        response_json = response.json()
        if 'response' in response_json:
            ai_response = response_json["response"]
            return ai_response
        else:
            return "Error: API response does not contain a 'response' key"
    else:
        return "Please provide a valid query or try again later"

def chatbot():
    st.title(":rainbow[LUX] BOT")
    with st.form("chat_form"):
        conversation = st.empty()
        st.divider()
        user_input = st.text_input("Enter your query here", placeholder="Enter your query here", autocomplete="off", label_visibility="collapsed")
        send_button = st.form_submit_button("Send",use_container_width=True)
        if send_button:
            if user_input.strip() == "":
                conversation.write(":red[Please enter a valid query!]")
                return
            user_style = "text-align: right; float: right; color: #ffbd79; padding: 1em 10px 10px 10px; background-color: #262730; border-radius: 6px 6px 0 0; width: 100%;"
            bot_style = "text-align: left; float: left; text-color: #FFC300; padding: 0px 10px 1em 10px; background-color: #262730; border-radius: 0 0 6px 6px; width: 100%"
            response = get_chatbot_response(user_input)
            typing_dots = "|"
            for i in range(len(response)):
                conversation.write(f"<div style=\"\"><span style=\"{user_style}\">{user_input}</span><br><br></div><span style=\"{bot_style}\">{response[:i+1]}{typing_dots}</span>", unsafe_allow_html=True)
                time.sleep(0.01)
            conversation.write(f"<div style=\"\"><span style=\"{user_style}\">{user_input}</span><br><br></div><span style=\"{bot_style}\">{response}</span>", unsafe_allow_html=True)
        else:
            conversation.write(f"<span style=\"text-align: left; float: left; text-color: #FFC300; padding: 1em 10px 1em 10px; background-color: #262730; border-radius: 6px; width: 100%\">Greetings! How can I assist you today?</span>", unsafe_allow_html=True)

main()
