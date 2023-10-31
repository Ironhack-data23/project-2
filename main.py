import pandas as pd 
import requests
from bs4 import BeautifulSoup
import re

pathway = "C:/Users/Sara/project-2/data_nike_vs_addidas_unsupervised.xlsx"
adidas_shoes = pd.read_excel(pathway)

def adidas_cleaining():
    adidas_shoes = adidas_shoes.head(2624)
    adidas_shoes = adidas_shoes.rename(columns={"Brand": "Category"})
    adidas_shoes.columns = adidas_shoes.columns.str.capitalize()

def adidas_drop():
    adidas_shoes.drop("Sale price", axis=1, inplace=True)
    adidas_shoes.drop("Discount", axis=1, inplace=True)

def get_adidas_gender(dataframe):
    men = re.compile(r"\b(?:Men|man)\b", flags=re.IGNORECASE)
    women = re.compile(r"\b(?:Women|woman)\b", flags=re.IGNORECASE)
    
    if men.search(dataframe):
        return "Hombre"
    elif  women.search(dataframe):
        return "Mujer"
    else:
        return "Hombre"
    
def get_adidas_cat(category):
    if category == "Adidas SPORT PERFORMANCE":
        return "Sports"
    elif category == "Adidas CORE / NEO":
        return "Sports"
    else:
        return "Lifestyle"
    
def apply_gender():
    adidas_shoes["Gender"] = adidas_shoes["Product name"].apply(get_adidas_gender)
    
def adidas_rename_product():
    men = re.compile(r"\b(?:Men|man)'?s\b", flags=re.IGNORECASE)
    women = re.compile(r"\b(?:Women|woman)'?s\b", flags=re.IGNORECASE)
    unisex = re.compile(r"\b(?:Unisex|unisex)'?s\b", flags=re.IGNORECASE)
    shoes = re.compile(r"\b(?:Shoes|shoes)\b", flags=re.IGNORECASE)
    adidas = re.compile(r"\b(?:Adidas|adidas)\b", flags=re.IGNORECASE)

def changing_column():
    adidas_shoes["Product name"] = adidas_shoes["Product name"].str.title()
    adidas_shoes["Category"] = adidas_shoes["Category"].str.title()
    column_order = ["Product name", "Product id", "Listing price", "Gender", "Category", "Rating", "Reviews"]
    adidas_shoes = adidas_shoes[column_order]
    return adidas_shoes

def drop_duplicates():
    adidas_shoes = adidas_shoes.drop_duplicates(subset=["Product id", "Product name","Gender"])
    return adidas_shoes

def basic_info(url):
    url = "https://www.nike.com/es/w/air-max-lifestyle-zapatillas-13jrmza6d8hzy7ok"
    res = requests.get(url)                                       
    soup = BeautifulSoup(res.content, 'html.parser')
    nikew = soup.find_all("div", {"class": "product-grid__items css-hvew4t"})
    return nikew


def get_name(url):
    res = requests.get(url)
    res.raise_for_status() 
    soup = BeautifulSoup(res.content, 'html.parser')
    nikew = soup.find_all("div", {"class": "product-card__title"})
    name = [name.get("id").replace(" \xa0 ", "") for name in nikew]
    return name

def get_nike_ids(url):
    try:
        res = requests.get(url)
        res.raise_for_status() 
        soup = BeautifulSoup(res.content, 'html.parser')
        nikew = soup.find_all("div", {"class": "product-grid__items css-hvew4t"})
        ids = [id.get('href') for i in nikew for id in i.select('.product-card__link-overlay')]
        ids = [url.split("/")[-1] for url in ids]
        return ids
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None 
    
def get_prices(soup):
    res = requests.get(url)
    res.raise_for_status() 
    soup = BeautifulSoup(res.content, 'html.parser')
    prices = soup.find_all("div", {"role":"link","class":"product-price es__styling is--current-price css-11s12ax"})
    return [i.text.strip().replace("\xa0", "").replace("€","") for i in prices]

def get_gender(soup):
    res = requests.get(url)
    res.raise_for_status() 
    soup = BeautifulSoup(res.content, 'html.parser')
    gender = soup.find_all("div", {"class": "product-card__titles"})
    return [i.text.strip().split()[-1].replace("1Zapatillas", "Unisex").replace("infantil", "Unisex").replace("pequeño/a","Unisex").replace("EasyOnZapatillas", "Mujeres") for i in gender]

def available_count_colors(soup):
    res = requests.get(url)
    res.raise_for_status() 
    soup = BeautifulSoup(res.content, 'html.parser')
    available_colors = soup.find_all("div", {"class": "product-card__count-item"})
    available_colors = [i.text.strip().replace(" colores", "").replace(" color", "") for i in available_colors]
    return available_colors

def get_brand(soup):
    res = requests.get(url)
    res.raise_for_status() 
    soup = BeautifulSoup(res.content, 'html.parser')
    brand = soup.select("div.brand")
    return brand

