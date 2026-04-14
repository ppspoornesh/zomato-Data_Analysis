import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import base64
import difflib
import re
from collections import Counter
from itertools import combinations
from streamlit_lottie import st_lottie
import requests

df = pd.read_csv(r"https://raw.githubusercontent.com/navinds/Zomato-Data-Analysis-and-Visualization/main/datasets/cleaned_final_df.csv")
# Get the list of unique cuisines from your DataFrame

# Set page title and favicon
st.set_page_config(page_title="Fine Dine-Zomato Restaurants Data App",layout="wide", page_icon="https://raw.githubusercontent.com/navinds/Zomato-Data-Analysis-and-Visualization/main/Media/finedine_favicon.png",)
violet_color = "#6F36AD"

#st.markdown("<div style='text-align:center'><a href='https://postimg.cc/VrCzqwSm'><img src='https://i.postimg.cc/VktZcrtg/Navin-s-Pulse-Vision-NEW-resize.png' alt='pulse-2.webp'/></a></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center'><img src='https://raw.githubusercontent.com/navinds/Zomato-Data-Analysis-and-Visualization/main/Media/finedine_logo.png' style='width: 500px;'/></div>", unsafe_allow_html=True)

selected = option_menu("",
                       options=["HOME", "INSIGHTS","REPORT","ABOUT"],
                       icons=["house", "bar-chart", "file-text", "info-circle"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"container": {"width": "100%","border": "1px ridge #ef4f5f","background-color": "#0E1117"},  # Adjust width to make it smaller
                               "icon": {"color": "#E33745", "font-size": "20px"},  # Adjust icon size and color
                               "nav-link": {"font-family": "**Helvetica**", "font-size": "20px", "text-align": "center", "color": "#FFFFFF"},  # Adjust font size and alignment
                               "nav-link-selected": {"background-color": "#FFFFFF", "color": "#E33745"}}) 


