# Biziday.ro Scraper

- Only articles summary and posted date are extracted
- Articles are automatically categorized in one of the following categories: Sport, Politics, Others
- Exports extracted articles to json file (`articles.json`)

### Pre-configuration

Edit file `main.py` line `35` with your absolute path:

```code
chrome_options.add_argument(r"--user-data-dir=C:\\Users\\[YOUR_USER]\\AppData\\Local\\Google\\Chrome\\User Data")
```

### ARGS

- `-s` or `--scrolls` - optional parameter - how many scrolls to load (how many times to press "Load More Articles button). Default is `2`
- `-d` or `--date` - optional parameter - it will show as output the number of articles scraped in that date. Format is `YYYY-mm-dd` (example `2023-04-22`). Default is `today`

## RUN

```code
python3 .\main.py -s 5 -d 2023-04-22 
```


### Example of output in `articles.json`

```json
[
    {
        "category": "Others",
        "text": "Mure\u0219. Un \u0219ofer a fost surprins de radarul poli\u021bi\u0219tilor \u00een timp ce circula cu 226 km/h pe autostrada A3. A fost amendat cu 2.900 de lei \u0219i a r\u0103mas f\u0103r\u0103 permis timp de patru luni.",
        "time": "2023-04-22"
    },
    {
        "category": "Others",
        "text": "Volkswagen va construi o fabric\u0103 de baterii pentru ma\u0219ini electrice \u00een Canada. Investi\u021bia de 15 miliarde de dolari va fi suportat\u0103 \u00een cea mai mare parte de guvernul canadian, sub forma unor subven\u021bii.",
        "time": "2023-04-22"
    },
    {
        "category": "Politcs",
        "text": "Sudan. Armata anun\u021b\u0103 c\u0103 cet\u0103\u021benii str\u0103ini din SUA, Marea Britanie, Fran\u021ba \u0219i China vor fi evacua\u021bi din \u021bar\u0103 \u00een urm\u0103toarele ore, pe fondul situa\u021biei tensionate din zon\u0103.",
        "time": "2023-04-22"
    },
    {
        "category": "Politcs",
        "text": "Analiz\u0103 Sky News. \u00cencheierea unei p\u0103ci \u00eentre Rusia \u0219i Ucraina va fi posibil\u0103 doar atunci c\u00e2nd cele dou\u0103 state vor fi epuizate, iar Occidentul va face presiuni \u00een acest sens.",
        "time": "2023-04-22"
    },
    {
        "category": "Others",
        "text": "SUA. Curtea Suprem\u0103 men\u021bine, momentan, accesul popula\u021biei la un medicament folosit la scar\u0103 larg\u0103 pentru avorturi. A suspendat astfel restric\u021biile decise de tribunalele statale.",
        "time": "2023-04-22"
    }
]
```