def AirForce1():
    AirForce1m = "https://www.nike.com/es/w/hombre-air-force-1-lifestyle-zapatillas-13jrmz5sj3yznik1zy7ok"
    name_airforcem = get_name(AirForce1m)
    id_airforcem = get_nike_ids(AirForce1m)
    price_airforcem = get_prices(AirForce1m)
    gender_airforcem = get_gender(AirForce1m)
    colors_airforcem = available_count_colors(AirForce1m)
    AirForce1w = "https://www.nike.com/es/w/mujer-air-force-1-lifestyle-zapatillas-13jrmz5e1x6z5sj3yzy7ok"
    name_airforcew = get_name(AirForce1w)
    id_airforcew = get_nike_ids(AirForce1w)
    price_airforcew = get_prices(AirForce1w)
    gender_airforcew = get_gender(AirForce1w)
    colors_airforcew = available_count_colors(AirForce1w)
    AirForce1u = "https://www.nike.com/es/w/unisex-air-force-1-lifestyle-zapatillas-13jrmz3rauvz5sj3yzy7ok"
    name_airforceu = get_name(AirForce1u)
    id_airforceu = get_nike_ids(AirForce1u)
    price_airforceu= get_prices(AirForce1u)
    gender_airforceu = get_gender(AirForce1u)
    colors_airforceu = available_count_colors(AirForce1u)
    dict_AirForce1 = {
    "name":name_airforcem + name_airforcew + name_airforceu,
    "id": id_airforcew + id_airforcem + id_airforceu,
    "price": price_airforcew + price_airforcem + price_airforceu,
    "gender": gender_airforcew  + gender_airforcem + gender_airforceu,
    "colors": colors_airforcew + colors_airforcem + colors_airforceu
    }

    max_length = max(len(value) for value in dict_AirForce1.values())
    for key, value in dict_AirForce1.items():
        dict_AirForce1[key] = value + [0] * (max_length - len(value))
    AirForce1 = pd.DataFrame(dict_AirForce1) 

    pd.set_option('display.max_rows', None)
    d = id_airforcew + id_airforcem + id_airforceu
    print(len(d))
    AirForce1 = AirForce1.head(52)
    return AirForce1

def AirMax1(): 
    AirMax1m = "https://www.nike.com/es/w/hombre-air-max-1-lifestyle-zapatillas-13jrmz8p4egznik1zy7ok"
    name_airmax1m = get_name(AirMax1m)
    id_airmax1m = get_nike_ids(AirMax1m)
    price_airmax1m = get_prices(AirMax1m)
    gender_airmax1m = get_gender(AirMax1m)
    colors_airmax1m = available_count_colors(AirMax1m)
    AirMax1w = "https://www.nike.com/es/w/mujer-air-max-1-lifestyle-zapatillas-13jrmz5e1x6z8p4egzy7ok"
    name_airmax1w = get_name(AirMax1w)
    id_airmax1w = get_nike_ids(AirMax1w)
    price_airmax1w = get_prices(AirMax1w)
    gender_airmax1w = get_gender(AirMax1w)
    colors_airmax1w = available_count_colors(AirMax1w)
    AirMax1u = "https://www.nike.com/es/w/unisex-air-max-1-lifestyle-zapatillas-13jrmz3rauvz8p4egzy7ok"
    name_airmax1u = get_name(AirMax1u)
    id_airmax1u = get_nike_ids(AirMax1u)
    price_airmax1u = get_prices(AirMax1u)
    gender_airmax1u = get_gender(AirMax1u)
    colors_airmax1u = available_count_colors(AirMax1u)
    dict_Airmax1 = {
        "name": name_airmax1m + name_airmax1w + name_airmax1u,
        "id": id_airmax1m + id_airmax1w + id_airmax1u,
        "price": price_airmax1m + price_airmax1w + price_airmax1u,
        "gender": gender_airmax1m  + gender_airmax1w + gender_airmax1u,
        "colors": colors_airmax1m + colors_airmax1w + colors_airmax1u
    }

    max_length = max(len(value) for value in dict_Airmax1.values())
    for key, value in dict_Airmax1.items():
        dict_Airmax1[key] = value + [0] * (max_length - len(value))
    Airmax1 = pd.DataFrame(dict_Airmax1) 

    d = id_airmax1m + id_airmax1w + id_airmax1u
    print(len(d))
    Airmax1 = Airmax1.head(29)
    return Airmax1

