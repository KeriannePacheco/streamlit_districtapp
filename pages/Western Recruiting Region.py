import streamlit as st 
import pandas as pd 
import numpy as np
import plotly.express as px

st.title("District WRR RSS Quadrant")
local_string = r"C:\Users\kpacheco\Documents\USMC\District\District WRR RSS_Index 2023.csv"
git_string = r"District WRR RSS_Index 2023.csv"

@st.cache_data 
def import_data(path):
    return pd.read_csv(path)

out_df = import_data(local_string)
#st.write(out_df)

def define_district(rs):
    """
    input: string that represents recruiting station
    output: string that represents district of recruiting station
    """
    if (rs == "ALBUQUERQUE" or rs == 'DALLAS' or rs == "DENVER" or rs == "FORT WORTH" or rs == "HOUSTON" 
        or rs == "PHOENIX" or rs == "SALT LAKE CITY" or rs == "SAN ANTONIO"):
        return "8"
    if (rs == "CHICAGO" or rs == "DES MOINES" or rs == "INDIANAPOLIS" or rs == "KANSAS CITY" or rs == "MILWAUKEE" 
        or rs == "OKLAHOMA CITY" or rs == "ST LOUIS" or rs == "TWIN CITIES"):
        return "9"
    if (rs == "LOS ANGELES" or rs == "ORANGE" or rs == "PORTLAND" or rs == "RIVERSIDE" or rs == "SACRAMENTO" 
        or rs == "SAN DIEGO" or rs == "SAN FRANCISCO" or rs == "SEATTLE"):
        return "12"
    
def clean_data(imported_data):
    df = imported_data.copy()
    df["Conversion rate"] = pd.to_numeric(df["Conversion rate"], errors="coerce")
    df = df.rename(columns={"% of total":"Percent Lead Share"})
    df = df.dropna()
    q1 = df['Conversion Rate Index'].quantile(q=0.25, interpolation='linear')
    q3 = df['Conversion Rate Index'].quantile(q=0.75, interpolation='linear')
    iqr = q3-q1
    lower_bound = q1-1.5*iqr
    upper_bound = q3+2.5*iqr
    df = df[df["Conversion Rate Index"] <= upper_bound].copy()
    df["District"] = df["RS"].apply(define_district)
    return df

clean_df = clean_data(out_df)

def visualize_data(clean_data):
    df = clean_data.copy()
    plot = px.scatter(df, x="Conversion Rate Index", y="QL Index", hover_data=["RSS","RS"], color="RS",
                  title="2023 District WRR RSS Index")
    plot.add_hline(y=100,
                annotation_text='<b>High Qualified Leads</b>',
                annotation_position='top right')
    plot.add_vline(x=100,
                annotation_text='<b>High Conversion Rate</b>',
                annotation_position='top right')
    plot.add_annotation(x=0, y=-15,
            text="Full Funnel",
            showarrow=False,
            yshift=0)
    plot.add_annotation(x=-4,y=315,
                    text="Nurture",
                    showarrow=False,
                    yshift=0)
    plot.add_annotation(x=270,y=315,
                    text="Maintain",
                    showarrow=False,
                    yshift=0)
    plot.add_annotation(x=260,y=-15,
                    text="Lead Generation",
                    showarrow=False,
                    yshift=0)
    return plot

plot = visualize_data(clean_df)
st.write(plot)

st.markdown("Substations have been categorized into four quadrants based on lead generation and conversion performance:")
st.markdown('''
            - Maintain: High Qualified Lead Index and High Conversion Index (HH)
                - Performing well in generating leads and converting those leads. Maintain the strategy set in place for these substations because the strategy has proven effective.
            - Nurture: High Qualified Lead Index/Low Conversion Index (HL)
                - Substations in the Nurture quadrant do a good job generating leads but those leads needs more nurturing to convert at a higher rate.
            - Lead Generation: Low Qualified Lead Index/High Conversion Index (LH)
                - Performing well in converting leads but need to generate more qualified leads.
            - Full Funnel: Low Qualified Lead Index/Low Conversion Index (LL)
                - Substations in the Full Funnel quadrant need to focus on generating more leads and converting at a higher rate. 
            ''')