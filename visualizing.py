import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def import_data_adidas():
    adidas = pd.read_csv("C:/Users/Sara/project-2/dataframes/adidas_shoes.csv")
    column_order = ["Product name", "Product id", "Listing price", "Gender", "Category", "Rating", "Reviews"]
    adidas = adidas[column_order]
    return adidas

def import_data_nike():
    nike = pd.read_csv("C:/Users/Sara/project-2/dataframes/nike_shoes.csv")
    return nike

def import_data_mynike():
    mynike = pd.read_csv("C:/Users/Sara/project-2/dataframes/nike_mine.csv")
    return mynike

def products_per_brand():
    num_nike = len(nike)
    num_adidas = len(adidas)

    plt.figure(figsize=(10,5))
    sns.set_theme()
    y = [num_nike, num_adidas]
    colors = ['lightskyblue', 'lightgreen']
    brands = ['Nike', 'Adidas']

    plt.bar(brands, y, color=colors);

    plt.xlabel('Brands')
    plt.ylabel('Number of Products')
    plt.title('Number of Products by Brand')
    plt.show()

def category_manufactured_brand():
    sns.set_theme()
    plt.figure(figsize=(12,10))

    figure, axes = plt.subplots(1, 2, figsize=(12, 7))
    figure.suptitle('Which category is the most manufactured for each brand?')

    sns.countplot(data=adidas, y="Category", color="lightgreen", ax=axes[0])
    axes[0].set_title('Adidas')
    axes[0].set_ylabel('Category') 
    axes[0].tick_params(axis='y', rotation=0)  

    sns.countplot(data=nike, y="Category", color="lightskyblue", ax=axes[1])
    axes[1].set_title('Nike')
    axes[1].set_ylabel('') 
    axes[1].tick_params(axis='y', rotation=0)
    plt.show()

def product_manufactured_brand():
    sns.set_theme()
    plt.figure(figsize=(20,10))

    figure, axes = plt.subplots(2, 1, figsize=(12, 10))
    figure.suptitle('Which products are the ones most manufactured by each brand?')

    AdidasProducts = adidas['Product name'].value_counts().head()
    sns.barplot(x=AdidasProducts.index, y=AdidasProducts, palette="viridis", ax=axes[0], hue=AdidasProducts.index, dodge=False, legend=False);
    axes[0].set_title('Adidas')
    axes[0].tick_params(axis='x', rotation=45)
    axes[0].set_ylabel('Count') 

    NikeProducts = nike['Product name'].value_counts().head()
    sns.barplot(x=NikeProducts.index, y=NikeProducts, palette="viridis", ax=axes[1], hue=NikeProducts.index, dodge=False, legend=False);
    axes[1].set_title('Nike')
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].set_ylabel('Count')  
    plt.tight_layout()
    plt.show()   

def price_variation():
    sns.set_theme()
    plt.figure(figsize=(12,7))

    nikes = nike[nike["Listing price"] != 0]

    figure, axes = plt.subplots(1, 2, figsize=(12, 7))
    figure.suptitle('Price variation for each brand')

    sns.histplot(nike["Listing price"],bins=10,color= "deepskyblue",ax=axes[0], kde=True)
    axes[0].set_xlim(1, 7000)
    axes[0].set_title('Nike')

    sns.histplot(adidas["Listing price"],bins=10,color="green",ax=axes[1], kde=True)
    axes[1].set_title('Adidas')
    plt.show()

def nike_brand_article(name):
    if "Force" in name:
        return "Air Force"
    elif "Max" in name:
        return "Air Max"
    elif "Dunk" in name:
        return "Dunk"
    elif "Blazer" in name:
        return "Blazer"
    elif "Jordan" in name:
        return "Jordan"
    elif "Vomero" in name:
        return "Vomero"
    elif "LeBron" in name:
        return "LeBron"
    elif "KD" in name:
        return "Kevin Durant"
    elif "Giannis" in name:
        return "Giannis Antetokounmpo"
    elif "Sabrina" in name:
        return "Sabrina Ionescu"
    elif "JA" in name:
        return "Ja Morant"
    elif "Giannis" in name:
        return "Giannis Antetokounmpo"
    else:
        return "Jordan"
    