def AirMax90(): 
    AirMax90m = "https://www.nike.com/es/w/hombre-air-max-90-lifestyle-zapatillas-13jrmzauqmoznik1zy7ok"
    name_airmax90m = get_name(AirMax90m)
    id_airmax90m = get_nike_ids(AirMax90m)
    price_airmax90m = get_prices(AirMax90m)
    gender_airmax90m = get_gender(AirMax90m)
    colors_airmax90m = available_count_colors(AirMax90m)
    AirMax90w = "https://www.nike.com/es/w/mujer-air-max-90-lifestyle-zapatillas-13jrmz5e1x6zauqmozy7ok"
    name_airmax90w = get_name(AirMax90w)
    id_airmax90w = get_nike_ids(AirMax90w)
    price_airmax90w = get_prices(AirMax90w)
    gender_airmax90w = get_gender(AirMax90w)
    colors_airmax90w = available_count_colors(AirMax90w)
    AirMax90u = "https://www.nike.com/es/w/unisex-air-max-90-lifestyle-zapatillas-13jrmz3rauvzauqmozy7ok"
    name_airmax90u = get_name(AirMax90u)
    id_airmax90u = get_nike_ids(AirMax90u)
    price_airmax90u = get_prices(AirMax90u)
    gender_airmax90u = get_gender(AirMax90u)
    colors_airmax90u = available_count_colors(AirMax90u)
    dict_Airmax90 = {
        "name": name_airmax90m + name_airmax90w + name_airmax90u,
        "id": id_airmax90m + id_airmax90w + id_airmax90u,
        "price": price_airmax90m + price_airmax90w + price_airmax90u,
        "gender": gender_airmax90m  + gender_airmax90w + gender_airmax90u,
        "colors": colors_airmax90m + colors_airmax90w + colors_airmax90u
    }

    max_length = max(len(value) for value in dict_Airmax90.values())
    for key, value in dict_Airmax90.items():
        dict_Airmax90[key] = value + [0] * (max_length - len(value))
    Airmax90 = pd.DataFrame(dict_Airmax90) 

    d = id_airmax90m + id_airmax90w + id_airmax90u
    print(len(d))
    Airmax90 = Airmax90.head(41)
    return Airmax90

def AirMax95():
    AirMax95m = "https://www.nike.com/es/w/hombre-air-max-95-lifestyle-zapatillas-13jrmzb0mibznik1zy7ok"
    name_airmax95m = get_name(AirMax95m)
    id_airmax95m = get_nike_ids(AirMax95m)
    price_airmax95m = get_prices(AirMax95m)
    gender_airmax95m = get_gender(AirMax95m)
    colors_airmax95m = available_count_colors(AirMax95m)
    AirMax95w = "https://www.nike.com/es/w/mujer-air-max-95-lifestyle-zapatillas-13jrmz5e1x6zb0mibzy7ok"
    name_airmax95w = get_name(AirMax95w)
    id_airmax95w = get_nike_ids(AirMax95w)
    price_airmax95w = get_prices(AirMax95w)
    gender_airmax95w = get_gender(AirMax95w)
    colors_airmax95w = available_count_colors(AirMax95w)
    dict_Airmax95 = {
        "name": name_airmax95m + name_airmax95w,
        "id": id_airmax95m + id_airmax95w,
        "price": price_airmax95m + price_airmax95w,
        "gender": gender_airmax95m  + gender_airmax95w ,
        "colors": colors_airmax95m + colors_airmax95w
    }

    max_length = max(len(value) for value in dict_Airmax95.values())
    for key, value in dict_Airmax95.items():
        dict_Airmax95[key] = value + [0] * (max_length - len(value))
    Airmax95 = pd.DataFrame(dict_Airmax95) 


    d =  id_airmax95m + id_airmax95w
    print(len(d))
    Airmax95 = Airmax95.head(23)
    return Airmax95

def AirMax97():
    AirMax97m = "https://www.nike.com/es/w/hombre-air-max-97-lifestyle-zapatillas-13jrmz77f38znik1zy7ok"
    name_airmax97m = get_name(AirMax97m)
    id_airmax97m = get_nike_ids(AirMax97m)
    price_airmax97m = get_prices(AirMax97m)
    gender_airmax97m = get_gender(AirMax97m)
    colors_airmax97m = available_count_colors(AirMax97m)
    AirMax97w = "https://www.nike.com/es/w/mujer-air-max-97-lifestyle-zapatillas-13jrmz5e1x6z77f38zy7ok"
    name_airmax97w = get_name(AirMax97w)
    id_airmax97w = get_nike_ids(AirMax97w)
    price_airmax97w = get_prices(AirMax97w)
    gender_airmax97w = get_gender(AirMax97w)
    colors_airmax97w = available_count_colors(AirMax97w)
    dict_Airmax97 = {
        "name": name_airmax97m + name_airmax97w,
        "id": id_airmax97m + id_airmax97w,
        "price": price_airmax97m + price_airmax97w,
        "gender": gender_airmax97m  + gender_airmax97w ,
        "colors": colors_airmax97m + colors_airmax97w
    }

    max_length = max(len(value) for value in dict_Airmax97.values())
    for key, value in dict_Airmax97.items():
        dict_Airmax97[key] = value + [0] * (max_length - len(value))
    Airmax97 = pd.DataFrame(dict_Airmax97) 


    d =  id_airmax97m + id_airmax97w
    print(len(d))
    Airmax97 = Airmax97.head(24)
    return Airmax97

