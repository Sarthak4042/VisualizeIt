import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Title of your Streamlit app
st.title('VisualizeIt - Data Visualization App')

# Upload CSV file and process
uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Group by category and count the products
    category_count = df['Product line'].value_counts().reset_index()
    category_count.columns = ['Product line', 'total_products']
    # Plotting for product line
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=category_count, x='Product line', y='total_products')
    plt.xlabel('Product line')
    plt.ylabel('Total Products Sold')
    plt.title('Total Products Sold per Category')
    plt.xticks(rotation=45)
    st.pyplot(fig_category) # Save plots to static files
    plot_path = os.path.join('static', 'plot_streamlit.png')
    fig_category.savefig(plot_path)

    # Plotting products sold per branch
    branch_count = df['Branch'].value_counts().reset_index()
    branch_count.columns = ['Branch', 'total_products']        
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=branch_count, x='Branch', y='total_products')
    plt.xlabel('Branch')
    plt.ylabel('Products Sold')
    plt.title('Products Sold per Branch')
    plt.xticks(rotation=45)
    st.pyplot(fig_category) # Save plots to static files
    plot_path_branch = os.path.join('static', 'plot_branch.png')
    plt.savefig(plot_path_branch)

    # Plotting products sold per city
    city_count = df['City'].value_counts().reset_index()
    city_count.columns = ['City', 'total_products']
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=city_count, x='City', y='total_products')
    plt.xlabel('City')
    plt.ylabel('Products Sold')
    plt.title('Products Sold per City')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_city = os.path.join('static', 'plot_city.png')
    plt.savefig(plot_path_city)

    # Plotting products sold per date
    date_count = df['Date'].value_counts().reset_index()
    date_count.columns = ['Date', 'total_products']        
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=date_count, x='Date', y='total_products')
    plt.xlabel('Date')
    plt.ylabel('Products Sold')
    plt.title('Products Sold per Date')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_date = os.path.join('static', 'plot_date.png')
    plt.savefig(plot_path_date)

        # Plotting products sold per payment method
    pm_count = df['Payment'].value_counts().reset_index()        
    pm_count.columns = ['Payment', 'total_products']
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=pm_count, x='Payment', y='total_products')
    plt.xlabel('Payment Method')
    plt.ylabel('Products Sold')
    plt.title('Products Sold per Payment Method')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_pm = os.path.join('static', 'plot_pm.png')
    plt.savefig(plot_path_pm)

    # Plotting for cogs
    plot_cogs = df['Product line'].value_counts().reset_index()
    plot_cogs.columns = ['Product line', 'cogs']
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_cogs, x='Product line', y='cogs')
    plt.xlabel('Product Category')
    plt.ylabel('COGS')
    plt.title('COGS per Product Category')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_cogs = os.path.join('static', 'plot_cogs.png')
    plt.savefig(plot_path_cogs)

    # Plotting for gross margin
    plot_cogs = df['Product line'].value_counts().reset_index()
    plot_cogs.columns = ['Product line', 'gross income']
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_cogs, x='Product line', y='gross income')
    plt.xlabel('Product Category')
    plt.ylabel('Gross Income')
    plt.title('Gross Income per Product Category')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_gross = os.path.join('static', 'plot_gross.png')
    plt.savefig(plot_path_gross)

    # Plotting for ratings
    plot_rating = df['Product line'].value_counts().reset_index()
    plot_rating.columns = ['Product line', 'Rating']
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_rating, x='Product line', y='Rating')
    plt.xlabel('Product Category')
    plt.ylabel('Rating')
    plt.title('Ratings per Product Category')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_rating = os.path.join('static', 'plot_rating.png')
    plt.savefig(plot_path_rating)

    # Plotting for unit price
    plot_unit = df['Product line'].value_counts().reset_index()
    plot_unit.columns = ['Product line', 'Unit price']
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_unit, x='Product line', y='Unit price')
    plt.xlabel('Product Category')
    plt.ylabel('Unit price')
    plt.title('Unit Price per Product Category')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_unit = os.path.join('static', 'plot_unit.png')
    plt.savefig(plot_path_unit)

    # Plotting for gender
    plot_gender = df['Gender'].value_counts().reset_index()
    plot_gender.columns = ['Gender', 'total_products']
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_gender, x='Gender', y='total_products')
    plt.xlabel('Gender')
    plt.ylabel('Total products sold')
    plt.title('Gender of customers')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_gender = os.path.join('static', 'plot_gender.png')
    plt.savefig(plot_path_gender)

    # Plotting for customer type
    plot_type = df['Customer type'].value_counts().reset_index()
    plot_type.columns = ['Customer type', 'total_products']
    fig_category = plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_type, x='Customer type', y='total_products')
    plt.xlabel('Product Category')
    plt.ylabel('Total products sold')
    plt.title('Types of customers')
    plt.xticks(rotation=45)
    st.pyplot(fig_category)
    plot_path_type = os.path.join('static', 'plot_type.png')
    plt.savefig(plot_path_type)

    # Display the plot in Streamlit
    #st.image(plot_path, caption='Total Products Sold per Category', use_column_width=True)
    #st.image(plot_path_branch, caption='Products Sold per Branch', use_column_width=True)
    #st.image(plot_path_city, caption='Products Sold per City', use_column_width=True)
    #st.image(plot_path_date, caption='Products Sold per Date', use_column_width=True)
    #st.image(plot_path_pm, caption='Products Sold per Payment Method', use_column_width=True)
    #st.image(plot_path_cogs, caption='COGS per Product Category', use_column_width=True)
    #st.image(plot_path_gross, caption='Gross Income per Product Category', use_column_width=True)
    #st.image(plot_path_rating, caption='Ratings per Product Category', use_column_width=True)
    #st.image(plot_path_unit, caption='Unit Price per Product Category', use_column_width=True)