# Function to load Lottie files from a URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
st.markdown("""
        <style>
               .block-container {
                    padding-top: 3rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)
if selected == "HOME":
    
    @st.cache_data 
    def home_page():
 
        st.markdown("""
        <div style='text-align:center'>
            <img src='https://raw.githubusercontent.com/navinds/Zomato-Data-Analysis-and-Visualization/main/Media/Greyscale%20Illustrative%20Project%20Overview%20Mind%20Map%20(Website).svg' alt='Step 1: Load the Data' style='width: 1350px;'/>
        </div>
        """, unsafe_allow_html=True)        
            
        st.markdown("")
        st.markdown("")
        st.markdown("<h1 style='color:#EF4F5F; display: inline;'> Welcome to Fine Dine</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color:black; display: inline;'>Unveiling India's Food Landscape: Insights from Zomato</h1>", unsafe_allow_html=True)
        home_col1,home_col2 = st.columns(2)
        with home_col1:
            
            st.title("")
            st.title("")
            st.markdown("<h2 style='color:#EF4F5F'>What is Fine Dine?</h2>", unsafe_allow_html=True)
            st.write(" Fine Dine is an app designed to help people explore and understand the diverse world of Indian cuisine. Using data from Zomato, it offers insights into various aspects, from city-level specifics to nationwide trends. Fine Dine aims to help users make better dining choices and assisting new or existing restaurant owners in improving strategies & offerings.")


        with home_col2:
            home_lottie_url = "https://lottie.host/26208437-09a6-44d5-b727-71b7fa0bb840/ZfL194fvPv.json"  # Replace with your Lottie file URL
                # Load the Lottie animation
            home_lottie_animation = load_lottie_url(home_lottie_url)
            st_lottie(home_lottie_animation, width=500, height=500,quality= 'medium')            
        
        home_col3,home_col4 = st.columns(2)
        with home_col3:
            explore_url = "https://lottie.host/e0b8a386-c9ea-4042-a9b8-ed63bec5f371/TF196S2MpR.json"  # Replace with your Lottie file URL

                # Load the Lottie animation
            explore_lottie_animation = load_lottie_url(explore_url)
            st_lottie(explore_lottie_animation, width=500, height=500,quality= 'medium')            
        with home_col4:            
            st.title("")
            st.title("")
            st.title("")
            st.markdown("<h1 style='color:#EF4F5F; display: inline;'>Discover by City or Nation</h1>", unsafe_allow_html=True)
            st.subheader("City Exploration:")
            st.write("Dive into the tastes of India's cities.")
            st.subheader("Nationwide Insights:")
            st.write("Get a taste of the entire country.")
        html1_string = """
        <style>
        .gif-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .gif-container img {
            width: 100;
            height: 100px;
        }
        </style>

        <div class="gif-container">
        <img src="https://raw.githubusercontent.com/navinds/Zomato-Data-Analysis-and-Visualization/main/Media/top_options.gif" alt="Alt Text">
        </div>
        """
        st.markdown(html1_string, unsafe_allow_html=True)    
        home_col5,home_col6 = st.columns(2)          
        with home_col5:
            st.title("")
            st.title("")
            st.markdown("<h2 style='color:#EF4F5F; display: inline;'>City Insights:</h2>", unsafe_allow_html=True)
            st.markdown("""
            - **Explore Cuisines:** Sample a variety of flavors without any specific cravings.
            - **Find Specific Cuisines:** Instantly locate and explore your favorite dishes.
            - **Cuisine Analysis:** Use filters to find the best cuisines based on popularity and value.
            - **Locality Ratings:** Discover top-rated dining spots in each city's neighborhoods.
            - **Cost vs Ratings:** See how restaurant ratings relate to different price ranges.
            """)
        
        with home_col6:
            city_explore_url = "https://lottie.host/12391662-2feb-4549-a4fa-825dcf427db8/VIGSC0W9wD.json"  # Replace with your Lottie file URL

                # Load the Lottie animation
            city_explore_animation = load_lottie_url(city_explore_url)
            st_lottie(city_explore_animation, width=400, height=400,quality= 'medium')

        # Nationwide Highlights
        home_col7,home_col8 = st.columns(2)   
        with home_col7:
            nation_explore_url = "https://lottie.host/8087f44a-3ade-4095-9455-4733a6ef1a3c/kYmsjGaWrK.json" 

                # Load the Lottie animation
            nation_explore_ani = load_lottie_url(nation_explore_url)
            st_lottie(nation_explore_ani, width=600, height=300,quality= 'medium')
        with home_col8:
            st.markdown("<h2 style='color:#EF4F5F; display: inline;'>Nationwide Highlights:</h2>", unsafe_allow_html=True)
            st.markdown("""
            - **Top Restaurants:** Uncover India's highest-rated dining destinations.
            - **Popular Cuisines:** Explore beloved dishes from across the nation.
            - **Search for Cuisines:** Find and learn about any cuisine with ease.
            - **Cuisine Filters:** Customize your cuisine preferences based on ratings and costs.
            - **Cost vs Ratings:** Make informed decisions by understanding how ratings vary with prices.
            - **Popular Pairings:** Discover favorite cuisine combinations loved by food enthusiasts everywhere.
            """)

        
        st.markdown("<h2 style='color:#EF4F5F; display: inline;'>How This App Will Be Helpful:</h2>", unsafe_allow_html=True) 
        html_string = """
        <style>
        .gif-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .gif-container img {
            width: 100;
            height: 100px;
        }
        </style>

        <div class="gif-container">
        <img src="https://raw.githubusercontent.com/navinds/Zomato-Data-Analysis-and-Visualization/main/Media/designed_for_whome__.gif" alt="Alt Text">
        </div>
        """
        st.markdown(html_string, unsafe_allow_html=True)         
        st.write("""
        1. **Comprehensive City-Wise Analysis:** Get detailed insights into the restaurant landscape of individual cities. Explore a wide variety of cuisines, understand dining trends, and make informed decisions based on ratings, costs, and locality analyses.

        2. **Discover Top Restaurants Across India:** Curated lists of the highest-rated restaurants across India help food enthusiasts and travelers discover the best dining spots nationwide, ensuring top-notch culinary experiences.

        3. **Filter and Analyze Specific Cuisines:** Search for specific cuisines and analyze various aspects such as popularity, cost-effectiveness, and user ratings. Find the best low-cost options or the highest-rated luxury dining experiences with ease.

        4. **Cost vs. Ratings Insights:** Compare restaurant costs with user ratings to make cost-effective dining choices without compromising on quality, ensuring the best value for your money.

        5. **Identify Popular Cuisine Combinations:** Discover new and interesting food pairings by analyzing data on popular cuisine combinations frequently paired together in restaurants.
        
        6. **Cuisine Comparison:** Utilize the "Cuisine Comparison" feature to compare two cuisines based on price range and rating distribution. This allows users to make informed decisions by understanding how different cuisines stack up against each other in terms of affordability and popularity.

        7. **User-Friendly Interface:** The app's intuitive and easy-to-use interface makes it accessible to users of all tech proficiency levels, ensuring a smooth and enjoyable experience while navigating through the data.

        8. **Customizable Analysis:** Users can customize their analysis by applying various filters and criteria to focus on specific aspects of the data that matter most to them, such as price ranges, rating thresholds, and cuisine types.

        9. **Enhanced Decision-Making:** By providing a wealth of data-driven insights, the app helps users make well-informed dining decisions, whether they are looking for budget-friendly options, highly rated spots, or specific cuisine types.

        10. **Supports Local Businesses:** By highlighting top-rated and popular local restaurants, the app supports local businesses and helps users discover hidden culinary gems in their area.

        11. **Travel Planning:** For travelers, the app provides valuable information about dining options in different cities, helping them plan their culinary adventures more effectively and enjoy the best food experiences during their trips.

        12. **Data-Driven Insights for Restaurant Owners:** Restaurant owners can use the app to gain insights into competitor performance, customer preferences, and emerging dining trends, helping them improve their offerings and strategies.

        13. **Health-Conscious Dining:** Users can filter and find restaurants offering healthy dining options, catering to those who are mindful of their diet and nutritional intake.

        """)
        # Food order
        st.markdown("<h2 style='color:#EF4F5F; display: inline;'>Order Food:</h2>", unsafe_allow_html=True)    
        st.write("Order delicious food now from Zomato!")
        food_order_lottie_url = "https://lottie.host/93869b46-57f4-43c9-ab4d-2dd7a9e7b7f5/slnPxoFZAp.json"  # Replace with your Lottie file URL

            # Load the Lottie animation
        lottie_animation = load_lottie_url(food_order_lottie_url)
        st_lottie(lottie_animation, width=250, height=250,quality= 'medium')
        col1, col2 = st.columns([0.08,1.5])
        with col2:
            st.link_button("Order Now","https://www.zomato.com/")
        

    home_page()               

if selected == "ABOUT" :
    @st.cache_data 
    def about_page():
        # Title
        st.title("About the Fine Dine Project")

        # Introduction
        st.write("""
        Welcome to the **Fine Dine Project**. This project is designed to provide insightful analysis of restaurant data across India, leveraging data scraped from the Zomato website. Whether you are a food enthusiast, a data science professional, or someone interested in dining trends, this app offers valuable insights for everyone.
        """)

        # Project Objectives
        st.markdown("<h2 style='color:#EF4F5F; display: inline;'>Project Objectives:</h2>", unsafe_allow_html=True)    
        st.write("""
        The Fine Dine project aims to achieve the following objectives:
        1. **Comprehensive Data Analysis**: To perform an extensive analysis of restaurant data, encompassing various metrics such as cuisines, ratings, costs,and locations at both city and national levels.
        2. **Enhanced Decision-Making**: To provide users with actionable insights that can help them make informed dining decisions based on their preferences and budget.
        3. **User-Friendly Experience**: To create an intuitive and interactive platform using Streamlit that allows users to explore restaurant data effortlessly.
        4. **Identifying Trends**: To uncover dining trends and patterns across different cities and nationwide, highlighting popular cuisines, cost-effective dining options, and high-rated localities.
        5. **Promoting Data Literacy**: To demonstrate the power of data science and web scraping in extracting and analyzing real-world data, encouraging users to explore these techniques.
        6. **Culinary Exploration**: To assist users in discovering new and diverse culinary experiences by providing detailed information on various cuisines and their popularity.
        """)

        # Data Collection
        st.markdown("<h2 style='color:#EF4F5F; display: inline;'>Data Collection:</h2>", unsafe_allow_html=True)    
        st.write("""
        The data for this project was collected from the Zomato website using advanced web scraping techniques. The tools and technologies used include:
        - **Selenium:** Used for automated browsing and interaction with the Zomato website.
        - **BeautifulSoup:** Employed for parsing HTML content and extracting relevant data.

        The scraped data encompasses a wide range of information, including restaurant names, locations, cuisines, ratings, and costs.
        """)


        # Features of the App
        st.markdown("<h2 style='color:#EF4F5F; display: inline;'>Features of the App:</h2>", unsafe_allow_html=True)    
        st.write("""
        The Fine Dine app offers a variety of features, categorized into City-Wise Analysis and Total India Analysis:

        **City-Wise Analysis**:
        - Explore and search for specific cuisines.
        - Analyze cuisines with multiple filters.
        - Discover top-rated localities.
        - Understand the relationship between cost and ratings.

        **Total India Analysis**:
        - Find top restaurants across India.
        - Discover popular cuisines nationwide.
        - Use filters to analyze cuisines by ratings and costs.
        - Explore popular cuisine combinations.
        """)
        # Technologies Used
        st.markdown("<h2 style='color:#EF4F5F; display: inline;'>Technologies Used:</h2>", unsafe_allow_html=True)    
        st.write("""
        The Fine Dine project was developed using the following technologies:
        - **Python:** The primary programming language used for data scraping, analysis, and app development.
        - **Selenium:** For web scraping and automated browsing.
        - **BeautifulSoup:** For parsing HTML and extracting data.
        - **Pandas:** For data manipulation and analysis.
        - **Streamlit:** For creating an interactive web application.

        These technologies provide a robust platform for collecting, analyzing, and visualizing restaurant data.
        """)
        st.markdown("<h2 style='color:#EF4F5F; display: inline;'>About Me:</h2>", unsafe_allow_html=True)    
        st.markdown("""
            Hi, I'm Navin, deeply passionate about the sea of data science and AI. 
            My goal is to become a skilled data scientist.

            Beyond the lines of code, my aim is to innovate and be a part of transformative technological evolution. 
            The world needs solutions that not only solve problems but redefine them. 
            I'm here to create change.
        """)

        # LinkedIn link with logo
        st.markdown("<h2 style='color:#EF4F5F; display: inline;'>Connect with Me:</h2>", unsafe_allow_html=True)    
        col1, col2 = st.columns([1,20])
           
        with col1:  
            
            linkedin_logo = "https://img.icons8.com/fluent/48/000000/linkedin.png"  
            linkedin_url = "https://www.linkedin.com/in/navinkumarsofficial/"  
            st.markdown(f"[![LinkedIn]({linkedin_logo})]({linkedin_url})")
        with col2:
            # Email with logo
            email_logo = "https://img.icons8.com/fluent/48/000000/email.png"  
            your_email = "https://mail.google.com/mail/?view=cm&source=mailto&to=navinofficial1@gmail.com"
            st.markdown(f"[![Email]({email_logo})]({your_email})")
    about_page()

if selected == "INSIGHTS" :
    filter_container1 =  st.container(border = True) 
    type_selection = filter_container1.radio('Category Selection',["**City-Wise**","**India-Wise**"], index = None)

    if type_selection == "**City-Wise**":

        city_wise_type_selection = filter_container1.radio('City-Wise Category Selection',["**Explore All Cuisines**","**Search for Specific Cuisine**","**Cuisine Analyzer**","**Compare Cuisines**","**Locality Analyzer**","**Cost Vs Ratings**"],index = None)
        with filter_container1.popover("Confused! Click Me"):
            st.write(f"<span style='color:#ef4f5f'>Explore All Cuisines =></span> This option allows you to explore a wide variety of cuisines without any specific preferences in mind.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Search for Specific Cuisine =></span> You can search for and analyze a particular cuisine they have in mind by typing its name directly.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Cuisines Analyzer =></span> This feature has many filters that helps you analyze different aspects of cuisines, such as popularity, best low cost cuisines, worst expensive cuisines ,to make informed decisions on cuisines.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Locality Analyzer =></span> This option helps you discover the top-rated localities in a city by calculating the average rating of all the restaurants in each locality.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Cost Vs Ratings =></span> This option helps you understand how dining ratings vary with different price categories, enabling them to make informed decisions based on their budget and desired dining experience.", unsafe_allow_html=True)
        st.write("You selected:", f"<span style='color:#ef4f5f'>{type_selection} => {city_wise_type_selection}</span>", unsafe_allow_html=True)
        if not city_wise_type_selection:
            # URL of the Lottie animation
            lottie_url = "https://lottie.host/12391662-2feb-4549-a4fa-825dcf427db8/VIGSC0W9wD.json"  

            # Load the Lottie animation
            lottie_animation = load_lottie_url(lottie_url)

            # Create three columns
            col1, col2, col3 = st.columns([1,0.75, 1])
            with col2:
                st_lottie(lottie_animation, width=250, height=250,quality= 'medium')

        if city_wise_type_selection == "**Explore All Cuisines**":
            # html_string = """
            # <style>
            # .gif-container {
            #     display: flex;
            #     justify-content: center;
            #     align-items: center;
            # }
            # .gif-container img {
            #     width: 200;
            #     height: 200px;
            # }
            # </style>

            # <div class="gif-container">
            # <img src="https://media.giphy.com/media/gACu73U4S2BPws20b0/giphy.gif?cid=790b7611kxephkx8z0sgx69ikbizyizav7k34mzphptys3i7&ep=v1_stickers_search&rid=giphy.gif&ct=s" alt="Alt Text">
            # </div>
            # """

            # st.markdown(html_string, unsafe_allow_html=True)  
             # URL of the Lottie animation
            lottie_url = "https://lottie.host/725d461a-b729-435e-aa8f-895cac6c660b/JZf13khNON.json" 

            # Load the Lottie animation
            lottie_animation = load_lottie_url(lottie_url)

            # Create three columns
            col1, col2, col3 = st.columns([1,0.75, 1])
            with col2:
                st_lottie(lottie_animation, width=250, height=250,quality= 'medium')           
            
            
            def ins_tab1_fn():

                def top_query(selected_city,price,dine_rating):
                    top_query2 = df.loc[(df["City"]== selected_city )&(df["Dining_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Dining_Votes", ascending=False).head(20)
                    top_query_2_all =df.loc[(df["City"]== selected_city )&(df["Dining_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Dining_Votes", ascending=False)
                    if selected_city and price and dine_rating:        
                        # outer if
                        if top_query2.shape[0] == 0:
                            st.text("No Results Found")
                        
                        # outer elif
                        elif top_query2.shape[0] == 1:
                            online_del= st.toggle("Show only the Restaurant has online delivery") # online delivery filter
                            if online_del: # inner if for online delivery filter
                                df_top_online_del = top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes"),["Restaurant Name","Address","Cuisines","Average_Cost_for_two","Dining_Ratings","Dining_Votes"]]
                                if df_top_online_del.shape[0] == 0:
                                    st.text("No Results Found")
                                else:
                                    st.header(':red[Restaurants Details] :open_file_folder:')
                                    st.dataframe(df_top_online_del,hide_index= True)
                            else: # inner else  for online delivery filter
                                st.header(':red[Restaurants Details] :open_file_folder:')
                                st.dataframe(top_query2.loc[:,["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                        # outer else
                        else: 
                            st.subheader("Showing Top 20")
                            popover = st.popover("Sort items")
                            online_del= popover.toggle("Show only the Restaurant has online delivery",key= "online_del")
                            sort_by_delivery= popover.toggle("Sort by Delivery Ratings & Votes", key ="sort_by_delivery" )
                            if online_del:# inner if for online delivery filter
                                
                                if sort_by_delivery:
                                    sort_by_votes ="Delivery_Votes"
                                    sort_by_ratings = "Delivery_Ratings"
                                    top_query2 = df.loc[(df["City"]== selected_city )&(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Delivery_Votes", ascending=False).head(20)
                                    top_query_2_all =df.loc[(df["City"]== selected_city )&(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Delivery_Votes", ascending=False)
                                    st.info(f"sorted based on Delivery Votes and Delivery Ratings")
                                if not sort_by_delivery :
                                    sort_by_votes ="Dining_Votes"
                                    sort_by_ratings = "Dining_Ratings"
                                    st.info(f"sorted based on Dining Votes and Dining Ratings")
                                
                                duplicate_names = top_query2["Restaurant_Name"].duplicated(keep=False)
                                top_query2['Restaurant Name with Locality'] = top_query2.apply(lambda row: f"{row['Restaurant_Name']} ({row['Locality']})" if duplicate_names[row.name] else row['Restaurant_Name'], axis=1)
                                top_query2 = top_query2.sort_values(by=sort_by_votes, ascending=False)
                                top_query2_online_del = top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes")]
                                if top_query2_online_del.shape[0] == 0:
                                    st.text("No Results Found")

                                else: 
                                    top_query2_fig = px.bar(top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes")],
                                                            x = "Restaurant Name with Locality" , 
                                                            y= sort_by_votes, 
                                                            text = sort_by_ratings , 
                                                            color = sort_by_ratings,
                                                            color_continuous_scale= px.colors.sequential.Viridis)
                                    top_query2_fig.update_layout(xaxis=dict(title='Restaurant Name'), yaxis=dict(title="Votes"))
                                    top_query2_fig.update_traces(textposition = "outside")
                                    top_query2_fig.update_traces(hovertemplate="Votes: %{y}<br>Rating: %{text}")
                                    
                                    st.plotly_chart(top_query2_fig, use_container_width=True)

                                    st.header(':red[Restaurants Details] :open_file_folder:')
                                    show_all= st.toggle(f"Show All {",".join(price)} Restaurant having online delivery in {selected_city}")

                                    if show_all:
                                        st.dataframe(top_query_2_all.loc[(top_query_2_all["Has_Online_Delivery"] == "Yes"),["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                                    else:
                                        st.dataframe(top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes"),["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)

                            else: # inner else  for online delivery filter
                                
                                if sort_by_delivery:
                                    sort_by_votes ="Delivery_Votes"
                                    sort_by_ratings = "Delivery_Ratings"
                                    st.info(f"sorted based on Delivery Votes and Delivery Ratings")
                                    top_query2 = df.loc[(df["City"]== selected_city )&(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Delivery_Votes", ascending=False).head(20)
                                    top_query_2_all =df.loc[(df["City"]== selected_city )&(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Delivery_Votes", ascending=False)
                                if not sort_by_delivery :
                                    sort_by_votes ="Dining_Votes"
                                    sort_by_ratings = "Dining_Ratings"
                                    st.info(f"sorted based on Dining Votes and Dining Ratings")

                                duplicate_names = top_query2["Restaurant_Name"].duplicated(keep=False)
                                top_query2['Restaurant Name with Locality'] = top_query2.apply(lambda row: f"{row['Restaurant_Name']} ({row['Locality']})" if duplicate_names[row.name] else row['Restaurant_Name'], axis=1)
                                top_query2 = top_query2.sort_values(by=sort_by_votes, ascending=False)
                                top_query2_fig = px.bar(top_query2,  
                                                        x = "Restaurant Name with Locality" , 
                                                        y= sort_by_votes,
                                                        text = sort_by_ratings, 
                                                        color = sort_by_ratings,
                                                        color_continuous_scale= px.colors.sequential.Viridis)
                                top_query2_fig.update_layout(xaxis=dict(title='Restaurant Name'), yaxis=dict(title="Votes"))
                                top_query2_fig.update_traces(textposition = "outside")
                                top_query2_fig.update_traces(hovertemplate="Votes: %{y}<br>Rating: %{text}")
                            
                                st.plotly_chart(top_query2_fig, use_container_width=True)
                                st.divider() 
                                st.header(':red[Restaurants Details] :open_file_folder:')
                                show_all= st.toggle(f"Show all the {",".join(price)} restaurants in {selected_city}")
                                if show_all:
                                    st.dataframe(top_query_2_all.loc[:,["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                                else:
                                    st.dataframe(top_query2.loc[:,["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)

                filter_container5 =  st.container(border = True) 
                filter_container5.subheader("Option Selector")
                selected_city = filter_container5.selectbox("Select City", sorted(df['City'].unique()),index= None) 
                if selected_city:
                    selected_default_expander = filter_container5.expander("Quick Selection")
                    default_price_options = ['Lower-Priced','Budget-Friendly','Affordable', 'Moderate','Semi-Expensive','Expensive','Luxurious']
                    with selected_default_expander:
                        st.write(f"<span style='color:#ef4f5f'>Please un-check selected option to see all the options</span>", unsafe_allow_html=True)
                        if st.checkbox("Top Rated Restaurants",key= "selected_default_expander1"):
                            selected_default = default_price_options
                            selected_default_rating = ["Excellent","Very Good"]
                        elif st.checkbox("Top Rated Lower-Priced Restaurants",key= "selected_default_expander2"):
                            selected_default = default_price_options[0:2]   
                            selected_default_rating = ["Excellent","Very Good"]          
                        elif st.checkbox("Top Rated Mid-Range Restaurants",key= "selected_default_expander3"):
                            selected_default = default_price_options[2:4] 
                            selected_default_rating = ["Excellent","Very Good"]
                        elif st.checkbox("Top Rated Expensive Restaurants",key= "selected_default_expander4"):
                            selected_default = default_price_options[4:6]  
                            selected_default_rating = ["Excellent","Very Good"]   
                        elif st.checkbox("Top Rated Luxurious Restaurants",key= "selected_default_expander5"):
                            selected_default = default_price_options[6]    
                            selected_default_rating = ["Excellent","Very Good"]                                                                     
                        else:
                            selected_default = None
                            selected_default_rating = None
                    filter_container5a =  st.container(border = True)
                    filter_container5a.subheader("Filter Options")
                    price = filter_container5a.multiselect("Select Pricing based on your budget",
                                    sorted(df['Cost_Category'].unique()),  # Ensure it's a list of strings
                                    default=selected_default)
                    dine_rating = filter_container5a.multiselect("Select Rating",
                                    sorted(df['Dining_Rating_Text'].unique()),  # Ensure it's a list of strings
                                    default=selected_default_rating)
                    top_query(selected_city,price,dine_rating)
            ins_tab1_fn()


        if city_wise_type_selection == "**Search for Specific Cuisine**":
            # html_string = """
            # <style>
            # .gif-container {
            #     display: flex;
            #     justify-content: center;
            #     align-items: center;
            # }
            # .gif-container img {
            #     width: 200;
            #     height: 200px;
            # }
            # </style>

            # <div class="gif-container">
            # <img src="https://media.giphy.com/media/lOIrcFa0N9vJh1yBaq/giphy.gif" alt="Alt Text">
            # </div>
            # """

            # st.markdown(html_string, unsafe_allow_html=True)
            # URL of the Lottie animation
            lottie_url = "https://lottie.host/a25633a4-3ae0-40f5-96f4-079c070c21be/bpi6WAWp0w.json"  # Replace with your Lottie file URL

            # Load the Lottie animation
            lottie_animation = load_lottie_url(lottie_url)

            # Create three columns
            col1, col2, col3 = st.columns([1,0.75, 1])
            with col2:
                st_lottie(lottie_animation, width=300, height=300,quality= 'medium')

            def ins_tab2_fn():
                unique_cuisines = df['Cuisines'].str.split(', ').explode().unique()
                # Function to find the closest match for entered cuisine
                def find_closest_match(entered_cuisine):
                    matches = difflib.get_close_matches(entered_cuisine, unique_cuisines, n=1)
                    if matches:
                        return matches[0]
                    else:
                        return None 

                def specific_cuisine(selected_city,price,dine_rating,corrected_cuisine):
                    
                    top_query2 = df.loc[(df["City"]== selected_city )&(df["Dining_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price)) & (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Dining_Votes", ascending=False).head(20)
                    top_query_2_all =df.loc[(df["City"]== selected_city )&(df["Dining_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Dining_Votes", ascending=False)
                    if selected_city and corrected_cuisine and price and dine_rating  :
                        # outer if
                        if top_query2.shape[0] == 0 :
                            st.warning("No Results Found")
                        
                        # outer elif
                        elif top_query2.shape[0] == 1:
                            online_del= st.toggle("Show only the Restaurant has online delivery") # online delivery filter
                            if online_del: # inner if for online delivery filter
                                df_top_online_del = top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes"),["Restaurant Name","Address","Cuisines","Average_Cost_for_two","Dining_Ratings","Dining_Votes"]]
                                if df_top_online_del.shape[0] == 0:
                                    st.warning("No Results Found")
                                else:
                                    st.header(':red[Restaurants Details] :open_file_folder:')
                                    st.dataframe(df_top_online_del,hide_index= True)
                            else: # inner else  for online delivery filter
                                st.header(':red[Restaurants Details] :open_file_folder:')
                                st.dataframe(top_query2.loc[:,["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                        # outer else
                        else: 
                            st.subheader(f"Showing 20 Restaurants in {selected_city}")
                            popover = st.popover("Sort items")
                            online_del= popover.toggle("Show only the Restaurant has online delivery",key = "tab2ondel")
                            sort_by_delivery= popover.toggle("Sort by Delivery Ratings & Votes",key = "tab2sort_by_delivery")
                            
                            if online_del:# inner if for online delivery filter
                                
                                if sort_by_delivery:
                                    sort_by_votes ="Delivery_Votes"
                                    sort_by_ratings = "Delivery_Ratings"
                                    top_query2 = df.loc[(df["City"]== selected_city )&(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Delivery_Votes", ascending=False).head(20)
                                    top_query_2_all =df.loc[(df["City"]== selected_city )&(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Delivery_Votes", ascending=False)
                                    st.info(f"sorted based on Delivery Votes and Delivery Ratings")
                                if not sort_by_delivery :
                                    sort_by_votes ="Dining_Votes"
                                    sort_by_ratings = "Dining_Ratings"
                                    st.info(f"sorted based on Dining Votes and Dining Ratings")
                                
                                duplicate_names = top_query2["Restaurant_Name"].duplicated(keep=False)
                                top_query2['Restaurant Name with Locality'] = top_query2.apply(lambda row: f"{row['Restaurant_Name']} ({row['Locality']})" if duplicate_names[row.name] else row['Restaurant_Name'], axis=1)
                                top_query2 = top_query2.sort_values(by=sort_by_votes, ascending=False)
                                top_query2_online_del = top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes")]
                                if top_query2_online_del.shape[0] == 0:
                                    st.warning("No Results Found")

                                else: 
                                    top_query2_fig = px.bar(top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes")],
                                                            x = "Restaurant Name with Locality" , 
                                                            y= sort_by_votes, 
                                                            text = sort_by_ratings , 
                                                            color = sort_by_ratings,
                                                            color_continuous_scale= px.colors.sequential.Viridis)
                                    top_query2_fig.update_layout(xaxis=dict(title='Restaurant Name'), yaxis=dict(title="Votes"))
                                    top_query2_fig.update_traces(textposition = "outside")
                                    top_query2_fig.update_traces(hovertemplate="Votes: %{y}<br>Rating: %{text}")
                                    
                                    st.plotly_chart(top_query2_fig, use_container_width=True)

                                    st.header(':red[Restaurants Details] :open_file_folder:')
                                    show_all= st.toggle(f"Show All the Restaurants having {corrected_cuisine} in {selected_city} having online delivery")

                                    if show_all:
                                        st.dataframe(top_query_2_all.loc[(top_query_2_all["Has_Online_Delivery"] == "Yes"),["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                                    else:
                                        st.dataframe(top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes"),["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)

                            else: # inner else  for online delivery filter
                                if sort_by_delivery:
                                    sort_by_votes ="Delivery_Votes"
                                    sort_by_ratings = "Delivery_Ratings"
                                    st.info(f"sorted based on Delivery Votes and Delivery Ratings")
                                    top_query2 = df.loc[(df["City"]== selected_city )&(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Delivery_Votes", ascending=False).head(20)
                                    top_query_2_all =df.loc[(df["City"]== selected_city )&(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Delivery_Votes", ascending=False)
                                if not sort_by_delivery :
                                    sort_by_votes ="Dining_Votes"
                                    sort_by_ratings = "Dining_Ratings"
                                    st.info(f"sorted based on Dining Votes and Dining Ratings")

                                duplicate_names = top_query2["Restaurant_Name"].duplicated(keep=False)
                                top_query2['Restaurant Name with Locality'] = top_query2.apply(lambda row: f"{row['Restaurant_Name']} ({row['Locality']})" if duplicate_names[row.name] else row['Restaurant_Name'], axis=1)
                                top_query2 = top_query2.sort_values(by=sort_by_votes, ascending=False)
                                top_query2_fig = px.bar(top_query2,  
                                                        x = "Restaurant Name with Locality" , 
                                                        y= sort_by_votes,
                                                        text = sort_by_ratings, 
                                                        color = sort_by_ratings,
                                                        color_continuous_scale= px.colors.sequential.Viridis)
                                top_query2_fig.update_layout(xaxis=dict(title='Restaurant Name'), yaxis=dict(title="Votes"))
                                top_query2_fig.update_traces(textposition = "outside")
                                top_query2_fig.update_traces(hovertemplate="Votes: %{y}<br>Rating: %{text}")
                            
                                st.plotly_chart(top_query2_fig, use_container_width=True)
                                st.divider() 
                                st.header(':red[Restaurants Details] :open_file_folder:')
                                show_all= st.toggle(f"Show All the Restaurants having {corrected_cuisine} in {selected_city}")
                                if show_all:
                                    st.dataframe(top_query_2_all.loc[:,["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                                else:
                                    st.dataframe(top_query2.loc[:,["Restaurant_Name","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                    
                    else:
                        st.info("Please select all the above options")
                
                filter_container6 =  st.container(border = True) 
                cus_q1,cus_q2 = filter_container6.columns(2)
                with cus_q1:
                    selected_city = st.selectbox("Select City", sorted(df['City'].unique()),placeholder="e.g., Chennai",index= None)

                if selected_city: 

                    with cus_q2:
                        st.markdown("<span style='color:#ef4f5f'>Type the Cuisine in your mind</span>", unsafe_allow_html=True)
                        entered_cuisine = st.text_input(label="Enter the cuisine", placeholder="e.g., Biryani", max_chars= 15)
                        st.markdown("<span style='color:#ef4f5f'>OR select the cuisine from below</span>", unsafe_allow_html=True)
                        cusine_dropbox = st.selectbox("Click to select cuisine", sorted([i for i in unique_cuisines if i not in ["Afghan","Beverages,"] ]),index = None)
                    if entered_cuisine and "," in entered_cuisine :
                        st.error("Please don't add more than one cuisine for best results")
                    
                    if entered_cuisine or cusine_dropbox:
                    # Perform auto-correction
                        if cusine_dropbox:
                            corrected_cuisine = cusine_dropbox
                        else:
                            corrected_cuisine = find_closest_match(entered_cuisine) 
                        if corrected_cuisine:
                            filter_container5c = st.container(border=True)
                            filter_container5c.markdown('Filter Options')
                            selected_default_expander = filter_container5c.expander("Quick Selection")
                            default_price_options = ['Lower-Priced','Budget-Friendly','Affordable', 'Moderate','Semi-Expensive','Expensive','Luxurious']
                            with selected_default_expander:
                                st.write(f"<span style='color:#ef4f5f'>Please un-check selected option to see all the options</span>", unsafe_allow_html=True)
                                if st.checkbox("Top Rated Restaurants",key= "selected_default_expander1"):
                                    selected_default = default_price_options
                                    selected_default_rating = ["Excellent","Very Good"]   
                                elif st.checkbox("Top Rated Lower-Priced Restaurants",key= "selected_default_expander2"):
                                    selected_default = default_price_options[0:2]   
                                    selected_default_rating = ["Excellent","Very Good"]   
                                elif st.checkbox("Top Rated Mid-Range Restaurants",key= "selected_default_expander3"):
                                    selected_default = default_price_options[2:4] 
                                    selected_default_rating = ["Excellent","Very Good"]   
                                elif st.checkbox("Top Rated Expensive Restaurants",key= "selected_default_expander4"):
                                    selected_default = default_price_options[4:6] 
                                    selected_default_rating = ["Excellent","Very Good"]       
                                elif st.checkbox("Top Rated Luxurious Restaurants",key= "selected_default_expander5"):
                                    selected_default = default_price_options[6]  
                                    selected_default_rating = ["Excellent","Very Good"]                                                                          
                                else:
                                    selected_default = None      
                                    selected_default_rating = None
                                                                 
                            price = filter_container5c.multiselect("Select Pricing",
                                        sorted(df['Cost_Category'].unique()),  # Ensure it's a list of strings
                                        default=selected_default,key="ins_tab2_fn_pricing_multiselect")
                            dine_rating = filter_container5c.multiselect("Select Rating",
                                        sorted(df['Dining_Rating_Text'].unique()),  # Ensure it's a list of strings
                                        default=selected_default_rating,key="ins_tab2_fn_rating_multiselect")
                            specific_cuisine(selected_city,price,dine_rating,corrected_cuisine)
                        
                        else:
                            st.warning("No results Found")
                    else:
                        st.info("Please enter valid cuisine name")
            ins_tab2_fn()
        if city_wise_type_selection == "**Cuisine Analyzer**":

            # URL of the Lottie animation
            lottie_url = "https://lottie.host/b1d1911e-83af-428e-887e-d647e028513c/NJeWiTiVDh.json"  # Replace with your Lottie file URL

            # Load the Lottie animation
            lottie_animation = load_lottie_url(lottie_url)

            # Create three columns
            col1, col2, col3 = st.columns([1,0.75, 1])

            # Display the Lottie animation in the center column
            with col2:
                st_lottie(lottie_animation, width=300, height=300,quality= 'medium')

            def ins_tab3_fn():
                filter_container3 =  st.container(border = True) 
                analyzer_type_selection = filter_container3.radio('Category Selection',["**Popular Cuisines**","**Cuisine Filter by Ratings & Costs**"], index = None)
                st.write("You selected:", f"<span style='color:#ef4f5f'>{analyzer_type_selection}</span>", unsafe_allow_html=True)
                                    
                def cusines_analyzer(selected_city):
                    if selected_city:
                        tab1,tab2 = st.tabs(["Chart", "Data"])
                        with tab1:
                            st.subheader(f"Showing Popular Cuisines in :red[ {selected_city}]")
                            c_analyzer_df_1 = df.loc[(df.City == selected_city)]
                            c_analyzer_df_1 = c_analyzer_df_1.groupby('City')['Cuisines'].apply(lambda x: x.str.split(', ').explode().value_counts()).reset_index()
                            c_analyzer_df_1 = c_analyzer_df_1.rename(columns={'City': 'City', selected_city: 'Cuisines', 'Cuisines': 'Count'})

                            c_analyzer_df_1_fig = px.pie(c_analyzer_df_1.head(10),
                                                        names = "Cuisines",
                                                        values = "Count",
                                                        hole = 0.7,
                                                        color_discrete_sequence=px.colors.qualitative.Vivid
                                                        )
                            c_analyzer_df_1_fig.update_traces(textposition='outside', textinfo='percent+label', pull=[0.05, 0.05, 0.05])
                            c_analyzer_df_1_fig.update_layout(showlegend=False, width=750, height=550)
                            c_analyzer_df_1_fig.update_traces(marker=dict(line=dict(color='#000000', width=0.25))) 
                            st.plotly_chart(c_analyzer_df_1_fig, use_container_width=True) 
                        with tab2:
                            st.header(':red[Data] :open_file_folder:')
                            c_analyzer_df_1_show_all = st.toggle(f"Show all Cuisines and It's Restaurant Count in {selected_city}")
                            if c_analyzer_df_1_show_all:
                                st.dataframe(c_analyzer_df_1.iloc[:,1:],hide_index = True)             
                            else:
                                st.dataframe(c_analyzer_df_1.iloc[:,1:].head(20),hide_index = True)       


                if analyzer_type_selection == "**Popular Cuisines**":     
                    selected_city = st.selectbox("Select City", sorted(df['City'].unique()),placeholder="e.g., Chennai",index= None,key="tab3popularcus")  
                    cusines_analyzer(selected_city)

                def cusines_analyzer1(selected_city,min_rating,pricing):
                    if selected_city :
                        tab1,tab2 = st.tabs(["Chart", "Data"])
                        with tab1:
                            st.subheader(f"Showing Popular Cuisines in :red[{selected_city}]")
                            popover = st.popover("Sort items")
                            sort_delivery =  popover.toggle("Filter Based on Delivery Ratings & Votes",key="tab3cusana1sortdel")
                            if sort_delivery:
                                c_analyzer_df_1 = df.loc[(df.City == selected_city) &(df.Delivery_Ratings >= min_rating)&(df.Cost_Category.isin(pricing))].sort_values(by="Delivery_Votes",ascending = False)
                                c_analyzer_df_1 = c_analyzer_df_1.groupby('City')['Cuisines'].apply(lambda x: x.str.split(', ').explode().value_counts()).reset_index()
                                c_analyzer_df_1 = c_analyzer_df_1.rename(columns={'City': 'City', selected_city: 'Cuisines', 'Cuisines': 'Count'})                          
                            else:
                                c_analyzer_df_1 = df.loc[(df.City == selected_city) &(df.Dining_Ratings >= min_rating) & (df.Cost_Category.isin(pricing))].sort_values(by="Dining_Votes",ascending = False)
                                c_analyzer_df_1 = c_analyzer_df_1.groupby('City')['Cuisines'].apply(lambda x: x.str.split(', ').explode().value_counts()).reset_index()
                                c_analyzer_df_1 = c_analyzer_df_1.rename(columns={'City': 'City', selected_city: 'Cuisines', 'Cuisines': 'Count'})                 


                            if c_analyzer_df_1.shape[0] == 0:
                                st.warning("No Results Found")
                            
                            elif c_analyzer_df_1.shape[0] == 1:
                                st.plotly_chart(c_analyzer_df_1_fig, use_container_width=True) 
                            
                            else:
                                c_analyzer_df_1_fig = px.bar(c_analyzer_df_1.head(10),
                                                            x = "Cuisines",
                                                            y = "Count",
                                                            text = "Count", 
                                                            color = "Count",
                                                            color_continuous_scale= px.colors.sequential.Viridis)
                                c_analyzer_df_1_fig.update_layout(xaxis=dict(title='Cuisines'), yaxis=dict(title="Restaurant Count"))
                                c_analyzer_df_1_fig.update_traces(textposition = "outside")
                                c_analyzer_df_1_fig.update_traces(hovertemplate="Cuisines: %{x}<br>Restaurant Count: %{y}")
                                st.plotly_chart(c_analyzer_df_1_fig, use_container_width=True) 
                        with tab2:
                            if c_analyzer_df_1.shape[0] >1:
                                st.header(':red[Data] :open_file_folder:')
                                c_analyzer_df_1_show_all = st.toggle(f"Show all Cuisines and It's Restaurant Count in {selected_city}")
                                if c_analyzer_df_1_show_all:
                                    st.dataframe(c_analyzer_df_1.iloc[:,1:],hide_index = True)             
                                else:
                                    st.dataframe(c_analyzer_df_1.iloc[:,1:].head(20),hide_index = True)
                            
                            else: 
                                st.warning("No Results Found")
                    else:
                        st.info("Please Select the city")
                        st.stop()
                if analyzer_type_selection == "**Cuisine Filter by Ratings & Costs**": 
                    filter_container4 =  st.container(border = True) 
                    filter_container4.subheader(':red[Filter Options] :slot_machine:')
                    col1, col2,col3 =  filter_container4.columns(3)  

                    selected_default_expander = filter_container4.expander("Quick Selection")
                    default_price_options = ['Lower-Priced','Budget-Friendly','Affordable', 'Moderate','Semi-Expensive','Expensive','Luxurious']
                    with selected_default_expander:
                        st.write(f"<span style='color:#ef4f5f'>Please un-check selected option to see all the options</span>", unsafe_allow_html=True)
                        if st.checkbox("Lower-Priced Cuisines",key= "selected_default_expander2"):
                            selected_default = default_price_options[0:2]     
                        elif st.checkbox("Mid-Range Cuisines",key= "selected_default_expander3"):
                            selected_default = default_price_options[2:4]  
                        elif st.checkbox("Expensive Cuisines",key= "selected_default_expander4"):
                            selected_default = default_price_options[4:6]   
                        elif st.checkbox("Luxurious Cuisines",key= "selected_default_expander5"):
                            selected_default = default_price_options[6]                                                                                      
                        else:
                            selected_default = None      
               
                    with col1:                  
                        selected_city = st.selectbox("Select City", sorted(df['City'].unique()),placeholder="e.g., Chennai",index= None,key = "tab3cusfilter_city") 
                        st.write("You selected:", f"<span style='color:#ef4f5f'>{selected_city}</span>", unsafe_allow_html=True) 
                    with col2:
                    # Define the rating slider
                        min_rating = st.slider("Select Minimum Rating", min_value=0, max_value=5, step=1, value=0)
                        st.write("Your selected ratings:", f"<span style='color:#ef4f5f'>{min_rating}⭐ & Up</span>", unsafe_allow_html=True)
                    with col3:
                        pricing = st.multiselect("Select Pricing",
                                        sorted(df['Cost_Category'].unique()),  # Ensure it's a list of strings
                                        default=selected_default)
                    cusines_analyzer1(selected_city,min_rating,pricing)

            ins_tab3_fn()
        if city_wise_type_selection == "**Compare Cuisines**":
            def city__wise_compare_cuisines():
                st.header("Compare Cuisines")
                unique_cuisines = df['Cuisines'].str.split(', ').explode().unique()
                unique_cities = df['City'].unique()

                # User input for selecting a city
                city = st.selectbox("Select a city", sorted(unique_cities))
                # Filter data for the selected city
                df_city = df[df['City'] == city]

                # User input for selecting two cuisines to compare
                cuisine_1 = st.selectbox("Select the first cuisine", sorted([i for i in unique_cuisines if i not in ["Afghan","Beverages,"] ]),index = None)
                cuisine_2 = st.selectbox("Select the second cuisine", sorted([i for i in unique_cuisines if i not in ["Afghan","Beverages,"] ]),index = None)

                if cuisine_1 and cuisine_2:
                    st.subheader(f"Comparing {cuisine_1} vs {cuisine_2} in {city}")

                    # Filter data for each cuisine within the selected city
                    df_cuisine_1 = df_city[df_city['Cuisines'].str.contains(cuisine_1, case=False)]
                    df_cuisine_2 = df_city[df_city['Cuisines'].str.contains(cuisine_2, case=False)]

                    # Calculate statistics for each cuisine
                    stats_cuisine_1 = {
                        "Average Cost for Two": df_cuisine_1['Average_Cost_For_Two'].mean(),
                        "Average Dining Rating": df_cuisine_1['Dining_Ratings'].mean(),
                        "Average Delivery Rating": df_cuisine_1['Delivery_Ratings'].mean(),
                        "Number of Restaurants": df_cuisine_1.shape[0]
                    }

                    stats_cuisine_2 = {
                        "Average Cost for Two": df_cuisine_2['Average_Cost_For_Two'].mean(),
                        "Average Dining Rating": df_cuisine_2['Dining_Ratings'].mean(),
                        "Average Delivery Rating": df_cuisine_2['Delivery_Ratings'].mean(),
                        "Number of Restaurants": df_cuisine_2.shape[0]
                    }

                    com_cus_cont_1 = st.container()
                    com_cus_cont_2 = st.container()
                    # Display statistics
                    with com_cus_cont_1:
                        st.write(f"**{cuisine_1} Statistics:**")
                        for key, value in stats_cuisine_1.items():
                            st.write(f"{key}: {value:.2f}")
                    with com_cus_cont_2:
                        st.write(f"**{cuisine_2} Statistics:**")
                        for key, value in stats_cuisine_2.items():
                            st.write(f"{key}: {value:.2f}")

                    # Plot price distribution
                    st.subheader(f"Price Distribution")
                    bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000, 2500, 3000, 4000, 5000, float('inf')]
                    labels = [
                        '0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500',
                        '500-600', '600-700', '700-800', '800-900', '900-1000', '1000-1250', '1250-1500', '1500-1750', '1750-2000',
                        '2000-2500', '2500-3000', '3000-4000', '4000-5000', '5000+'
                    ]
                    df_price_dist = pd.DataFrame({
                        'Price Range': pd.cut(df_city['Average_Cost_For_Two'], bins=bins, labels=labels, right=False),
                        'Cuisine': df_city['Cuisines'].apply(lambda x: cuisine_1 if cuisine_1 in x else (cuisine_2 if cuisine_2 in x else None))
                    }).dropna()
                    df_price_dist = df_price_dist.sort_values(by="Price Range")
                    price_dist_fig = px.histogram(df_price_dist, x='Price Range', color='Cuisine', barmode='group',
                                                color_discrete_sequence=px.colors.qualitative.Vivid,
                                                title=f"Price Distribution of {cuisine_1} vs {cuisine_2} in {city}",
                                                labels={"Price Range": "Amount (₹)", "count": "% of orders"})
                    st.plotly_chart(price_dist_fig, use_container_width=True)

                    # Plot rating distribution
                    st.subheader("Rating Distribution")
                    df_rating_dist = pd.melt(df_city[df_city['Cuisines'].str.contains(f"{cuisine_1}|{cuisine_2}", case=False)],
                                            id_vars=['Cuisines'],
                                            value_vars=['Dining_Ratings', 'Delivery_Ratings'],
                                            var_name='Rating Type',
                                            value_name='Rating')

                    df_rating_dist['Cuisine'] = df_rating_dist['Cuisines'].apply(lambda x: cuisine_1 if cuisine_1 in x else (cuisine_2 if cuisine_2 in x else None)).dropna()
                    rating_dist_fig = px.histogram(df_rating_dist, x='Rating', color='Cuisine', barmode='group',
                                                facet_row='Rating Type', color_discrete_sequence=px.colors.qualitative.Vivid,
                                                title=f"Rating Distribution of {cuisine_1} vs {cuisine_2} in {city}",
                                                labels={"count": "% of orders"})
                    st.plotly_chart(rating_dist_fig, use_container_width=True)
                else:
                    st.warning("Please select both cuisines to compare.")

            city__wise_compare_cuisines()

        if city_wise_type_selection == "**Locality Analyzer**":
            lottie_url = "https://lottie.host/ab875427-6843-4496-8275-c8584ab034a2/ytDvG4prHv.json" 

            # Load the Lottie animation
            lottie_animation = load_lottie_url(lottie_url)

            # Create three columns
            col1, col2, col3 = st.columns([1, 0.5, 1])

            # Display the Lottie animation in the center column
            with col2:
                st_lottie(lottie_animation, width=250, height=250,quality= 'medium')   
            def locality_analyzer(selected_city):
            # Load the data
                locality_data = df
                def find_area(address, locality):
                    address_parts = address.split(',')
                    # Try to find the last element containing a city or locality
                    for i in range(len(address_parts)-1, -1, -1):
                        part = address_parts[i].strip()
                        if part.lower() in locality.lower():
                            # Check if the previous element is the area
                            if i > 0:
                                area = address_parts[i-1].strip()
                                if area not in locality.lower():
                                    return area
                            break
                    return None
                    # Add a new column to store the area name
                locality_data['Area'] = locality_data.apply(lambda row: find_area(row['Address'], row['Locality']), axis=1)
                locality_data.Area.fillna("Unknown",inplace= True)



                def refine_area_name(area):
                    # Remove "Near" from the area name
                    refined_area = re.sub(r'\bNear\b', '', area, flags=re.IGNORECASE).strip()

                    # If refined area is empty after stripping, return None
                    if not refined_area:
                        return None

                    return refined_area.title()  # Capitalize the first letter of each word


                
                locality_data['Area'] = locality_data['Area'].apply(refine_area_name)
                locality_data.Area.fillna(locality_data.Address.str.split(",").str[-2].str.strip(),inplace= True)

                # Reset index
                locality_data.reset_index(drop=True, inplace=True)
                # Filter data for city
                
                city_data = locality_data[locality_data['City'] == selected_city]

                area_counts = city_data['Area'].value_counts()

                # Filter out the rows where the count of unique values in the "Area" column is not greater than 3
                valid_areas = area_counts[area_counts > 3].index

                # Filter the DataFrame to keep only rows with "Area" values that occur more than 3 times
                locality_data_filtered = locality_data[locality_data['Area'].isin(valid_areas)]
                # Calculate average ratings by locality
                area_counts_data = locality_data_filtered.groupby('Area').agg({
                    'Dining_Ratings': 'mean',
                    'Delivery_Ratings': 'mean',
                    'City': 'count'
                }).reset_index()
                area_counts_data.rename(columns = {"City":"Count"}, inplace = True)
                area_counts_data['Dining_Ratings'] = area_counts_data['Dining_Ratings'].round(2)
                area_counts_data['Delivery_Ratings'] = area_counts_data['Delivery_Ratings'].round(2)
                sort_by_del = st.toggle("Sort by Delivery Rating")
                if sort_by_del:
                    top_localities = area_counts_data.sort_values(by = ["Delivery_Ratings","Count"],ascending = False).reset_index(drop= True)
                    sort_by_how = 'Delivery_Ratings'
                if not sort_by_del:
                    top_localities = area_counts_data.sort_values(by = ["Dining_Ratings","Count"],ascending = False).reset_index(drop= True)
                    sort_by_how = 'Dining_Ratings'


                # Plotting
                fig = px.bar(top_localities.head(20), 
                            x='Area', 
                            y=sort_by_how,
                            color =sort_by_how,
                            color_continuous_scale= px.colors.sequential.Viridis,
                            text = sort_by_how)
                fig.update_layout(xaxis={'categoryorder':'total descending'})
                fig.update_traces(textposition = "inside")
                fig.update_traces(hovertemplate="Locality: %{x}<br>Average Rating: %{y}")
                st.plotly_chart(fig,use_container_width= True)
                st.dataframe(top_localities)
            selected_city = st.selectbox("Select City", sorted(df['City'].unique()),index= None) 
            if selected_city:
                locality_analyzer(selected_city)
        

        if city_wise_type_selection == "**Cost Vs Ratings**":
               # URL of the Lottie animation
            lottie_url = "https://lottie.host/153745bd-a08a-488f-9b7c-879b3a19f588/PNAnD5X7UY.json" 

            # Load the Lottie animation
            lottie_animation = load_lottie_url(lottie_url)

            # Create three columns
            col1, col2, col3 = st.columns([1, 0.5, 1])

            # Display the Lottie animation in the center column
            with col2:
                st_lottie(lottie_animation, width=250, height=250,quality= 'medium')        


            def costvsratings(selected_city):
                city_data = df[df['City'] == selected_city]
                # Define the order of cost categories
                cost_order = ['Lower-Priced', 'Budget-Friendly', 'Affordable', 'Moderate', 'Semi-Expensive', 'Expensive','Luxurious']

                # Group by Cost_Category and calculate mean ratings
                ratings_by_cost = city_data.groupby('Cost_Category').agg({
                    'Dining_Ratings': 'mean',
                    'Delivery_Ratings': 'mean'
                }).reindex(cost_order)

                # Reset index to ensure proper ordering
                ratings_by_cost.reset_index(inplace=True)
               
                # Melt the dataframe to long format for line chart
                ratings_by_cost_melted = pd.melt(ratings_by_cost, id_vars=['Cost_Category'], var_name='Rating Type', value_name='Average Rating')
                ratings_by_cost_melted['Average Rating'] = ratings_by_cost_melted['Average Rating'].round(2)

                with st.expander("See Explanation"):
                    st.markdown("<p style='color:red'>The reason why delivery ratings decrease after the moderate price categories is because many expensive and luxurious restaurants don't provide online delivery services.</p>", unsafe_allow_html=True)

                    delivery_counts = city_data.groupby('Cost_Category')['Has_Online_Delivery'].value_counts(normalize=True).unstack().fillna(0)
                    delivery_counts = delivery_counts.reindex(cost_order)

                    # Plotting
                    fig1 = px.bar(delivery_counts, x=delivery_counts.index, y=['Yes', 'No'],
                                title=f'Proportion of Restaurants with Online Delivery in {selected_city}',
                                labels={'value': 'Proportion', 'variable': 'Has Online Delivery'},
                                category_orders={'index': cost_order}, barmode='stack', color_discrete_map={'Yes': 'green', 'No': 'red'})

                    fig1.update_layout(xaxis={'title': 'Cost Category'}, yaxis={'title': 'Proportion'})
                    st.plotly_chart(fig1,use_container_width= True)                
                # Plotting
                fig = px.line(ratings_by_cost_melted, x='Cost_Category', y='Average Rating', color='Rating Type',
                            title='Cost vs. Ratings Analysis', labels={'Average Rating': 'Average Rating'},
                            category_orders={'Cost_Category': cost_order},color_discrete_sequence=px.colors.qualitative.Vivid ,markers=True)
                fig.update_layout(xaxis={'categoryorder': 'array', 'categoryarray': cost_order})
                fig.update_traces(hovertemplate="Cost Category: %{x}<br>Average Rating: %{y}")
                st.plotly_chart(fig,use_container_width= True)

                
            selected_city = st.selectbox("Select City", sorted(df['City'].unique()),index= None) 
            if selected_city:
                costvsratings(selected_city)



    if type_selection == "**India-Wise**":
        
        ind_queries = filter_container1.radio("Category Selection",["Top Restaurants in India",
                                                     "Popular Cuisines in India",  
                                                     "Search for Specific Cuisines",
                                                     "Cuisine Filter by Ratings & Costs",
                                                     "Compare Cuisines",
                                                     "Cost Vs Ratings",
                                                     "Popular Cuisine Combinations"],index = None,horizontal= False)
        with filter_container1.popover("Confused! Click Me"):
            st.write(f"<span style='color:#ef4f5f'>Top Restaurants in India =></span> This option allows you to find the highest-rated restaurants in India based on user votes and ratings.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Popular Cuisines in India =></span> This option allows you to discover the most popular cuisines available across India.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Search for Specific Cuisine =></span> This option allows you to search and analyze any specific cuisine by typing its name.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Cuisine Filter by Ratings & Costs =></span> This feature has many filters that helps you analyze different aspects of cuisines, such as popularity, best low cost cuisines, worst expensive cuisines ,to make informed decisions on cuisines.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Cost Vs Ratings =></span> This option helps you to see how restaurant ratings vary with different price categories to make good dining choices.", unsafe_allow_html=True)
            st.write(f"<span style='color:#ef4f5f'>Popular Cuisine Combinations =></span> This option helps you to discover popular combinations of cuisines frequently paired in restaurants.", unsafe_allow_html=True)
        st.write("You selected:", f"<span style='color:#ef4f5f'>{type_selection} => {ind_queries}</span>", unsafe_allow_html=True)

        if not ind_queries:
            lottie_url = "https://lottie.host/da5a20ed-6956-4ce4-81db-30973918d48f/U5TStChgbw.json"  

            # Load the Lottie animation
            lottie_animation = load_lottie_url(lottie_url)

            # Create three columns
            col1, col2, col3 = st.columns([1, 1, 1])

            # Display the Lottie animation in the center column
            with col2:
                st_lottie(lottie_animation, width=250, height=250,quality= 'medium')   
                
        if ind_queries:
            if ind_queries == "Popular Cuisines in India":
                def cusines_analyzer():
                    tab1,tab2 = st.tabs(["Chart", "Data"])
                    with tab1:
                        st.subheader(f"Showing Popular Cuisines in :red[All Over India]")
                        c_analyzer_df_1 = df['Cuisines'].str.split(', ').explode().value_counts().reset_index()

                        c_analyzer_df_1_fig = px.pie(c_analyzer_df_1.head(10),
                                                    names = "Cuisines",
                                                    values = "count",
                                                    hole = 0.7,
                                                    color_discrete_sequence=px.colors.qualitative.Vivid
                                                    )
                        c_analyzer_df_1_fig.update_traces(textposition='outside', textinfo='percent+label', pull=[0.05, 0.05, 0.05])
                        c_analyzer_df_1_fig.update_layout(showlegend=False, width=750, height=550)
                        c_analyzer_df_1_fig.update_traces(marker=dict(line=dict(color='#000000', width=0.25))) 
                        with st.expander("Detailed Explanation of Popular Cuisines in India"):
                            st.markdown("""
                            **Description**:
                            This insight reveals the distribution of popular cuisines among Zomato restaurants in India. The data indicates the percentage of restaurants offering each type of cuisine, highlighting the culinary preferences of the Indian population.

                            **Interpretation**:
                            1. **Dominance of North Indian Cuisine**:
                            - North Indian cuisine is the most popular, accounting for 19% of the restaurants. This indicates a strong preference for traditional North Indian dishes among the population.

                            2. **Popularity of Chinese Cuisine**:
                            - Chinese cuisine is the second most popular, with 16% of the restaurants offering it. This reflects a significant influence of Chinese food culture in India.

                            3. **Demand for Beverages**:
                            - Beverages represent 15% of the total, suggesting a high demand for drink options, including coffee, tea, and juices.

                            4. **Fast Food and Desserts**:
                            - Fast food (12%) and desserts (11%) are also quite popular, indicating a trend towards quick, convenient meals and a preference for sweet treats.

                            5. **Specialized Cuisines**:
                            - Biryani (7%) and Pizza (6%) are notable for their specialized appeal, showcasing specific dishes that have a dedicated following.

                            6. **Lesser-Known Cuisines**:
                            - Continental (6%), South Indian (5%), and Italian (4%) cuisines have a smaller presence. This suggests a niche but stable demand for these types of food.

                            **Implications**:
                            - **Business Strategy**: Restaurants can use this information to tailor their menus to include popular cuisines to attract more customers.
                            - **Market Entry**: New entrants in the food industry can focus on high-demand cuisines like North Indian and Chinese to quickly gain market share.
                            - **Culinary Trends**: The data highlights ongoing culinary trends, such as the growing popularity of fast food and beverages.

                            **Conclusion**:
                            The analysis of popular cuisines in India provides valuable insights into consumer preferences. North Indian and Chinese cuisines dominate the market, while there is also substantial demand for beverages, fast food, and desserts. Understanding these trends can help stakeholders make informed decisions about menu offerings, marketing strategies, and business expansion.

                            **Recommendations**:
                            - **Menu Optimization**: Restaurants should consider featuring popular cuisines prominently on their menus.
                            - **Promotional Campaigns**: Targeted promotions for high-demand cuisines can attract more customers.
                            - **Diversification**: Offering a mix of popular and niche cuisines can cater to a broader audience and enhance customer satisfaction.
                            """)                        
                        st.plotly_chart(c_analyzer_df_1_fig, use_container_width=True) 

                        
                    with tab2:
                        st.header(':red[Data] :open_file_folder:')
                        c_analyzer_df_1_show_all = st.toggle(f"Show all Cuisines and It's Restaurant Count ")
                        if c_analyzer_df_1_show_all:
                            st.dataframe(c_analyzer_df_1,hide_index = True)             
                        else:
                            st.dataframe(c_analyzer_df_1.head(10),hide_index = True)       

                cusines_analyzer()

            elif ind_queries == "Top Restaurants in India":
                def Ind_top_query(price,dine_rating):
                    top_query2 = df.loc[(df["Dining_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Dining_Votes", ascending=False).head(20)
                    top_query_2_all =df.loc[(df["Dining_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Dining_Votes", ascending=False)
                    if price and dine_rating:        
                        # outer if
                        if top_query2.shape[0] == 0:
                            st.text("No Results Found")
                        
                        # outer elif
                        elif top_query2.shape[0] == 1:
                            online_del= st.toggle("Show only the Restaurant has online delivery") # online delivery filter
                            if online_del: # inner if for online delivery filter
                                df_top_online_del = top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes"),["Restaurant Name","City","Address","Cuisines","Average_Cost_for_two","Dining_Ratings","Dining_Votes"]]
                                if df_top_online_del.shape[0] == 0:
                                    st.text("No Results Found")
                                else:
                                    st.header(':red[Restaurants Details] :open_file_folder:')
                                    st.dataframe(df_top_online_del,hide_index= True)
                            else: # inner else  for online delivery filter
                                st.header(':red[Restaurants Details] :open_file_folder:')
                                st.dataframe(top_query2.loc[:,["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                        # outer else
                        else: 
                            st.subheader("Showing Top 20")
                            popover = st.popover("Sort items")
                            online_del= popover.toggle("Show only the Restaurant has online delivery",key= "online_del")
                            sort_by_delivery= popover.toggle("Sort by Delivery Ratings & Votes", key ="sort_by_delivery" )
                            if online_del:# inner if for online delivery filter
                                
                                if sort_by_delivery:
                                    sort_by_votes ="Delivery_Votes"
                                    sort_by_ratings = "Delivery_Ratings"
                                    top_query2 = df.loc[(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Delivery_Votes", ascending=False).head(20)
                                    top_query_2_all =df.loc[(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Delivery_Votes", ascending=False)
                                    st.info(f"sorted based on Delivery Votes and Delivery Ratings")
                                if not sort_by_delivery :
                                    sort_by_votes ="Dining_Votes"
                                    sort_by_ratings = "Dining_Ratings"
                                    st.info(f"sorted based on Dining Votes and Dining Ratings")
                                
                                duplicate_names = top_query2["Restaurant_Name"].duplicated(keep=False)
                                top_query2['Restaurant Name with Locality'] = top_query2.apply(lambda row: f"{row['Restaurant_Name']} ({row['Locality']})" if duplicate_names[row.name] else row['Restaurant_Name'], axis=1)
                                top_query2 = top_query2.sort_values(by=sort_by_votes, ascending=False)
                                top_query2_online_del = top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes")]
                                if top_query2_online_del.shape[0] == 0:
                                    st.text("No Results Found")

                                else: 
                                    top_query2_fig = px.bar(top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes")],
                                                            x = "Restaurant Name with Locality" , 
                                                            y= sort_by_votes, 
                                                            text = sort_by_ratings , 
                                                            color = sort_by_ratings,
                                                            color_continuous_scale= px.colors.sequential.Viridis)
                                    top_query2_fig.update_layout(xaxis=dict(title='Restaurant Name'), yaxis=dict(title="Votes"))
                                    top_query2_fig.update_traces(textposition = "outside")
                                    top_query2_fig.update_traces(hovertemplate="Votes: %{y}<br>Rating: %{text}")
                                    
                                    st.plotly_chart(top_query2_fig, use_container_width=True)

                                    st.header(':red[Restaurants Details] :open_file_folder:')
                                    show_all= st.toggle(f"Show All {",".join(price)} Restaurant having online delivery ")

                                    if show_all:
                                        st.dataframe(top_query_2_all.loc[(top_query_2_all["Has_Online_Delivery"] == "Yes"),["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                                    else:
                                        st.dataframe(top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes"),["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)

                            else: # inner else  for online delivery filter
                                
                                if sort_by_delivery:
                                    sort_by_votes ="Delivery_Votes"
                                    sort_by_ratings = "Delivery_Ratings"
                                    st.info(f"sorted based on Delivery Votes and Delivery Ratings")
                                    top_query2 = df.loc[(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Delivery_Votes", ascending=False).head(20)
                                    top_query_2_all =df.loc[(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))].sort_values(by="Delivery_Votes", ascending=False)
                                if not sort_by_delivery :
                                    sort_by_votes ="Dining_Votes"
                                    sort_by_ratings = "Dining_Ratings"
                                    st.info(f"sorted based on Dining Votes and Dining Ratings")

                                duplicate_names = top_query2["Restaurant_Name"].duplicated(keep=False)
                                top_query2['Restaurant Name with Locality'] = top_query2.apply(lambda row: f"{row['Restaurant_Name']} ({row['Locality']})" if duplicate_names[row.name] else row['Restaurant_Name'], axis=1)
                                top_query2['Restaurant Name with Locality'] = top_query2['Restaurant Name with Locality'] +"-" + top_query2["City"]
                                top_query2 = top_query2.sort_values(by=sort_by_votes, ascending=False)
                                top_query2_fig = px.bar(top_query2,  
                                                        x = "Restaurant Name with Locality" , 
                                                        y= sort_by_votes,
                                                        text = sort_by_ratings, 
                                                        color = sort_by_ratings,
                                                        color_continuous_scale= px.colors.sequential.Viridis)
                                top_query2_fig.update_layout(xaxis=dict(title='Restaurant Name'), yaxis=dict(title="Votes"))
                                top_query2_fig.update_traces(textposition = "outside")
                                top_query2_fig.update_traces(hovertemplate="Votes: %{y}<br>Rating: %{text}")
                            
                                st.plotly_chart(top_query2_fig, use_container_width=True)
                                st.divider() 
                                st.header(':red[Restaurants Details] :open_file_folder:')
                                show_all= st.toggle(f"Show all the {",".join(price)} restaurants")
                                if show_all:
                                    st.dataframe(top_query_2_all.loc[:,["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                                else:
                                    st.dataframe(top_query2.loc[:,["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)

                filter_container5 =  st.container(border = True) 
                filter_container5.subheader("Filter Options")
                selected_default_expander = filter_container5.expander("Quick Selection")
                default_price_options = ['Lower-Priced','Budget-Friendly','Affordable', 'Moderate','Semi-Expensive','Expensive','Luxurious']
                with selected_default_expander:
                    st.write(f"<span style='color:#ef4f5f'>Please un-check selected option to see all the options</span>", unsafe_allow_html=True)
                    if st.checkbox("Top Rated Restaurants",key= "selected_default_expander1"):
                        selected_default = default_price_options
                        selected_default_rating = ["Excellent","Very Good"]
                    elif st.checkbox("Top Rated Lower-Priced Restaurants",key= "selected_default_expander2"):
                        selected_default = default_price_options[0:2]   
                        selected_default_rating = ["Excellent","Very Good"]          
                    elif st.checkbox("Top Rated Mid-Range Restaurants",key= "selected_default_expander3"):
                        selected_default = default_price_options[2:4] 
                        selected_default_rating = ["Excellent","Very Good"]
                    elif st.checkbox("Top Rated Expensive Restaurants",key= "selected_default_expander4"):
                        selected_default = default_price_options[4:6]  
                        selected_default_rating = ["Excellent","Very Good"]   
                    elif st.checkbox("Top Rated Luxurious Restaurants",key= "selected_default_expander5"):
                        selected_default = default_price_options[6]    
                        selected_default_rating = ["Excellent","Very Good"]                                                                     
                    else:
                        selected_default = None
                        selected_default_rating = None
                
                columns = st.columns(2)
                with columns[0]:
                    price = filter_container5.multiselect("Select Pricing based on your budget",
                                    sorted(df['Cost_Category'].unique()),placeholder= "eg., Low-Priced, Expensive",  # Ensure it's a list of strings
                                    default=selected_default)
                with columns[1]:
                    dine_rating = filter_container5.multiselect("Select Rating",
                                    sorted(df['Dining_Rating_Text'].unique()), placeholder= "eg., Good, Excellent", # Ensure it's a list of strings
                                    default=selected_default_rating)
                Ind_top_query(price,dine_rating)
            
            elif ind_queries == "Search for Specific Cuisines":
                def ind_specific_cus():
                    unique_cuisines = df['Cuisines'].str.split(', ').explode().unique()
                    # Function to find the closest match for entered cuisine
                    def find_closest_match(entered_cuisine):
                        matches = difflib.get_close_matches(entered_cuisine, unique_cuisines, n=1)
                        if matches:
                            return matches[0]
                        else:
                            return None 

                    def specific_cuisine(price,dine_rating,corrected_cuisine):
                        
                        top_query2 = df.loc[(df["Dining_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price)) & (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Dining_Votes", ascending=False).head(20)
                        top_query_2_all =df.loc[(df["Dining_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Dining_Votes", ascending=False)
                        if corrected_cuisine and price and dine_rating :
                            # outer if
                            if top_query2.shape[0] == 0:
                                st.warning("No Results Found")
                            
                            # outer elif
                            elif top_query2.shape[0] == 1:
                                online_del= st.toggle("Show only the Restaurant has online delivery") # online delivery filter
                                if online_del: # inner if for online delivery filter
                                    df_top_online_del = top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes"),["Restaurant Name","City","Address","Cuisines","Average_Cost_for_two","Dining_Ratings","Dining_Votes"]]
                                    if df_top_online_del.shape[0] == 0:
                                        st.warning("No Results Found")
                                    else:
                                        st.header(':red[Restaurants Details] :open_file_folder:')
                                        st.dataframe(df_top_online_del,hide_index= True)
                                else: # inner else  for online delivery filter
                                    st.header(':red[Restaurants Details] :open_file_folder:')
                                    st.dataframe(top_query2.loc[:,["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                            # outer else
                            else: 
                                st.subheader(f"Showing 20 Restaurants")
                                popover = st.popover("Sort items")
                                online_del= popover.toggle("Show only the Restaurant has online delivery",key = "tab2ondel")
                                sort_by_delivery= popover.toggle("Sort by Delivery Ratings & Votes",key = "tab2sort_by_delivery")
                                
                                if online_del:# inner if for online delivery filter
                                    
                                    if sort_by_delivery:
                                        sort_by_votes ="Delivery_Votes"
                                        sort_by_ratings = "Delivery_Ratings"
                                        top_query2 = df.loc[(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Delivery_Votes", ascending=False).head(20)
                                        top_query_2_all =df.loc[(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Delivery_Votes", ascending=False)
                                        st.info(f"sorted based on Delivery Votes and Delivery Ratings")
                                    if not sort_by_delivery :
                                        sort_by_votes ="Dining_Votes"
                                        sort_by_ratings = "Dining_Ratings"
                                        st.info(f"sorted based on Dining Votes and Dining Ratings")
                                    
                                    duplicate_names = top_query2["Restaurant_Name"].duplicated(keep=False)
                                    top_query2['Restaurant Name with Locality'] = top_query2.apply(lambda row: f"{row['Restaurant_Name']} ({row['Locality']})" if duplicate_names[row.name] else row['Restaurant_Name'], axis=1)
                                    top_query2 = top_query2.sort_values(by=sort_by_votes, ascending=False)
                                    top_query2_online_del = top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes")]
                                    if top_query2_online_del.shape[0] == 0:
                                        st.warning("No Results Found")

                                    else: 
                                        top_query2_fig = px.bar(top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes")],
                                                                x = "Restaurant Name with Locality" , 
                                                                y= sort_by_votes, 
                                                                text = sort_by_ratings , 
                                                                color = sort_by_ratings,
                                                                color_continuous_scale= px.colors.sequential.Viridis)
                                        top_query2_fig.update_layout(xaxis=dict(title='Restaurant Name'), yaxis=dict(title="Votes"))
                                        top_query2_fig.update_traces(textposition = "outside")
                                        top_query2_fig.update_traces(hovertemplate="Votes: %{y}<br>Rating: %{text}")
                                        
                                        st.plotly_chart(top_query2_fig, use_container_width=True)

                                        st.header(':red[Restaurants Details] :open_file_folder:')
                                        show_all= st.toggle(f"Show All the Restaurants having {corrected_cuisine} having online delivery")

                                        if show_all:
                                            st.dataframe(top_query_2_all.loc[(top_query_2_all["Has_Online_Delivery"] == "Yes"),["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                                        else:
                                            st.dataframe(top_query2.loc[(top_query2["Has_Online_Delivery"] == "Yes"),["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)

                                else: # inner else  for online delivery filter
                                    if sort_by_delivery:
                                        sort_by_votes ="Delivery_Votes"
                                        sort_by_ratings = "Delivery_Ratings"
                                        st.info(f"sorted based on Delivery Votes and Delivery Ratings")
                                        top_query2 = df.loc[(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Delivery_Votes", ascending=False).head(20)
                                        top_query_2_all =df.loc[(df["Delivery_Rating_Text"].isin(dine_rating)) & (df["Cost_Category"].isin(price))& (df.Cuisines.str.contains(str(corrected_cuisine)))].sort_values(by="Delivery_Votes", ascending=False)
                                    if not sort_by_delivery :
                                        sort_by_votes ="Dining_Votes"
                                        sort_by_ratings = "Dining_Ratings"
                                        st.info(f"sorted based on Dining Votes and Dining Ratings")

                                    duplicate_names = top_query2["Restaurant_Name"].duplicated(keep=False)
                                    top_query2['Restaurant Name with Locality'] = top_query2.apply(lambda row: f"{row['Restaurant_Name']} ({row['Locality']})" if duplicate_names[row.name] else row['Restaurant_Name'], axis=1)
                                    top_query2 = top_query2.sort_values(by=sort_by_votes, ascending=False)
                                    top_query2['Restaurant Name with Locality'] = top_query2['Restaurant Name with Locality'] +"-"+ top_query2["City"]
                                    top_query2_fig = px.bar(top_query2,  
                                                            x = "Restaurant Name with Locality" , 
                                                            y= sort_by_votes,
                                                            text = sort_by_ratings, 
                                                            color = sort_by_ratings,
                                                            color_continuous_scale= px.colors.sequential.Viridis)
                                    top_query2_fig.update_layout(xaxis=dict(title='Restaurant Name'), yaxis=dict(title="Votes"))
                                    top_query2_fig.update_traces(textposition = "outside")
                                    top_query2_fig.update_traces(hovertemplate="Votes: %{y}<br>Rating: %{text}")
                                
                                    st.plotly_chart(top_query2_fig, use_container_width=True)
                                    st.divider() 
                                    st.header(':red[Restaurants Details] :open_file_folder:')
                                    show_all= st.toggle(f"Show All the Restaurants having {corrected_cuisine}")
                                    if show_all:
                                        st.dataframe(top_query_2_all.loc[:,["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                                    else:
                                        st.dataframe(top_query2.loc[:,["Restaurant_Name","City","Address","Cuisines","Average_Cost_For_Two","Has_Online_Delivery","Dining_Ratings","Dining_Votes","Delivery_Ratings","Delivery_Votes","Contact_Number","Restaurant_Url"]],hide_index= True)
                        
                        else:
                            st.info("Please select all the above options")
                    
                    filter_container6 =  st.container(border = True) 
                    st.markdown("Type the Cuisine in your mind")
                    entered_cuisine = st.text_input(label="Enter the cuisine", placeholder="e.g., Biryani", max_chars= 15)
                    st.markdown("OR select from below")
                    ind_cusine_dropbox = st.selectbox("Select the first cuisine", sorted([i for i in unique_cuisines if i not in ["Afghan","Beverages,"] ]),index = None)
                    if entered_cuisine and "," in entered_cuisine :
                        st.error("Please don't add more than one cuisine for best results")
                    
                    if entered_cuisine or ind_cusine_dropbox:
                    # Perform auto-correction
                        if ind_cusine_dropbox:
                            corrected_cuisine = ind_cusine_dropbox
                        else:
                            corrected_cuisine = find_closest_match(entered_cuisine) 
                        if corrected_cuisine:
                            filter_container5c = st.container(border=True)
                            filter_container5c.markdown('Filter Options')
                            selected_default_expander = filter_container5c.expander("Quick Selection")
                            default_price_options = ['Lower-Priced','Budget-Friendly','Affordable', 'Moderate','Semi-Expensive','Expensive','Luxurious']
                            with selected_default_expander:
                                st.write(f"<span style='color:#ef4f5f'>Please un-check selected option to see all the options</span>", unsafe_allow_html=True)
                                if st.checkbox("Top Rated Restaurants",key= "selected_default_expander1"):
                                    selected_default = default_price_options
                                    selected_default_rating = ["Excellent","Very Good"]   
                                elif st.checkbox("Top Rated Lower-Priced Restaurants",key= "selected_default_expander2"):
                                    selected_default = default_price_options[0:2]   
                                    selected_default_rating = ["Excellent","Very Good"]   
                                elif st.checkbox("Top Rated Mid-Range Restaurants",key= "selected_default_expander3"):
                                    selected_default = default_price_options[2:4] 
                                    selected_default_rating = ["Excellent","Very Good"]   
                                elif st.checkbox("Top Rated Expensive Restaurants",key= "selected_default_expander4"):
                                    selected_default = default_price_options[4:6] 
                                    selected_default_rating = ["Excellent","Very Good"]       
                                elif st.checkbox("Top Rated Luxurious Restaurants",key= "selected_default_expander5"):
                                    selected_default = default_price_options[6]  
                                    selected_default_rating = ["Excellent","Very Good"]                                                                          
                                else:
                                    selected_default = None      
                                    selected_default_rating = None
                                                                 
                            price = filter_container5c.multiselect("Select Pricing",
                                        sorted(df['Cost_Category'].unique()),  # Ensure it's a list of strings
                                        default=selected_default,key="ins_tab2_fn_pricing_multiselect")
                            dine_rating = filter_container5c.multiselect("Select Rating",
                                        sorted(df['Dining_Rating_Text'].unique()),  # Ensure it's a list of strings
                                        default=selected_default_rating,key="ins_tab2_fn_rating_multiselect")
                            specific_cuisine(price,dine_rating,corrected_cuisine)
                        
                        else:
                            st.warning("No Results Found")
                    else:
                        st.info("Please enter valid cuisine name")
                ind_specific_cus()                
            elif ind_queries == "Compare Cuisines":


                def compare_cuisines():
                    st.header("Compare Cuisines")
                    unique_cuisines = df['Cuisines'].str.split(', ').explode().unique()

                    # User input for selecting two cuisines to compare
                    cuisine_1 = st.selectbox("Select the first cuisine", sorted([i for i in unique_cuisines if i not in ["Afghan","Beverages,"] ]),index = None)
                    cuisine_2 = st.selectbox("Select the second cuisine", sorted([i for i in unique_cuisines if i not in ["Afghan","Beverages,"] ]),index = None)

                    
                    if cuisine_1 and cuisine_2:
                        st.subheader(f"Comparing {cuisine_1} vs {cuisine_2}")
                        
                        # Filter data for each cuisine
                        df_cuisine_1 = df[df['Cuisines'].str.contains(cuisine_1, case=False)]
                        df_cuisine_2 = df[df['Cuisines'].str.contains(cuisine_2, case=False)]
                        
                        # Calculate statistics for each cuisine
                        stats_cuisine_1 = {
                            "Average Cost for Two": df_cuisine_1['Average_Cost_For_Two'].mean(),
                            "Average Dining Rating": df_cuisine_1['Dining_Ratings'].mean(),
                            "Average Delivery Rating": df_cuisine_1['Delivery_Ratings'].mean(),
                            "Number of Restaurants": df_cuisine_1.shape[0]
                        }
                        
                        stats_cuisine_2 = {
                            "Average Cost for Two": df_cuisine_2['Average_Cost_For_Two'].mean(),
                            "Average Dining Rating": df_cuisine_2['Dining_Ratings'].mean(),
                            "Average Delivery Rating": df_cuisine_2['Delivery_Ratings'].mean(),
                            "Number of Restaurants": df_cuisine_2.shape[0]
                        }
                        
                        com_cus_cont_1 = st.container(border=True)
                        com_cus_cont_2 = st.container(border=True)
                        # Display statistics
                        with com_cus_cont_1:
                            st.write(f"**{cuisine_1} Statistics:**")
                            for key, value in stats_cuisine_1.items():
                                st.write(f"{key}: {value:.2f}")
                        with com_cus_cont_2:
                            st.write(f"**{cuisine_2} Statistics:**")
                            for key, value in stats_cuisine_2.items():
                                st.write(f"{key}: {value:.2f}")
                        
                        # Plot price distribution
                        st.subheader(f"Price Distribution")
                        bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000, 2500, 3000, 4000, 5000, float('inf')]
                        labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500',
                                    '500-600', '600-700', '700-800', '800-900', '900-1000', '1000-1250', '1250-1500', '1500-1750', '1750-2000',
                                    '2000-2500', '2500-3000', '3000-4000', '4000-5000', '5000+']
                        df_price_dist = pd.DataFrame({
                            'Price Range': pd.cut(df['Average_Cost_For_Two'], bins=bins, labels=labels, right=False),
                            'Cuisine': df['Cuisines'].apply(lambda x: cuisine_1 if cuisine_1 in x else (cuisine_2 if cuisine_2 in x else None))
                        }).dropna()
                        df_price_dist = df_price_dist.sort_values(by= "Price Range")
                        price_dist_fig = px.histogram(df_price_dist, x='Price Range', color='Cuisine', barmode='group',color_discrete_sequence=px.colors.qualitative.Vivid,
                                                    title=f"Price Distribution of {cuisine_1} vs {cuisine_2}", labels={"Price Range": "Amount (₹)", "count": "% of orders"})
                        st.plotly_chart(price_dist_fig, use_container_width=True)
                        
                        # Plot rating distribution
                        st.subheader("Rating Distribution")
                        df_rating_dist = pd.melt(df[df['Cuisines'].str.contains(f"{cuisine_1}|{cuisine_2}", case=False)], 
                                                id_vars=['Cuisines'], 
                                                value_vars=['Dining_Ratings', 'Delivery_Ratings'], 
                                                var_name='Rating Type', 
                                                value_name='Rating')

                        df_rating_dist['Cuisine'] = df_rating_dist['Cuisines'].apply(lambda x: cuisine_1 if cuisine_1 in x else (cuisine_2 if cuisine_2 in x else None)).dropna()
                        rating_dist_fig = px.histogram(df_rating_dist, x='Rating', color='Cuisine', barmode='group', 
                                                    facet_row='Rating Type', color_discrete_sequence=px.colors.qualitative.Vivid,
                                                    title="Rating Distribution of Dining Ratings & Delivery Ratings", labels={"count": "% of orders"})
                        st.plotly_chart(rating_dist_fig, use_container_width=True)
                        
                    # else:
                    #     if not cuisine_1:
                    #         st.warning(f"No close match found for the first cuisine: {entered_cuisine_1}")
                    #     if not cuisine_2:
                    #         st.warning(f"No close match found for the second cuisine: {entered_cuisine_2}")
                    else:
                        st.warning("Please select both cuisines to compare.")


                compare_cuisines()


            elif ind_queries == "Cost Vs Ratings":
                def ind_costvsratings():
                    city_data = df
                    # Define the order of cost categories
                    cost_order = ['Lower-Priced', 'Budget-Friendly', 'Affordable', 'Moderate', 'Semi-Expensive', 'Expensive','Luxurious']

                    # Group by Cost_Category and calculate mean ratings
                    ratings_by_cost = city_data.groupby('Cost_Category').agg({
                        'Dining_Ratings': 'mean',
                        'Delivery_Ratings': 'mean'
                    }).reindex(cost_order)

                    # Reset index to ensure proper ordering
                    ratings_by_cost.reset_index(inplace=True)
                
                    # Melt the dataframe to long format for line chart
                    ratings_by_cost_melted = pd.melt(ratings_by_cost, id_vars=['Cost_Category'], var_name='Rating Type', value_name='Average Rating')
                    ratings_by_cost_melted['Average Rating'] = ratings_by_cost_melted['Average Rating'].round(2)

                    with st.expander("Why Delivery Rating is falling contionusly?"):
                        st.markdown("<p style='color:red'>The reason why delivery ratings decrease after the moderate price categories is because many expensive and luxurious restaurants don't provide online delivery services.</p>", unsafe_allow_html=True)

                        delivery_counts = city_data.groupby('Cost_Category')['Has_Online_Delivery'].value_counts(normalize=True).unstack().fillna(0)
                        delivery_counts = delivery_counts.reindex(cost_order)
                        delivery_counts["Yes"] = delivery_counts["Yes"].round(2)
                        delivery_counts["No"] = delivery_counts["No"].round(2)


                        # Plotting
                        fig1 = px.bar(delivery_counts, x=delivery_counts.index, y=['Yes', 'No'],
                                    title=f'Proportion of Restaurants with Online Delivery',
                                    labels={'value': 'Proportion', 'variable': 'Has Online Delivery'},
                                    category_orders={'index': cost_order}, barmode='stack', color_discrete_map={'Yes': 'green', 'No': 'red'})

                        fig1.update_layout(xaxis={'title': 'Cost Category'}, yaxis={'title': 'Proportion'})
                        st.plotly_chart(fig1,use_container_width= True)                
                    # Plotting
                    fig = px.line(ratings_by_cost_melted, x='Cost_Category', y='Average Rating', color='Rating Type',
                                title='Cost vs. Ratings Analysis', labels={'Average Rating': 'Average Rating'},
                                category_orders={'Cost_Category': cost_order},color_discrete_sequence=px.colors.qualitative.Vivid ,markers=True)
                    fig.update_layout(xaxis={'categoryorder': 'array', 'categoryarray': cost_order})
                    fig.update_traces(hovertemplate="Cost Category: %{x}<br>Average Rating: %{y}")

                    with st.expander("Detailed Explanation of Cost vs. Ratings"):
                        st.markdown("""
                        **Description**:
                        This insight examines the relationship between the cost of dining and delivery ratings for restaurants. The data highlights how different price categories affect customer ratings for dining and delivery experiences.

                        **Interpretation**:
                        1. **Dining Ratings**:
                        - **Increasing Trend with Cost**: Dining ratings generally improve as the cost increases, with luxurious restaurants receiving the highest ratings (4.2). This suggests that customers tend to perceive higher-priced restaurants as providing better dining experiences.

                        2. **Delivery Ratings**:
                        - **Inverse Relationship with Cost**: Delivery ratings peak at budget-friendly (3.3) and affordable (3.2) categories, but significantly decline for higher-priced categories. This is most evident in luxurious restaurants, which have a delivery rating of 0.0, indicating no delivery service.

                        3. **Divergence in Ratings**:
                        - As prices increase, the gap between dining and delivery ratings becomes more obvious. Semi-expensive and expensive restaurants maintain high dining ratings (4.1) but have lower delivery ratings (2.4 and 1.7, respectively). This indicates a potential gap in service expectations and availability between dining in and ordering out from higher-end restaurants.

                        **Implications**:
                        - **Service Strategy**: Restaurants, particularly those in higher price categories, might need to evaluate their delivery services. Enhancing delivery quality or offering delivery options could improve customer satisfaction.
                        - **Customer Expectations**: Customers might associate higher dining costs with better in-house experiences but not necessarily with superior delivery services. Restaurants should manage expectations accordingly.
                        - **Market Opportunities**: There is an opportunity for budget-friendly and affordable restaurants to capitalize on their relatively high delivery ratings by expanding their delivery operations and enhancing service quality.

                        **Conclusion**:
                        The analysis of cost versus ratings reveals key patterns in customer perceptions of dining and delivery experiences. While dining ratings improve with increasing costs, delivery ratings tend to decrease, especially in the higher price categories where delivery services are less common or non-existent.

                        **Recommendations**:
                        - **Enhance Delivery Services**: High-end restaurants should consider investing in improving their delivery services or introducing them if not already available.
                        - **Focus on Quality**: Budget-friendly and affordable restaurants should continue to focus on the quality of their delivery services to maintain and improve their ratings.
                        - **Customer Communication**: Clearly communicate the availability and quality of delivery services to manage customer expectations, especially for higher-priced establishments.
                        """)


                    st.plotly_chart(fig,use_container_width= True)
                ind_costvsratings()                

            elif ind_queries == "Cuisine Filter by Ratings & Costs":
                    
                def ind_cusines_analyzer1(min_rating,pricing):
                    if pricing:
                        tab1,tab2 = st.tabs(["Chart", "Data"])
                        with tab1:
                            st.subheader(f"Showing Popular Cuisines in :red[India]")
                            popover = st.popover("Sort items")
                            sort_delivery =  popover.toggle("Filter Based on Delivery Ratings & Votes",key="tab3cusana1sortdel")
                            if sort_delivery:
                                c_analyzer_df_1 = df.loc[(df.Delivery_Ratings >= min_rating)&(df.Cost_Category.isin(pricing))].sort_values(by="Delivery_Votes",ascending = False)
                                c_analyzer_df_1 =c_analyzer_df_1['Cuisines'].str.split(', ').explode().value_counts().reset_index()
                                c_analyzer_df_1.columns = ['Cuisines', 'Count']  
                            else:
                                c_analyzer_df_1 = df.loc[(df.Dining_Ratings >= min_rating) & (df.Cost_Category.isin(pricing))].sort_values(by="Dining_Votes",ascending = False)
                                c_analyzer_df_1 = c_analyzer_df_1['Cuisines'].str.split(', ').explode().value_counts().reset_index()
                                c_analyzer_df_1.columns = ['Cuisines', 'Count']            

                            
                            if c_analyzer_df_1.shape[0] == 0:
                                st.warning("No Results Found")
                            
                            elif c_analyzer_df_1.shape[0] == 1:
                                st.plotly_chart(c_analyzer_df_1_fig, use_container_width=True) 
                            
                            else:
                                c_analyzer_df_1_fig = px.bar(c_analyzer_df_1.head(10),
                                                            x = "Cuisines",
                                                            y = "Count",
                                                            text = "Count", 
                                                            color = "Count",
                                                            color_continuous_scale= px.colors.sequential.Viridis)
                                c_analyzer_df_1_fig.update_layout(xaxis=dict(title='Cuisines'), yaxis=dict(title="Restaurant Count"))
                                c_analyzer_df_1_fig.update_traces(textposition = "outside")
                                c_analyzer_df_1_fig.update_traces(hovertemplate="Cuisines: %{x}<br>Restaurant Count: %{y}")
                                st.plotly_chart(c_analyzer_df_1_fig, use_container_width=True) 
                        with tab2:
                            if c_analyzer_df_1.shape[0] >1:
                                st.header(':red[Data] :open_file_folder:')
                                c_analyzer_df_1_show_all = st.toggle(f"Show all Cuisines and It's Restaurant Count")
                                if c_analyzer_df_1_show_all:
                                    st.dataframe(c_analyzer_df_1,hide_index = True)             
                                else:
                                    st.dataframe(c_analyzer_df_1.head(20),hide_index = True)
                            
                            else: 
                                st.warning("No Results Found")

                filter_container4 =  st.container(border = True) 
                filter_container4.subheader(':red[Filter Options] :slot_machine:')
                col1, col2 =  filter_container4.columns(2)  

                selected_default_expander = filter_container4.expander("Quick Selection")
                default_price_options = ['Lower-Priced','Budget-Friendly','Affordable', 'Moderate','Semi-Expensive','Expensive','Luxurious']
                with selected_default_expander:
                    st.write(f"<span style='color:#ef4f5f'>Please un-check selected option to see all the options</span>", unsafe_allow_html=True)
                    if st.checkbox("Lower-Priced Cuisines",key= "selected_default_expander2"):
                        selected_default = default_price_options[0:2]     
                    elif st.checkbox("Mid-Range Cuisines",key= "selected_default_expander3"):
                        selected_default = default_price_options[2:4]  
                    elif st.checkbox("Expensive Cuisines",key= "selected_default_expander4"):
                        selected_default = default_price_options[4:6]   
                    elif st.checkbox("Luxurious Cuisines",key= "selected_default_expander5"):
                        selected_default = default_price_options[6]                                                                                      
                    else:
                        selected_default = None      
            
                with col1:
                # Define the rating slider
                    min_rating = st.slider("Select Minimum Rating", min_value=0, max_value=5, step=1, value=0)
                    st.write("Your selected ratings:", f"<span style='color:#ef4f5f'>{min_rating}⭐ & Up</span>", unsafe_allow_html=True)
                with col2:
                    pricing = st.multiselect("Select Pricing",
                                    sorted(df['Cost_Category'].unique()),  # Ensure it's a list of strings
                                    default=selected_default)
                ind_cusines_analyzer1(min_rating,pricing)
            
            elif ind_queries == "Popular Cuisine Combinations":

                def count_cuisine_combinations(df):
                    cuisine_combinations = Counter()

                    for cuisines in df['Cuisines']:
                        cuisine_list = cuisines.split(', ')
                        # Filter out single cuisines
                        if len(cuisine_list) > 1:
                            # Generate all possible combinations of cuisines for each restaurant
                            for r in range(2, len(cuisine_list) + 1):  # Minimum combination length is 2
                                combinations_list = combinations(cuisine_list, r)
                                for combination in combinations_list:
                                    sorted_combination = sorted(combination)
                                    cuisine_combinations[tuple(sorted_combination)] += 1

                    return cuisine_combinations

                # Count cuisine combinations
                cuisine_counts = count_cuisine_combinations(df)

                # Get top 10 cuisine combinations
                top_n = 10
                top_cuisines = dict(sorted(cuisine_counts.items(), key=lambda x: x[1], reverse=True)[:top_n])

                # Create DataFrame for top cuisines
                top_df = pd.DataFrame({
                    'Cuisine Combinations': [", ".join(combination) for combination in top_cuisines.keys()],
                    'Frequency': list(top_cuisines.values())
                })

                # Plot using Plotly Express
                fig = px.bar(top_df, y='Frequency', x='Cuisine Combinations',  
                             title='Top {} Popular Cuisine Combinations'.format(top_n),
                             color = 'Frequency',
                              color_continuous_scale= px.colors.sequential.Viridis)

                with st.expander("Detailed Explanation of top 10 Popular Cuisine Combinations"):
                    st.markdown("""
                    **Description**:
                    This insight identifies the top 10 combinations of cuisines offered by restaurants on Zomato, revealing prevalent culinary pairings that customers commonly enjoy together.

                    **Interpretation**:
                    1. **Consumer Preferences and Pairing Habits**:
                    - The dominance of **Chinese & North Indian** (7129 restaurants) suggests a blend of diverse tastes, catering to both Indian and Chinese cuisine enthusiasts.
                    - **Beverages & North Indian** (4569 restaurants) and **Beverages & Desserts** (4425 restaurants) reflect common preferences for accompanying main courses with drinks or sweet endings.

                    2. **Cross-Cultural Dining Trends**:
                    - Combinations like **Beverages & Chinese** (4255 restaurants) and **Beverages & Fast-food** (4238 restaurants) highlight a global dining trend where beverages are paired with quick-service or international dishes, appealing to a wide audience.

                    3. **Regional and Traditional Influences**:
                    - **Biryani & North Indian** (3272 restaurants) underscores the popularity of traditional Indian cuisines together, indicating a strong regional preference and culinary tradition.

                    **Implications**:
                    - **Menu Optimization**: Restaurants can strategically feature these popular combinations to attract and satisfy customer expectations, potentially increasing sales and customer loyalty.
                    - **Marketing Strategy**: Promoting these combinations can enhance menu visibility and customer engagement, driving interest and foot traffic.
                    - **Operational Efficiency**: Understanding these preferences can streamline inventory management and operational processes, ensuring consistent availability of popular pairings.

                    **Conclusion**:
                    Analyzing the top cuisine combinations on Zomato provides valuable insights into consumer dining habits and preferences. By leveraging this data, restaurants can tailor their offerings to better meet customer demand, ultimately enhancing the overall dining experience.

                    **Recommendations**:
                    - **Promotional Campaigns**: Develop targeted promotions around popular combinations to capitalize on customer preferences.
                    - **Menu Innovation**: Continuously monitor trends and consider introducing new combinations to keep offerings fresh and appealing.
                    - **Quality Assurance**: Ensure consistent quality and presentation of popular pairings to maintain customer satisfaction and loyalty.
                    """)

               
                st.plotly_chart(fig,use_container_width=True)


if selected == "REPORT":
    # Function to fetch file content from URL
    def fetch_file_content(url):
        response = requests.get(url)
        return response.content

    # URL to the PDF file on GitHub (raw link)
    pdf_url = "https://github.com/navinds/Zomato-Data-Analysis-and-Visualization/raw/main/Media/fine_dine_report.pdf"

    # Fetch the PDF file from the URL
    pdf_content = fetch_file_content(pdf_url)
    reportcol1,reportcol1a,reportcol2 ,reportcol3= st.columns([1,0.5,0.5,1])
    with reportcol1a:
        st.image("https://raw.githubusercontent.com/navinds/Zomato-Data-Analysis-and-Visualization/main/Media/1.png",width = 400)

    with reportcol2:
        # Add a download button for the PDF file
        st.text("")
        st.download_button(
            label="Download PDF",
            data=pdf_content,
            file_name="fine_dine_report.pdf",
            mime="application/pdf",
        )