def AirMax270(): 
    AirMax270m = "https://www.nike.com/es/w/hombre-air-max-270-lifestyle-zapatillas-13jrmz5ix6dznik1zy7ok"  
    name_airmax270m = get_name(AirMax270m)
    id_airmax270m = get_nike_ids(AirMax270m)
    price_airmax270m = get_prices(AirMax270m)
    gender_airmax270m = get_gender(AirMax270m)
    colors_airmax270m = available_count_colors(AirMax270m)
    AirMax270w = "https://www.nike.com/es/w/mujer-air-max-270-lifestyle-zapatillas-13jrmz5e1x6z5ix6dzy7ok"  
    name_airmax270w = get_name(AirMax270w)
    id_airmax270w = get_nike_ids(AirMax270w)
    price_airmax270w = get_prices(AirMax270w)
    gender_airmax270w = get_gender(AirMax270w)
    colors_airmax270w = available_count_colors(AirMax270w)
    dict_Airmax270 = {
        "name": name_airmax270m + name_airmax270w,
        "id": id_airmax270m + id_airmax270w,
        "price": price_airmax270m + price_airmax270w,
        "gender": gender_airmax270m  + gender_airmax270w ,
        "colors": colors_airmax270m + colors_airmax270w
    }

    max_length = max(len(value) for value in dict_Airmax270.values())
    for key, value in dict_Airmax270.items():
        dict_Airmax270[key] = value + [0] * (max_length - len(value))
    Airmax270 = pd.DataFrame(dict_Airmax270) 

    d = id_airmax270m + id_airmax270w
    print(len(d))
    Airmax270 = Airmax270.head(11)
    return Airmax270

def AirMaxF():
    AirMaxFw = "https://www.nike.com/es/w/mujer-air-max-furyosa-lifestyle-zapatillas-13jrmz5e1x6z5lnxgzy7ok"
    name_airmaxFw = get_name(AirMaxFw)
    id_airmaxFw = get_nike_ids(AirMaxFw)
    price_airmaxFw = get_prices(AirMaxFw)
    gender_airmaxFw = get_gender(AirMaxFw)
    colors_airmaxFw = available_count_colors(AirMaxFw)
    dict_AirmaxF = {
        "name": name_airmaxFw,
        "id": id_airmaxFw,
        "price":  price_airmaxFw,
        "gender": gender_airmaxFw,
        "colors": colors_airmaxFw
    }

    max_length = max(len(value) for value in dict_AirmaxF.values())
    for key, value in dict_AirmaxF.items():
        dict_AirmaxF[key] = value + [0] * (max_length - len(value))
    AirmaxF = pd.DataFrame(dict_AirmaxF) 


    d = id_airmaxFw
    print(len(d))
    AirmaxF = AirmaxF.head(3)
    return AirmaxF

def AirMaxP():
    AirMaxPm = "https://www.nike.com/es/w/hombre-air-max-pulse-lifestyle-zapatillas-13jrmz1lkruznik1zy7ok"
    name_airmaxPm= get_name(AirMaxPm)
    id_airmaxPm = get_nike_ids(AirMaxPm)
    price_airmaxPm = get_prices(AirMaxPm)
    gender_airmaxPm = get_gender(AirMaxPm)
    colors_airmaxPm = available_count_colors(AirMaxPm)
    AirMaxPw = "https://www.nike.com/es/w/mujer-air-max-pulse-lifestyle-zapatillas-13jrmz1lkruz5e1x6zy7ok"
    name_airmaxPw= get_name(AirMaxPw)
    id_airmaxPw = get_nike_ids(AirMaxPw)
    price_airmaxPw = get_prices(AirMaxPw)
    gender_airmaxPw = get_gender(AirMaxPw)
    colors_airmaxPw = available_count_colors(AirMaxPw)
    dict_AirmaxP = {
        "name": name_airmaxPm + name_airmaxPw, 
        "id": id_airmaxPm + id_airmaxPw,
        "price": price_airmaxPm + price_airmaxPw,
        "gender": gender_airmaxPm  + gender_airmaxPw ,
        "colors": colors_airmaxPm + colors_airmaxPw
    }

    max_length = max(len(value) for value in dict_AirmaxP.values())
    for key, value in dict_AirmaxP.items():
        dict_AirmaxP[key] = value + [0] * (max_length - len(value))
    AirmaxP = pd.DataFrame(dict_AirmaxP) 

    d = id_airmaxPm + id_airmaxPw
    print(len(d))
    AirmaxP = AirmaxP.head(9)
    return AirmaxP

def AirMax2021(): 
    AirMax2021w = "https://www.nike.com/es/w/mujer-air-max-pulse-lifestyle-zapatillas-13jrmz1lkruz5e1x6zy7ok"
    name_airmax2021w= get_name(AirMax2021w)
    id_airmax2021w = get_nike_ids(AirMax2021w)
    price_airmax2021w = get_prices(AirMax2021w)
    gender_airmax2021w = get_gender(AirMax2021w)
    colors_airmax2021w = available_count_colors(AirMax2021w)
    dict_Airmax2021 = {
        "name": name_airmax2021w, 
        "id": id_airmax2021w,
        "price":  price_airmax2021w,
        "gender": gender_airmax2021w,
        "colors": colors_airmax2021w
    }

    max_length = max(len(value) for value in dict_Airmax2021.values())
    for key, value in dict_Airmax2021.items():
        dict_Airmax2021[key] = value + [0] * (max_length - len(value))
    Airmax2021 = pd.DataFrame(dict_Airmax2021) 

    d = id_airmax2021w
    print(len(d))
    Airmax2021 = Airmax2021.head(3)
    return Airmax2021

