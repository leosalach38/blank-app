
import streamlit as st
from PIL import Image
import pandas as pd
import plost
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Student Performance EDA")
st.write("by:  ***Leo Salach***")





st.write("---")
st.subheader("Deriving a Complete Perspective from Qualitative and Quantitative Data")
st.write(" Data serves as a powerful tool for identifying trends and relationships, but it is incapable of telling the full story on its own. While the analysis of data can reveal patterns, it often lacks the analytical depth necessary to capture the complexities of real-world scenarios. Context, qualitative data, and external factors must complement quantitative data to bridge logical gaps and provide a more comprehensive and accurate understanding. Without these additional factors, conclusions derived solely from data risk being incomplete or misleading.")

st.write("---")
st.header("Test/Quiz Performance")


df = pd.read_csv("tests.csv")

st.write("Sample Data")

with st.expander("View Table"):
    st.write("Grades")
    st.dataframe(df)


x_col = "test/quiz"
# Filter out the x-axis column from the y-axis dropdown
y_columns = df.columns[df.columns != x_col]
y_cols = st.multiselect("Continous Variables Affecting Test and Quiz Scores", y_columns)

fig = go.Figure()

# Add a line for each selected y-axis variable
for y_col in y_cols:
    fig.add_trace(go.Scatter(x=df[x_col], y=df[y_col], mode='lines+markers', name=y_col))

fig.update_layout(title="Overlay of Selected Variables", xaxis_title=x_col, yaxis_title="Values")

st.plotly_chart(fig)
st.subheader("Overlay Description")
st.write("The table above overlays up to two continuous variables (time studied and confidence). Demonstrating their effect on test and quiz scores from various classes")
st.write("---")

st.title("Statistical Analysis Using Pearson's Correlation Coefficient")
st.write("Pearson’s correlation coefficient is a statistical measure that not only evaluates the strength but also direction of the relationship between two continuous variables. It is significant in this study because it quantifies the strength of the relationship between time studied and confidence’s effects on student performance.")
st.write("Pearson’s correlation coefficient ranges from -1 to 1. A value of 1 indicates a perfect positive correlation, meaning that as one variable increases, the other variable also increases. A value of -1 indicates a perfect negative correlation, meaning that as one variable increases, the other variable decreases. A value of 0 indicates no correlation between the two variables.")



df = pd.read_csv("tests.csv")

with st.expander("View Table"):
    st.header("Grades Data")
    st.dataframe(df)

# Calculate Pearson Correlation Coefficient
st.header("Pearson's Correlation Coefficient (r) ")

st.image ("Correlation-Coefficient.png")

st.write("Xᵢ = Total amount of x variable (sum of Grades as a percentage ie. 98+100+95…)")
# Insert an image
st.write("Yᵢ = Total amount of y variable(Total Time Studied)")

st.write("r = Pearson’s Correlation Coefficient")

st.write("Σ = Summation of the values")

st.write("N = Total number of data points ")

st.write("X̄  = Mean of the x values in the data set (Grades as a Percentage)")

st.write("Ȳ  = Mean of the y values in the data set (Total Time Studied)")

st.write("The Numerator computes the covariance of the X and Y variables. In other words, it determines if the variables are related or if a change in one variable results in a change of the other.")

st.write("The Denominator computes the standard deviation of the X and Y variables. In other words, it determines how much the variables vary from their mean. The denominator is used to normalize the covariance, which allows for a more accurate comparison of the strength of the relationship between the two variables.")

st.write("---")

st.subheader("")

# Select only numerical columns for correlation
numerical_columns = df.select_dtypes(include=['number']).columns

if len(numerical_columns) < 2:
    st.write("Not enough numerical columns to calculate correlation.")
else:
    # Compute the correlation matrix
    correlation_matrix = df[numerical_columns].corr(method='pearson')

    # Display the correlation matrix
    
   


    # Plot the heatmap
st.subheader("Correlation Heatmap")


st.write("The heat map is a visual representation of the correlation between the three continuous variables: Time Studied, Grade as a Percentage, and Confidence. Using the color gradient to illustrate the strength and direction of the relationships between these variables, the heat map gives a visual representation of the variables' influence on one another.")


fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

   


st.write("---")

st.header("Analysis of the Correlation")

st.write(" The analysis indicates an insignificant correlation between time studied and grades despite the undeniable logical correlation between the two. Data expresses trends and relationships but often fails to express causation. Data fails to account for factors such as learning styles, quality of study time, prior knowledge and more. Because of this, the numerical relationship between time studied and grades is not an accurate depiction or a true perspective of their correlation.")

st.title("Student Performance 2023-2024")
# Create two columns for displaying metrics side by side
col1, col2 = st.columns(2)

# Column 1: Display Earned Points in a box
with col1:
    st.subheader("2023-2024 Student Metrics")
    st.metric(label="Earned Points:", value="7230.5", delta="")

# Column 2: Display Assignments in a box
with col2:
    st.metric(label="Assignments:", value="505", delta="")

st.subheader("Performance by Class")

csv_files = {
    "American Literature": "Amlit.csv",
    "Chemistry": "Chem.csv",
    "Geometry": "Geo.csv",
    "Spanish": "Spanish.csv",
    "Theology": "Theo.csv",
    "Us History": "US History.csv",
    "Totals": "Totals.csv",
    
    }

selected_csv_files = st.multiselect("Select a Class", list(csv_files.keys()), default=list(csv_files.keys()))

# Create a figure for the overlay
overlay_fig = go.Figure()

# Loop through each selected CSV file and add their data to the figure
for csv_file_key in selected_csv_files:
    csv_file = csv_files[csv_file_key]
    # Load the data for the selected CSV file
    df_overlay = pd.read_csv(csv_file)

    x_col_overlay = "Month"
    if x_col_overlay not in df_overlay.columns:
        st.error(f"The column '{x_col_overlay}' is not present in the dataframe for {csv_file_key}.")
        continue

    y_columns_overlay = df_overlay.columns[df_overlay.columns != x_col_overlay]
    y_cols_overlay = st.multiselect(f"Select Performance Measurement for {csv_file_key}", y_columns_overlay, key=f"y_{csv_file_key}")

    # Add a line for each selected y-axis variable
    for y_col_overlay in y_cols_overlay:
        overlay_fig.add_trace(go.Scatter(x=df_overlay[x_col_overlay], y=df_overlay[y_col_overlay], mode='lines+markers', name=f"{csv_file_key} - {y_col_overlay}"))

overlay_fig.update_layout(title="Overlay of Performance", xaxis_title="Month", yaxis_title="Performance")

st.plotly_chart(overlay_fig)

st.write("---")


