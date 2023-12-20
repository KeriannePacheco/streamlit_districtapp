import streamlit as st 
import pandas as pd 
import numpy as np
import plotly.express as px

st.title("District RSS Quadrant")

st.markdown("Analyzed 12 months of lead and conversion data across the Eastern and Western Recruiting Region substations through FY23")
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
st.markdown("The goal of this analysis was to expose the outlier substations within each recruiting station that would benefit from a separate strategic plan rather than following the same strategy as the overall recruiting station")