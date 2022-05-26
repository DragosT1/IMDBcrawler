# Scraper common project

### Pull
git clone git@github.com:unknownliviu/demoscraper.git

### First time install
In the project root folder of demoscraper, install your virtualenv
```
pip install virtualenv

virtualenv venv

source venv/bin/activate

```
*Please note* you may have to run `source venv/bin/activate` every time you cd into this folder to load its own env. your shell will add a (venv) before your username

### Install dependencies
`source venv/bin/activate` to make sure you load the venv
then 
`pip install -r requirements.txt` 


## How to list and run scrapers
`cd jokes` 
`ls` should show `scrapy.cfg` here

Then run `scrapy list` to see which scrapers are available
Finally, run `scrapy crawl <spidername>` to run a specific spider

## Docs
https://docs.scrapy.org/en/latest/intro/tutorial.html read this for more info