def nike_manufactured_articles(mynike):
    mynike["General Product name"] = mynike["Product name"].apply(get_nike_product_name)
    sns.set_theme()
    plt.figure(figsize=(12,7))

    sns.violinplot(data=mynike,x = "Category", y = "General Product name", hue="Gender",
                split=True, inner="quart", fill=False,
                palette={"Hombre": "blue", "Mujeres": "red"})
    
def adidas_brand_articles(name):
    if "NMD_" in name:
        return "NMD"
    elif "Gazelle" in name: 
        return "Gazelle"
    elif "Stan" in name:
        return "Stan Smith"
    elif "Superstar" in name:
        return "Superstar"
    elif "Inspired" in name or "INSPIRED" in name: 
        return "Inspired"
    elif "Swim" in name or "SWIM" in name or "Swimming" in name:
        return "Swim Slippers"
    elif "Sleek" in name:
        return "Sleeks"
    elif "Taekwondo" in name:
        return "Taekwondo"
    elif "Forest" in name:
        return "Forest"
    elif "Swif" in name or "SWIFT" in name:
        return "Swift"
    elif "Storm" in name: 
        return "Storm"
    elif "Nayo" in name or "NAYO" in name: 
        return "Nayo"
    elif "Nepton" in name: 
        return "Nepton"
    elif "Torik" in name: 
        return "Torik"
    elif "Nova" in name: 
        return "Nova"
    elif "Duramo" in name: 
        return "Duramo"
    elif "Cosmic" in name: 
        return "Cosmic"
    elif "EnergyFalcon" in name: 
        return "EnergyFalcon"
    elif "Aseerun" in name:
        return "Aseerun"
    elif "Hellion" in name: 
        return "Hellion"
    elif "Marathon" in name:
        return "Marathon"
    elif "U_Path" in name:
        return "U_Path"
    elif "Continental" in name:
        return "Continental"
    elif "YAMO" in name or "Yamo" in name:
        return "Yamo"
    elif "NEBULAR" in name or "Nebular" in name:
        return "Nebular"
    elif "LEGUS" in name or "Legus" in name:
        return "Legus"
    elif "HELKIN" in name or "Helkin" in name:
        return "Helkin"
    elif "Supercourt" in name:
        return "Supercourt"
    elif "Toe" in name:
        return "Toe"
    elif "Elevate" in name:
        return "Elevate"
    elif "CAMPUS" in name or "Campus" in name: 
        return "Campus"
    elif "Sambarose" in name:
        return "Sambarose"
    elif "Solar" in name:
        return "Solar"
    elif "SenseBoost" in name:
        return "SenseBoost"
    elif "Zx" in name:
        return "Zx 4000"
    elif "Alphaedge" in name:
        return "Alphaedge 4D"
    elif "Kontuur I" in name:
        return "Kontuur II"
    elif "Mutator" in name:
        return "Mutator 20+"
    elif "Nemeziz" in name:
        return "Nemeziz 19+/18+"
    elif "Copa" in name:
        return "Copa 19+"
    elif "Predator" in name:
        return "Predator 19+"
    elif "X" in name:
        return "X 18+"
    elif "Alexander" in name:
        return "Alexander Wang"
    elif "Pharrell" in name:
        return "Pharrell Williams"
    elif "Predator" in name:
        return "Predator 19+"
    elif "X" in name:
        return "X 18+"
    else:
        return "Other" 

def adidas_manufactured_articles(adidas):
    sns.set_theme()
    plt.figure(figsize=(25,17))

    sns.violinplot(data=adidas,x = "Category", y = "General Product name", hue="Gender",
                split=True, inner="quart", fill=False,
                palette={"Hombre": "blue", "Mujer": "red"})
    
def adidas_highest_price():
    sns.set_theme()
plt.figure(figsize=(12,7))
adidas_top_25 = adidas.sort_values(by="Listing price",ascending=False).head(25)
sns.barplot(x = "Listing price", y = "General Product name", data = adidas_top_25, color = "lightgreen")

def nike_highest_price():
    sns.set_theme()
    plt.figure(figsize=(12,7))
    nike_top_25 = mynike.sort_values(by = "Listing price", ascending = False).head(25)
    sns.barplot(x = "Listing price", y = "General Product name", data = nike_top_25, color = "lightskyblue")

