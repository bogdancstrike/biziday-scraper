# Biziday.ro Scraper

- Only articles summary and posted date are extracted
- Exports extracted articles to json file (`articles.json`)

### Pre-configuration

Edit file `main.py` line `35` with your absolute path:

```code
chrome_options.add_argument(r"--user-data-dir=C:\\Users\\[YOUR_USER]\\AppData\\Local\\Google\\Chrome\\User Data")
```

### ARGS

- `-s` or `--scrolls` - optional parameter - how many scrolls to load (how many times to press "Load More Articles) button. Default is `2`
- `-d` or `--date` - optional parameter - it will show as output the number of articles scraped in that date. Format is `YYYY-mm-dd` (example `2023-04-22`). Default is `today`

## RUN

```python
python3 .\main.py -s 5 -d 2023-04-22 
```