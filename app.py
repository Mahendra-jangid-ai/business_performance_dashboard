from flask import Flask, render_template
import pandas as pd
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load dataset
DATA_PATH = 'data/Sales_Dataset.csv'
df = pd.read_csv(DATA_PATH)

def plot_monthly_sales():
    monthly_sales = df.groupby('Year-Month')['Amount'].sum()
    plt.figure(figsize=(10,4))
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title('Monthly Sales')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return img_base64

def plot_category_distribution():
    category_sales = df.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(6,6))
    category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140,
                        colors=['#FF9999','#66B2FF','#99FF99','#FFCC99'])
    plt.title('Sales by Category')
    plt.ylabel('')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return img_base64

@app.route('/')
def index():
    # Key metrics
    total_sales = df['Amount'].sum()
    total_profit = df['Profit'].sum()
    total_quantity = df['Quantity'].sum()
    top_category = df.groupby('Category')['Amount'].sum().idxmax()
    top_city = df.groupby('City')['Amount'].sum().idxmax()

    # Charts
    monthly_sales_chart = plot_monthly_sales()
    category_chart = plot_category_distribution()

    return render_template('index.html',
                           total_sales=total_sales,
                           total_profit=total_profit,
                           total_quantity=total_quantity,
                           top_category=top_category,
                           top_city=top_city,
                           monthly_sales_chart=monthly_sales_chart,
                           category_chart=category_chart)

if __name__ == '__main__':
    app.run(debug=True)
