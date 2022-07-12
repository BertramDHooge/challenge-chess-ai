# challenge-chess-ai

Dataset: https://www.kaggle.com/datasets/datasnaek/chess
https://database.lichess.org/ May 2022

### Solo Project

<h2 align="center">Collecting data challenge</h2>
<p align="center"><a href="https://github.com/CorentinChanet/challenge-collecting-data">
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200"></a></p>
<h3 align="center"> Web scraping group project at <a href="https://github.com/becodeorg"><strong>BeCode</strong></a></h3>
<h3 align="center"> Contributors: <a href="https://github.com/Len-Fid">Lena, <a href="https://github.com/anikaarevalo">Anika,<a href="https://https://github.com/BertramDHooge"> Bertram</a></h3><br>

  
## The timeline of the project: 
**28/02/22 - 01/03/22**


## Objectives of the project: 
* Scrape a website containing information about the Belgian house market
* Build a dataset from scratch

## Libraries used:
* Selenium 
* BeautifulSoup
* Pandas 
* JSON

## Usage:
* The code can be run through [this file in Jupyter Notebook](https://github.com/Len-Fid/challenge-collecting-data/blob/main/scraping_that_demo.ipynb)
* Demo version containing 30 links can be seen in [this file](https://github.com/Len-Fid/challenge-collecting-data/blob/main/scraping_that_demo.ipynb)

## Walk through of this DIY scraping challenge:

* Locating elements of the source code of the requisite URL from the immoweb.be/en web site
* Extracting targeted elements (links) asynchronously per web get and saving these links by creating a list in a soup file for parsing
* Creating a data frame using pandas for approximately 10,000 inputs
* Saving everything in a CSV file

## Dataset details:
Dataset contains the following columns :

- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale (Exclusion of life sales)
- Number of rooms
- Area
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No)
  - If yes: Area
- Garden (Yes/No)
  - If yes: Area
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)
