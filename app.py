from flask import Flask
from flask import render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import os
import numpy as np

# instance of flask application
app = Flask(__name__ ,template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'csv_file' not in request.files:
        return 'No file part'
    file = request.files['csv_file']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        
        # Group by category and count the products
        category_count = df['Product line'].value_counts().reset_index()
        category_count.columns = ['Product line', 'total_products']
        
        # Plotting
        plt.figure(figsize=(10,15))
        sns.barplot(data=category_count, x='Product line', y='total_products')
        plt.xlabel('Product line')
        plt.ylabel('Total Products Sold')
        plt.title('Total Products Sold per Category')
        plt.xticks(rotation=45)
        # Set y-axis ticks in intervals of 5
        plt.yticks(np.arange(0, category_count['total_products'].max() + 5, 5))
        # Save plot to file
        plot_path = os.path.join('static', 'plot.png')
        plt.savefig(plot_path)

        # Plotting products sold per branch
        branch_count = df['Branch'].value_counts().reset_index()
        branch_count.columns = ['Branch', 'total_products']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=branch_count, x='Branch', y='total_products')
        plt.xlabel('Branch')
        plt.ylabel('Products Sold')
        plt.title('Products Sold per Branch')
        plt.xticks(rotation=45)
        plot_path_branch = os.path.join('static', 'plot_branch.png')
        plt.savefig(plot_path_branch)

        # Plotting products sold per city
        city_count = df['City'].value_counts().reset_index()
        city_count.columns = ['City', 'total_products']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=city_count, x='City', y='total_products')
        plt.xlabel('City')
        plt.ylabel('Products Sold')
        plt.title('Products Sold per City')
        plt.xticks(rotation=45)
        plot_path_city = os.path.join('static', 'plot_city.png')
        plt.savefig(plot_path_city)

        # Plotting products sold per date
        date_count = df['Date'].value_counts().reset_index()
        date_count.columns = ['Date', 'total_products']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=date_count, x='Date', y='total_products')
        plt.xlabel('Date')
        plt.ylabel('Products Sold')
        plt.title('Products Sold per Date')
        plt.xticks(rotation=45)
        plot_path_date = os.path.join('static', 'plot_date.png')
        plt.savefig(plot_path_date)

        # Plotting products sold per payment method
        pm_count = df['Payment'].value_counts().reset_index()
        pm_count.columns = ['Payment', 'total_products']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=pm_count, x='Payment', y='total_products')
        plt.xlabel('Payment Method')
        plt.ylabel('Products Sold')
        plt.title('Products Sold per Payment Method')
        plt.xticks(rotation=45)
        plot_path_pm = os.path.join('static', 'plot_pm.png')
        plt.savefig(plot_path_pm)

        # Plotting for cogs
        plot_cogs = df['Product line'].value_counts().reset_index()
        plot_cogs.columns = ['Product line', 'cogs']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=plot_cogs, x='Product line', y='cogs')
        plt.xlabel('Product Category')
        plt.ylabel('COGS')
        plt.title('COGS per Product Category')
        plt.xticks(rotation=45)
        plot_path_cogs = os.path.join('static', 'plot_cogs.png')
        plt.savefig(plot_path_cogs)

        # Plotting for gross margin
        plot_cogs = df['Product line'].value_counts().reset_index()
        plot_cogs.columns = ['Product line', 'gross income']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=plot_cogs, x='Product line', y='gross income')
        plt.xlabel('Product Category')
        plt.ylabel('Gross Income')
        plt.title('Gross Income per Product Category')
        plt.xticks(rotation=45)
        plot_path_gross = os.path.join('static', 'plot_gross.png')
        plt.savefig(plot_path_gross)

        # Plotting for ratings
        plot_rating = df['Product line'].value_counts().reset_index()
        plot_rating.columns = ['Product line', 'Rating']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=plot_rating, x='Product line', y='Rating')
        plt.xlabel('Product Category')
        plt.ylabel('Rating')
        plt.title('Ratings per Product Category')
        plt.xticks(rotation=45)
        plot_path_rating = os.path.join('static', 'plot_rating.png')
        plt.savefig(plot_path_rating)

        # Plotting for unit price
        plot_unit = df['Product line'].value_counts().reset_index()
        plot_unit.columns = ['Product line', 'Unit price']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=plot_unit, x='Product line', y='Unit price')
        plt.xlabel('Product Category')
        plt.ylabel('Unit price')
        plt.title('Unit Price per Product Category')
        plt.xticks(rotation=45)
        plot_path_unit = os.path.join('static', 'plot_unit.png')
        plt.savefig(plot_path_unit)

        # Plotting for gender
        plot_gender = df['Gender'].value_counts().reset_index()
        plot_gender.columns = ['Gender', 'total_products']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=plot_gender, x='Gender', y='total_products')
        plt.xlabel('Product Category')
        plt.ylabel('Unit price')
        plt.title('Unit Price per Product Category')
        plt.xticks(rotation=45)
        plot_path_gender = os.path.join('static', 'plot_gender.png')
        plt.savefig(plot_path_gender)

        # Plotting for customer type
        plot_type = df['Customer type'].value_counts().reset_index()
        plot_type.columns = ['Customer type', 'total_products']
        plt.figure(figsize=(10, 9))
        sns.barplot(data=plot_type, x='Customer type', y='total_products')
        plt.xlabel('Product Category')
        plt.ylabel('Unit price')
        plt.title('Unit Price per Product Category')
        plt.xticks(rotation=45)
        plot_path_type = os.path.join('static', 'plot_type.png')
        plt.savefig(plot_path_type)
        
        return render_template('index.html', plot_url=plot_path, plot_url_branch=plot_path_branch, plot_url_city=plot_path_city, plot_url_date=plot_path_date, plot_url_pm=plot_path_pm, plot_url_cogs=plot_path_cogs, plot_url_gross=plot_path_gross, plot_url_raring=plot_path_rating, plot_url_unit=plot_path_unit, plot_url_gender=plot_path_gender, plot_url_type=plot_path_type)

    return 'Invalid file format'