def AirMaxPlus(): 
    AirMaxPlusm = "https://www.nike.com/es/w/hombre-air-max-plus-lifestyle-zapatillas-13jrmzahvdnznik1zy7ok"
    name_airmaxplusm= get_name(AirMaxPlusm)
    id_airmaxplusm = get_nike_ids(AirMaxPlusm)
    price_airmaxplusm = get_prices(AirMaxPlusm)
    gender_airmaxplusm = get_gender(AirMaxPlusm)
    colors_airmaxplusm = available_count_colors(AirMaxPlusm)
    AirMaxPlusw = "https://www.nike.com/es/w/mujer-air-max-plus-lifestyle-zapatillas-13jrmz5e1x6zahvdnzy7ok"
    name_airmaxplusw= get_name(AirMaxPlusw)
    id_airmaxplusw = get_nike_ids(AirMaxPlusw)
    price_airmaxplusw = get_prices(AirMaxPlusw)
    gender_airmaxplusw = get_gender(AirMaxPlusw)
    colors_airmaxplusw = available_count_colors(AirMaxPlusw)
    dict_AirmaxPlus = {
        "name": name_airmaxplusm + name_airmaxplusw,
        "id": id_airmaxplusm + id_airmaxplusw,
        "price": price_airmaxplusm + price_airmaxplusw,
        "gender": gender_airmaxplusm  + gender_airmaxplusw,
        "colors": colors_airmaxplusm + colors_airmaxplusw
    }

    max_length = max(len(value) for value in dict_AirmaxPlus.values())
    for key, value in dict_AirmaxPlus.items():
        dict_AirmaxPlus[key] = value + [0] * (max_length - len(value))
    AirmaxPlus = pd.DataFrame(dict_AirmaxPlus) 

    d =  id_airmaxplusm + id_airmaxplusw
    print(len(d))
    AirmaxPlus = AirmaxPlus.head(38)
    return AirmaxPlus

def AirMaxTW():
    AirMaxTWm = "https://www.nike.com/es/w/hombre-air-max-tw-lifestyle-zapatillas-13jrmz9k3inznik1zy7ok"
    name_airmaxTWm = get_name(AirMaxTWm)
    id_airmaxTWm = get_nike_ids(AirMaxTWm)
    price_airmaxTWm = get_prices(AirMaxTWm)
    gender_airmaxTWm = get_gender(AirMaxTWm)
    colors_airmaxTWm = available_count_colors(AirMaxTWm)
    dict_AirmaxTW = {
        "name": name_airmaxTWm, 
        "id": id_airmaxTWm,
        "price":  price_airmaxTWm,
        "gender": gender_airmaxTWm,
        "colors": colors_airmaxTWm
    }

    max_length = max(len(value) for value in dict_AirmaxTW.values())
    for key, value in dict_AirmaxTW.items():
        dict_AirmaxTW[key] = value + [0] * (max_length - len(value))
    AirmaxTW = pd.DataFrame(dict_AirmaxTW) 

    d =  id_airmaxTWm
    print(len(d))
    AirmaxTW = AirmaxTW.head(7)
    return AirmaxTW

def VaporMax(): 
    VaporMAXm = "https://www.nike.com/es/w/hombre-vapormax-lifestyle-zapatillas-13jrmz220dznik1zy7ok"
    name_vapormaxm = get_name(VaporMAXm)
    id_vapormaxm = get_nike_ids(VaporMAXm)
    price_vapormaxm = get_prices(VaporMAXm)
    gender_vapormaxm = get_gender(VaporMAXm)
    colors_vapormaxm = available_count_colors(VaporMAXm)
    VaporMAXw = "https://www.nike.com/es/w/mujer-vapormax-lifestyle-zapatillas-13jrmz220dz5e1x6zy7ok"
    name_vapormaxw = get_name(VaporMAXw)
    id_vapormaxw = get_nike_ids(VaporMAXw)
    price_vapormaxw = get_prices(VaporMAXw)
    gender_vapormaxw = get_gender(VaporMAXw)
    colors_vapormaxw = available_count_colors(VaporMAXw)
    dict_VaporMAX= {
        "name": name_vapormaxm + name_vapormaxw,
        "id": id_vapormaxm + id_vapormaxw,
        "price": price_vapormaxm + price_vapormaxw,
        "gender": gender_vapormaxm  + gender_vapormaxw,
        "colors": colors_vapormaxm + colors_vapormaxw
    }

    max_length = max(len(value) for value in dict_VaporMAX.values())
    for key, value in dict_VaporMAX.items():
        dict_VaporMAX[key] = value + [0] * (max_length - len(value))
    VaporMAX = pd.DataFrame(dict_VaporMAX) 

    d = id_vapormaxm + id_vapormaxw
    print(len(d))
    VaporMAX = VaporMAX.head(11)
    return VaporMAX

