# CZ1016 Kdrama Chemistry Matcher
Done by: Chen Xing Yu, Jacintha Wee, Valencia Lie

## 1. Scraping
1.1. kdrama.py: spider for scraping the url of all dramas

1.2. basic_cleaning.ipynb: basic cleaning of the csv scraped from the spider above

1.3. actor_info.py: spider for scraping general information

1.4. cleaning.ipynb:  basic cleaning of the csv scraped from actor_info.py

1.5. ind_re.py: spider for scraping kdrama reviews

## 2. EDA

2.1. EDA.ipynb: Jupyter notebook containing EDA on general information and reviews

## 3. Review Analysis

### Preprocessing
3.1. kdrama.ipynb: count number of reviews for each drama and drop the ones with not enough reviews

3.2. coref.ipynb: drop non-English reviews, convert emojis/emoticons, replace pronouns (requirements_coref.txt as the virtual environment)

### Pattern-matching and sentiment analysis
3.3. senti.ipynb: extract lines with keywords from reviews, find pairs from each line and do sentiment analysis for each pair

## 4. Facial analysis
4.1. Image.py: scrape images off the mydramalist website using the url scraped previously and converting the images into grayscale

4.1. facial_similarity.ipynb: do facial similarity analysis on all images of actors that we scraped before. Match these actors and actresses with the output csv in the senti.ipynb accordingly (e.g. actor A looks the most similar to actor B and actor B is matched with actress C). (requirements_vgg.txt as the virtual environment)

## 5. Visualisation 

5.1. dataset_visualisation.ipynb: find who are the baseline actors and actresses (those who do not need facial similarity at all and can just be matched naturally using sentiment analysis) as well as the ‘newcomers’ and clean the csv so that it is fit for our dashboard.

5.2. global.R: all the csv we have generated will be put in this file so that our ui and server file can always access it.

5.3. ui.R: the design of the dashboard as well as its structure

5.4. server.R: the interactive aspect of the dashboard so that it is able to function the way we want to.

To access the dashboard, please go to: https://valencialie11.shinyapps.io/actormatcher/
