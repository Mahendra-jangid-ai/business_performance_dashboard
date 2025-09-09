# Business Performance Dashboard

A simple **Flask-based web dashboard** to analyze and visualize sales performance from a CSV dataset.  
The app calculates key metrics like total sales, profit, quantity, top category, and top city, and also displays charts for monthly sales and category-wise sales distribution.

---

##  Project Structure
BUSINESS PERFORMANCE DASHBOARD/
│── data/
│ └── Sales_Dataset.csv 
│
│── my_venv/ 
│
│── templates/
│ └── index.html 
│── app.py 
│── requirements.txt 
│── README.md 


---

##  Features
- Dashboard with responsive UI
- Displays key sales metrics
- Monthly sales bar chart
- Category-wise sales pie chart
- Uses Flask, Pandas, Matplotlib

---

## Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone [https://github.com/your-username/business-dashboard.git](https://github.com/Mahendra-jangid-ai/business_performance_dashboard)
   cd business-dashboard


2. **Create and activate virtual environment**
python -m venv my_venv
source my_venv/Scripts/activate   
source my_venv/bin/activate       


3. **Install dependencies**
pip install -r requirements.txt


4. **Run the Flask app**
python app.py
