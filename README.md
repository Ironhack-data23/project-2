<div style="text-align:center">
  <h1><strong>Nike vs Adidas</strong></h1>
  <h3><em>An In-Depth Exploration through Data Analysis and Web Scraping</em></h3>
  <h3><small>Cleaning, Exploring, Extracting, Transforming, and Visualizing data</small></h3>
  <h3><small>Project - 2</small></h3>
</div>

## Introduction
Two of the biggest names in sports, Nike and Adidas, have grown significantly over the past few decades as the industry has expanded. Even with the industry's diversification, both businesses are firmly established in similar markets that include sportswear, footwear, and equipment. Their rivalry has become greater because of their common interest.

### Dataset
For this research, two distincts datasets were employed: 

The first dataset, sourced from Kaggle,compared Adidas and Nike products.It includes information about products ID, products names, prices, discounts, ratings and reviews from both brands. 

The second dataset contains only and exclusively Nike products, generated through web scraping the official Nike webpage. It provides products ID, product names, prices and gender. It is important to mention that ratings and reviews are not included in this dataset, as it is nformation not available in the web-page. 

A combination of these datasets facilitates an in-depth analysis of pricing, discounts, and client feedback, hence augmenting a comprehensive comprehension of the competitive terrain among Adidas and Nike.

## Methodology 
Kaggle's dataset:
1. Cleaning dataset: staying with just Adidas brand, as Nike products were almost empty
2. Exploring data (EDA)
3. Data visualization 

Nike's dataset: 
1. Web scraping: define functions, and apply teh to each column 
2. Cleaning the resulting dataset
3. Merge with Nike's Kaggle part dataset by product ID. 
4. Data visualization 

## Pipeline
1. Data Collection:
Web Scraping: Identify the websites or platforms in which collect data.In this case Nike webpage. 
Specific data points to scrape: product name, product ID, price, shoe category, gender, colors. For this steps I used BeautifulSoup and requests libraries.
2. Data Cleaning:
    - Handle missing or inconsistent data.
    - Convert data types if necessary.
    - Remove duplicates and outliers.
3. Exploratory Data Analysis (EDA): 
4. Data visualization: Histograms, countplots, etc...

## Aims
The aim of this study is to study the footwear products that these brands sell. The study's objectives are to evaluate and compare a number of variables, such as costs, sales, categories, and other relevant elements. With this investigation, we hope to identify and assess Nike and Adidas' respective advantages in the fiercely competitive shoe industry.

## Analysis - Insights, patterns, relations found in the data, etc. 



## Results - Results of the analysis (visualizations, validation of hypothesis, etc.)


## Conclusion - Conclusions of the project