def Dunk():
    Dunksm = "https://www.nike.com/es/w/hombre-dunk-lifestyle-zapatillas-13jrmz90aohznik1zy7ok"
    name_dunkm = get_name(Dunksm)
    id_dunkm = get_nike_ids(Dunksm)
    price_dunkm = get_prices(Dunksm)
    gender_dunkm = get_gender(Dunksm)
    colors_dunkm = available_count_colors(Dunksm)
    Dunksw = "https://www.nike.com/es/w/mujer-dunk-lifestyle-zapatillas-13jrmz5e1x6z90aohzy7ok"
    name_dunkw = get_name(Dunksw)
    id_dunkw = get_nike_ids(Dunksw)
    price_dunkw = get_prices(Dunksw)
    gender_dunkw = get_gender(Dunksw)
    colors_dunkw = available_count_colors(Dunksw)
    Dunksu = "https://www.nike.com/es/w/unisex-dunk-lifestyle-zapatillas-13jrmz3rauvz90aohzy7ok"
    name_dunku = get_name(Dunksu)
    id_dunku = get_nike_ids(Dunksu)
    price_dunku = get_prices(Dunksu)
    gender_dunku = get_gender(Dunksu)
    colors_dunku = available_count_colors(Dunksu)
    dict_Dunk = {
        "name": name_dunkm + name_dunkw + name_dunku,
        "id": id_dunkm + id_dunkw + id_dunku,
        "price": price_dunkm + price_dunkw + price_dunku,
        "gender": gender_dunkm  + gender_dunkw + gender_dunku,
        "colors": colors_dunkm + colors_dunkw + colors_dunku
    }

    max_length = max(len(value) for value in dict_Dunk.values())
    for key, value in dict_Dunk.items():
        dict_Dunk[key] = value + [0] * (max_length - len(value))
    Dunk = pd.DataFrame(dict_Dunk) 

    d = id_dunkm + id_dunkw + id_dunku
    print(len(d))
    Dunk = Dunk.head(48)
    return Dunk

def Blazer():
    Blazersm = "https://www.nike.com/es/w/hombre-blazer-lifestyle-zapatillas-13jrmz9gw3aznik1zy7ok"
    name_blazerm = get_name(Blazersm)
    id_blazerm = get_nike_ids(Blazersm)
    price_blazerm = get_prices(Blazersm)
    gender_blazerm = get_gender(Blazersm)
    colors_blazerm = available_count_colors(Blazersm)
    Blazersw = "https://www.nike.com/es/w/mujer-blazer-lifestyle-zapatillas-13jrmz5e1x6z9gw3azy7ok"
    name_blazerw = get_name(Blazersw)
    id_blazerw = get_nike_ids(Blazersw)
    price_blazerw = get_prices(Blazersw)
    gender_blazerw = get_gender(Blazersw)
    colors_blazerw = available_count_colors(Blazersw)
    Blazersu = "https://www.nike.com/es/w/unisex-blazer-lifestyle-zapatillas-13jrmz3rauvz9gw3azy7ok"
    name_blazeru = get_name(Blazersu)
    id_blazeru = get_nike_ids(Blazersu)
    price_blazeru = get_prices(Blazersu)
    gender_blazeru = get_gender(Blazersu)
    colors_blazeru = available_count_colors(Blazersu)
    dict_Blazer = {
        "name": name_blazerm + name_blazerw + name_blazeru,
        "id": id_blazerm + id_blazerw + id_blazeru,
        "price": price_blazerm + price_blazerw + price_blazeru,
        "gender": gender_blazerm  + gender_blazerw + gender_blazeru,
        "colors": colors_blazerm + colors_blazerw + colors_blazeru
    }

    max_length = max(len(value) for value in dict_Blazer.values())
    for key, value in dict_Blazer.items():
        dict_Blazer[key] = value + [0] * (max_length - len(value))
    Blazer = pd.DataFrame(dict_Blazer) 

    d = id_blazerm + id_blazerw + id_blazeru
    print(len(d))
    Blazer = Blazer.head(30)
    return Blazer

def JordansMid():
    JordanMidm = "https://www.nike.com/es/w/hombre-jordan-lifestyle-perfil-medio-zapatillas-13jrmz1pi6yz37eefznik1zy7ok"
    name_jmidm = get_name(JordanMidm)
    id_jmidm = get_nike_ids(JordanMidm)
    price_jmidm = get_prices(JordanMidm)
    gender_jmidm = get_gender(JordanMidm)
    colors_jmidm= available_count_colors(JordanMidm)
    JordanMidw = "https://www.nike.com/es/w/mujer-jordan-lifestyle-perfil-medio-zapatillas-13jrmz1pi6yz37eefz5e1x6zy7ok"
    name_jmidw = get_name(JordanMidw)
    id_jmidw = get_nike_ids(JordanMidw)
    price_jmidw = get_prices(JordanMidw)
    gender_jmidw = get_gender(JordanMidw)
    colors_jmidw = available_count_colors(JordanMidw)
    dict_Jordansmid= {
        "name": name_jmidm + name_jmidw, 
        "id": id_jmidm + id_jmidw,
        "price": price_jmidm + price_jmidw,
        "gender": gender_jmidm  + gender_jmidw,
        "colors": colors_jmidm + colors_jmidw
    }

    max_length = max(len(value) for value in dict_Jordansmid.values())
    for key, value in dict_Jordansmid.items():
        dict_Jordansmid[key] = value + [0] * (max_length - len(value))
    Jordansmid = pd.DataFrame(dict_Jordansmid) 

    d = id_jmidm + id_jmidw
    print(len(d))
    Jordansmid = Jordansmid.head(48)
    return Jordansmid

