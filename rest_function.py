#!/usr/bin/env python

def my_function():
    # importing necessary libraries
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    names = []
    no_of_reviews = []
    rating = []
    category=[]

    for page in range(0,50,10):
        url=f'https://www.yelp.com/search?find_desc=Restaurants&l=a%3A38.7964144%2C-90.8495939%2C27.346&start={page}'
        soup = BeautifulSoup(requests.get(url).text,'html.parser')
        
        try:
            
            all_divs = soup.find_all("div",class_="businessName__09f24__EYSZE display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")
            for i in all_divs:
                rest_names = i.find('a', class_='css-1422juy').text
                names.append(rest_names)
            
            
            review = soup.find_all("div", class_="attribute__09f24__hqUj7 display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")
            for i in review:
                reviews = i.find('span', class_="reviewCount__09f24__tnBk4 css-1e4fdj9").text
                no_of_reviews.append(reviews)

            
            rating_star = soup.find_all("div", class_="attribute__09f24__hqUj7 display--inline-block__09f24__fEDiJ margin-r1__09f24__rN_ga border-color--default__09f24__NPAKY")
            for i in rating_star:
                for j in i:
                    ratings = j.div['aria-label']
                    rating.append(ratings)

            price_category = soup.find_all("div",class_="priceCategory__09f24__svarC iaPriceCategory__09f24__GPx_c display--inline-block__09f24__fEDiJ margin-t1__09f24__w96jn border-color--default__09f24__NPAKY")
            
            for i in price_category:
                p_tags = i.find_all('p', class_='css-1p8aobs')
                categoryTemp = []
                for j in p_tags:
                    categoryTemp.append(j.getText())
                category.append(categoryTemp)
        except Exception as e:
            print(e)

    # Creating Data frame
    dictionary = {'Restaurant_Name':names,
                'Categories':category,
                'no_of_reviews':no_of_reviews,
                'Rating':rating}
    return dictionary 