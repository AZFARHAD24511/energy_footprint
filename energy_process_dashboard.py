import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Energy Process Explorer")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('df_energy.csv')  # Ensure this CSV is in the app directory
    # Filter out negative inputs
    df = df[df['Energy_Input_for_production'] >= 0]
    return df

df = load_data()

# User input for keyword
keyword = st.text_input("Enter keyword to filter processes", value="electricity")

if keyword:
    # Filter processes containing the keyword (case-insensitive)
    mask = df['Product'].str.contains(keyword, case=False, na=False)
    filtered = df[mask]

    st.subheader(f"Processes matching '{keyword}' ({len(filtered)})")
    if filtered.empty:
        st.write("No processes found for this keyword.")
    else:
        # Display table
        st.dataframe(filtered[['Product', 'Energy_Input_for_production', 'Energy_Content_MJ_per_unit']])

        # Plot bar chart for Energy Input
        st.markdown("**Energy Input for Production**")
        fig, ax = plt.subplots()
        ax.barh(filtered['Product'], filtered['Energy_Input_for_production'])
        ax.set_xlabel('Energy Input (MJ)')
        ax.set_ylabel('Process')
        ax.invert_yaxis()
        st.pyplot(fig)

        # Plot bar chart for Energy Content
        st.markdown("**Energy Content per Unit**")
        fig2, ax2 = plt.subplots()
        ax2.barh(filtered['Product'], filtered['Energy_Content_MJ_per_unit'])
        ax2.set_xlabel('Energy Content (MJ)')
        ax2.set_ylabel('Process')
        ax2.invert_yaxis()
        st.pyplot(fig2)