def JordansHigh():
    JordanHighm = "https://www.nike.com/es/w/hombre-jordan-lifestyle-perfil-alto-zapatillas-13jrmz37eefz6lqy0znik1zy7ok"
    name_jhighm= get_name(JordanHighm)
    id_jhighm = get_nike_ids(JordanHighm)
    price_jhighm = get_prices(JordanHighm)
    gender_jhighm = get_gender(JordanHighm)
    colors_jhighm = available_count_colors(JordanHighm)
    JordanHighw = "https://www.nike.com/es/w/mujer-jordan-lifestyle-perfil-alto-zapatillas-13jrmz37eefz5e1x6z6lqy0zy7ok"
    name_jhighw= get_name(JordanHighw)
    id_jhighw = get_nike_ids(JordanHighw)
    price_jhighw = get_prices(JordanHighw)
    gender_jhighw = get_gender(JordanHighw)
    colors_jhighw = available_count_colors(JordanHighw)
    dict_Jordanshigh= {
        "name": name_jhighm + name_jhighw,
        "id": id_jhighm + id_jhighw,
        "price": price_jhighm + price_jhighw,
        "gender": gender_jhighm  + gender_jhighw,
        "colors": colors_jhighm + colors_jhighw
    }

    max_length = max(len(value) for value in dict_Jordanshigh.values())
    for key, value in dict_Jordanshigh.items():
        dict_Jordanshigh[key] = value + [0] * (max_length - len(value))
    Jordanshigh = pd.DataFrame(dict_Jordanshigh) 

    d = id_jhighm + id_jhighw
    print(len(d))
    Jordanshigh = Jordanshigh.head(26)
    return Jordanshigh

def Voomero(): 
    Voomm =  "https://www.nike.com/es/w/hombre-zoom-vomero-lifestyle-zapatillas-13jrmz7gee1znik1zy7ok"
    name_voomm= get_name(Voomm)
    id_voomm = get_nike_ids(Voomm)
    price_voomm = get_prices(Voomm)
    gender_voomm = get_gender(Voomm)
    colors_voomm = available_count_colors(Voomm)
    Voomw =  "https://www.nike.com/es/w/mujer-zoom-vomero-lifestyle-zapatillas-13jrmz5e1x6z7gee1zy7ok"
    name_voomw= get_name(Voomw)
    id_voomw = get_nike_ids(Voomw)
    price_voomw = get_prices(Voomw)
    gender_voomw = get_gender(Voomw)
    colors_voomw = available_count_colors(Voomw)
    Voomu =  "https://www.nike.com/es/w/unisex-zoom-vomero-lifestyle-zapatillas-13jrmz3rauvz7gee1zy7ok"
    name_voomu = get_name(Voomw)
    id_voomu = get_nike_ids(Voomu)
    price_voomu = get_prices(Voomu)
    gender_voomu = get_gender(Voomu)
    colors_voomu = available_count_colors(Voomu)
    dict_Voom = {
        "name": name_voomm + name_voomw + name_voomu,
        "id": id_voomm + id_voomw + id_voomu,
        "price": price_voomm + price_voomw + price_voomu,
        "gender": gender_voomm  + gender_voomw + gender_voomu,
        "colors": colors_voomm + colors_voomw + colors_voomu
    }

    max_length = max(len(value) for value in dict_Voom.values())
    for key, value in dict_Voom.items():
        dict_Voom[key] = value + [0] * (max_length - len(value))
    Voom = pd.DataFrame(dict_Voom) 


    d = id_voomm + id_voomw + id_voomu
    print(len(d))
    Voom = Voom.head(7)
    return Voom 

def LebronJames():
    LeBronJames = "https://www.nike.com/es/w/lebron-baloncesto-zapatillas-3glsmz3rauvz5e1x6z7y57xznik1zy7ok"
    name_lbj= get_name(LeBronJames)
    id_lbj = get_nike_ids(LeBronJames)
    price_lbj = get_prices(LeBronJames)
    gender_lbj = get_gender(LeBronJames)
    colors_lbj = available_count_colors(LeBronJames)

    dict_LeBron = {
    "name": name_lbj, 
    "id": id_lbj,
    "price": price_lbj,
    "gender": gender_lbj,
    "colors": colors_lbj
    }

    max_length = max(len(value) for value in dict_LeBron.values())
    for key, value in dict_LeBron.items():
        dict_LeBron[key] = value + [0] * (max_length - len(value))
    LeBron = pd.DataFrame(dict_LeBron) 

    d = id_lbj
    print(len(d))
    LeBron = LeBron.head(7)
    return LeBron 

