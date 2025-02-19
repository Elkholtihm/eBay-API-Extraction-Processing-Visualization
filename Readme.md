# Processes ETL for Cryptocurencies market Analysis

## Overview
This project uses the eBay API to extract data about products (computers), processes it with Pandas and Scikit-learn, and visualizes it in a dashboard with Power BI.

---

## 📂 Repository Structure

### CODE/
```  
├── code/  
│   ├── executor.py              # execute functions presented in utils 
│   └──  utils.py                # contains function to authentificate, get data from eBay and store it in a csv file
├── images/ # contains Dashboard screenshot
├──  .env (you should create it)
├──  data.csv # data we extract
├──  output.csv # data after processing, dedicated to visualization
├──  requirements.txt # contains packages needed
├──  extract-process.ipynb # contains all the process from extracting, proccessing to storing.
├──  dashbord_web.pbix # Dashboard created on output.csv in power BI
└──  Getting eBay API Credentials.pdf # tutorial to get eBay API Credentials

```

---

## Used Technologies
The project leverages the following technologies:
- ![Sklearn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white&style=flat-square)
- ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white&style=flat-square)
- ![eBay](https://img.shields.io/badge/eBay-E53238?logo=ebay&logoColor=white&style=flat-square)
- ![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black&style=flat-square)
- ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=flat-square)

---

## Collaboration
This project was created in collaboration with **[Aya Salim](https://github.com/Salim-aya)**.

---
## 🚀 Using the Project
to use the project you need first to get the eBay API credentials and then create a .env file and include the folowing informations : 
as follow : 

```  
client_id = paste you're client id here 
client_secret = paste you're client secret here 

```
1. Clone the repository:
```bash
   git clone https://github.com/Elkholtihm/eBay-API-Extraction-Processing-Visualization.git
```

2. Install the required packages:
```bash
  pip install -r requirements.txt
```

3. Navigate to the code directory:
```bash
  cd code
```
4. Run executor.py 
```bash
  python executor.py
```
After the script will ask you about the product name (visite to see product name) and then the country code like US for united state, CA for Canada.
To process data you could use extract-process.ipynb or use you're approche. based on data you extract and the objectives of you're project.
## 📊 Dashboard
![Architecture](images/Dash.png)
## Get API credentials
To get API refer to Getting eBay API Credentials.pdf file