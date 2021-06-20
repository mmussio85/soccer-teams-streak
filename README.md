# soccer-teams-streak
Playing around with BeatifulSoap for scraping and Data Bricks/Apache Spark for data processing.

## scraper.py

This is a Python script using BeatifulSoup for scraping the web site "https://www.sobrefutbol.com/torneos/torneo_uruguayo.htm" which contains a table with all the champions in the uruguayan soccer league by year. Once the script is executed, a file championships.csv is retrieved in the format <year_od_championship, champion, runner-up>

###### requirements.txt

Contains the libraries needed for scraping the web site.

Run the script below within the directory to create the virtual environment:
> python3 -m venv env

In order to start the virtual environment run the script below:
> source env/bin/activate

Finally, run the scraper script in order to get the information needed from the page:
> python3 scraper.py

## champions.ipnyb 

All the queries performed in Data Bricks, written in PySpark.
The main goal of the last query is to order each team by the largest streak in uruguayan soccer history.