def KevinDurant():
    KD = "https://www.nike.com/es/w/kevin-durant-baloncesto-zapatillas-3glsmz3hmd1z3rauvz5e1x6znik1zy7ok" 
    name_kd= get_name(KD)
    id_kd = get_nike_ids(KD)
    price_kd = get_prices(KD)
    gender_kd = get_gender(KD)
    colors_kd = available_count_colors(KD)

    dict_KD = {
        "name": name_kd,
        "id": id_kd,
        "price": price_kd,
        "gender": gender_kd,
        "colors": colors_kd
    }

    max_length = max(len(value) for value in dict_KD.values())
    for key, value in dict_KD.items():
        dict_KD[key] = value + [0] * (max_length - len(value))
    KD = pd.DataFrame(dict_KD) 

    d = id_kd
    print(len(d))
    KD = KD.head(4)
    return KD

def Giannis():
    GiannisA = "https://www.nike.com/es/w/giannis-antetokounmpo-baloncesto-zapatillas-2wfnqz3glsmz3rauvz5e1x6znik1zy7ok"
    name_ga = get_name(GiannisA)
    id_ga = get_nike_ids(GiannisA)
    price_ga = get_prices(GiannisA)
    gender_ga = get_gender(GiannisA)
    colors_ga = available_count_colors(GiannisA)

    dict_GA = {
        "name": name_ga,
        "id": id_ga,
        "price": price_ga,
        "gender": gender_ga,
        "colors": colors_ga
    }

    max_length = max(len(value) for value in dict_GA.values())
    for key, value in dict_GA.items():
        dict_GA[key] = value + [0] * (max_length - len(value))
    GA = pd.DataFrame(dict_GA) 

    d = id_ga
    print(len(d))
    GA = GA.head(8)
    return GA

def Sabrina():
    SabrinaI = "https://www.nike.com/es/w/sabrina-ionescu-baloncesto-zapatillas-2h3kpz3glsmz3rauvz5e1x6znik1zy7ok"
    name_si = get_name(SabrinaI)
    id_si = get_nike_ids(SabrinaI)
    price_si = get_prices(SabrinaI)
    gender_si = get_gender(SabrinaI)
    colors_si = available_count_colors(SabrinaI)

    dict_SI = {
        "name": name_si,
        "id": id_si,
        "price": price_si,
        "gender": gender_si,
        "colors": colors_si
    }

    max_length = max(len(value) for value in dict_SI.values())
    for key, value in dict_SI.items():
        dict_SI[key] = value + [0] * (max_length - len(value))
    SI = pd.DataFrame(dict_SI) 

    d = id_si
    print(len(d))
    SI= SI.head(3)
    return SI

def JaMorant():
    JaMorant = "https://www.nike.com/es/w/ja-morant-baloncesto-zapatillas-3glsmz3rauvz4m5h1z5e1x6znik1zy7ok"
    name_jm = get_name(JaMorant)
    id_jm = get_nike_ids(JaMorant)
    price_jm = get_prices(JaMorant)
    gender_jm= get_gender(JaMorant)
    colors_jm = available_count_colors(JaMorant)

    dict_JM = {
        "name": name_jm,
        "id": id_jm,
        "price": price_jm,
        "gender": gender_jm,
        "colors": colors_jm
    }

    max_length = max(len(value) for value in dict_JM.values())
    for key, value in dict_JM.items():
        dict_JM[key] = value + [0] * (max_length - len(value))
    JM = pd.DataFrame(dict_JM) 

    d = id_jm
    print(len(d))

    JM= JM.head(3)
    return JM

def RussellWestbrook():
    RussellWestbrook = "https://www.nike.com/es/w/russell-westbrook-baloncesto-zapatillas-3glsmz3rauvz5e1x6z8ib36znik1zy7ok"
    name_rw = get_name(RussellWestbrook)
    id_rw = get_nike_ids(RussellWestbrook)
    price_rw = get_prices(RussellWestbrook)
    gender_rw = get_gender(RussellWestbrook)
    colors_rw = available_count_colors(RussellWestbrook)
    dict_RW = {
        "name": name_rw,
        "id": id_rw,
        "price": price_rw,
        "gender": gender_rw,
        "colors": colors_rw
    }

    max_length = max(len(value) for value in dict_RW.values())
    for key, value in dict_RW.items():
        dict_RW[key] = value + [0] * (max_length - len(value))
    RW= pd.DataFrame(dict_RW) 

    d = id_rw
    print(len(d))
    RW= RW.head(8)
    return RW

def JordanBasket():
    Basketj = "https://www.nike.com/es/w/jordan-baloncesto-zapatillas-37eefz3glsmzy7ok"
    name_bj = get_name(Basketj)
    id_bj = get_nike_ids(Basketj)
    price_bj = get_prices(Basketj)
    gender_bj= get_gender(Basketj)
    colors_bj = available_count_colors(Basketj)
    dict_JB = {
        "name": name_bj,
        "id": id_bj,
        "price": price_bj,
        "gender": gender_bj,
        "colors": colors_bj
    }

    max_length = max(len(value) for value in dict_JB.values())
    for key, value in dict_JB.items():
        dict_JB[key] = value + [0] * (max_length - len(value))
    JB = pd.DataFrame(dict_JB) 

    d = id_bj
    print(len(d))
    JB= JB.head(24)
    return JB