# pixiv-scraper
Scraper that anonymously scrapes images from pixiv.net and filteres out adult content.

Used by me to get an anime picture dataset for deep learning project.

### File structure
```
.
├── filter_adult_content.py       # moves adult rated images too separate folder
├── get_proxies.py                # generates up to date proxy list (when scraper is run)
├── images                        # folder for images
├── pixivScrape                   # scraper main files
│   ├── pipelines.py              # processing for scraped data
│   ├── proxy_list.txt            # list generated by get_proxies.py
│   ├── settings.py               # scraper settings
│   └── spiders
│       ├── pixiv.py              # crawler for pixiv.net
│       └── rotate_useragent.py   # middleware for rotating user agent
├── README.md
└── scrapy.cfg                    # project config
```

#### Requirements
Scraper is made on scrapy framework, it mainly requires scrapy and scrapy-proxy

### Setup
```
git clone https://github.com/Stsh4lson/pixiv-scraper
cd pixiv-scraper
pip install -r requirements.txt
```
### Run
1. Scrape items `scrapy crawl pixiv -o items.json` (by default scrapes 100 days back (50k images))
2. Optionally move adult images to separate `images/adult` folder by `python filter_adult_content.py`

### Closing
If you want to close app in middle of execution using ctrl+c once will start gracefull shutdown. Using ctrl+c again will execute force shut down and files (like, items.json) could be incomplete.
**Gracefull shutdown could take up to 5 minutes.**
