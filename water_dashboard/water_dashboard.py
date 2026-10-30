import streamlit as st
import pandas as pd # data manipulation
import plotly.express as px # data visualization

# to run: streamlit run name_of_file.py
# if it doesn't work, try: python -m streamlit run name_of_file.py
st.set_page_config(
    page_title="Water Quality Dashboard",
    layout="wide"
)

st.title("Water Quality Dashboard")
st.header("CIS 3590 - Internship-Ready Software Development")
st.subheader("Marcelo Ortiz")

st.divider()

st.sidebar.header("File Upload")
st.sidebar.info("Upload a CSV file "
                "with water quality data")
uploaded_file=st.sidebar.file_uploader("Upload a CSV file",
                         type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("biscayneBay_waterquality.csv") # please use this csv file

tables, plots, maps, about = st.tabs(["Data",
                               "Charts",
                               "Maps",
                               "About"])

with tables:
    st.subheader("Raw CSV Data")
    st.markdown(
    "Browse individual observations from the loaded dataset.",
    help=(
        "Each row represents a recorded observation, and each "
        "colum a measurement or related information. "
        "  \nHover over the column headers to sort data, hide columns, etc.")
    )
    selected_columns = st.multiselect(
            "Choose columns to display",
            options=df.columns.tolist()
        )
    
    if selected_columns:
            display_df = df[selected_columns]
    else:
            display_df = df
    
    st.dataframe(display_df)
    st.caption(
            f"{len(display_df):,} observations and "
            f"{len(display_df.columns)} columns displayed."
        )

    st.subheader("Descriptive Statistics")
    st.write("Descriptive statistics for the loaded dataset")
    st.dataframe(df.describe())
    
with plots:
    st.subheader("Line Chart")
    parameter = st.selectbox("Select Line Chart Parameter",options=df.columns.tolist())
    # TODO: add all possible parameters to list of parameters in the selectbox above
    #  and dynamically change the y axis in the plot below to the selected parameter
    fig1 = px.line(df,
                   x="Time",
                   y=parameter,
                   title=f"{parameter} over Time")
    st.plotly_chart(fig1)
    st.caption(
        "Shows how the selected parameter changes over time. "
        "Use the dropdown to choose a parameter and hover over the line to see values."
    )

    fig2 = px.scatter(df,
                      x="Temperature (c)",
                      y="Salinity (ppt)",
                      title="Temperature vs Salinity")
    st.plotly_chart(fig2)
    st.caption(
    f"Recorded temperatures range from "
    f"{df['Temperature (c)'].min():.1f} to "
    f"{df['Temperature (c)'].max():.1f} °C "
    f"and salinity ranges from "
    f"{df['Salinity (ppt)'].min():.2f} to "
    f"{df['Salinity (ppt)'].max():.2f} ppt.  \n"
    "Hover over data points to see individual values."
    )

    fig3 = px.scatter_3d(df,
                         x="Longitude",
                         y="Latitude",
                         z="Total Water Column (m)",
                         color="Temperature (c)",
                         title="3D Visualization of the Bay Floor")
    fig3.update_scenes(zaxis_autorange="reversed")
    fig3.update_traces(marker_size=3)
    st.plotly_chart(fig3)
    st.caption(
        "Shows recorded water-column depth by location, with color indicating temperature. "
        "Drag to rotate the 3D view and hover over points to see their measurements."
    )

with maps:
    st.subheader("Maps")
    first_map = px.scatter_map(
        df,
        lat="Latitude",
        lon="Longitude",
        title="Vehicle Track on a Map",
        center={"lat":25.9121,"lon":-80.1371},
        zoom=16,
        color="Temperature (c)",
        color_continuous_scale="viridis")
    st.plotly_chart(first_map, height = 600)
    st.caption(
        "Shows where each reading was recorded, with colors showing temperature. "
        "Hover over a point to see its location and temperature.",
        help=(
            "Readings recorded close together can look like a line when zoomed out. "
            "Zoom in to see individual points."
        )
    )

with about:
    st.header("About this dashboard")
    st.write("" \
        "This dashboard explores water-quality data collected in "
        "Biscayne Bay or for an uploaded CSV file. Interactive tables, charts, and maps help "
        "users examine temperature, salinity, and other measurements."
        )
    st.markdown("""
        - **Data:** Browse the dataset and descriptive statistics.
        - **Charts:** Choose a parameter for the line chart. Hover over
        points to see values, and use the chart controls to zoom or pan.
        - **Maps:** Explore sampling locations, color-coded by temperature.
        - **Upload:** Use the sidebar to upload your own CSV with the same
        column names and structure as the provided dataset.
        """)

   
