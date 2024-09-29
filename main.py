import streamlit as st
import plotly.express as px
from backend import get_data, format_date

# Number of images per row
images_per_row = 6
# Add a title and inputs for the API
st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Select the number of forecasted days")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, 
                            y=temperatures,
                            labels={"x": "Date", "y": "Temperture (C)"})
            # Create a temperature plot
            st.plotly_chart(figure)
        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", 
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]

            # Display sky images
            for i in range(0, len(image_paths), images_per_row):
                cols = st.columns(images_per_row)  
                for col, image_path, date in zip(cols, image_paths[i:i+images_per_row], dates[i:i+images_per_row]):
                    with col:
                        st.image(image_path, width=115)
                        st.write(format_date(date))
    except KeyError:
        st.write("That place does not exist.")