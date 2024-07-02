# MagimixSimpleScraper

Simple Magimix recipes scraper from Magimix website.

Current recipes language(s):
- French


<img src="./media/magimix_app.jpeg" width="350" height="350">




## Project information
- **Version**: 0.1.0
- **Development Stage**: Prod
- **Author**: Guillaume Pot
- **Contact Information**: guillaumepot.pro@outlook.com



## Purpose:
- Get all recipes, for each recipe :
    - Name
    - Tag
    - Image
    - URL
    - Author
    - Times (preparation, cooking, total time, rest)
    - Ingredients

- Submit one or several ingredients & get associated recipes


## Table of Contents
- [Repo Architecture] (#repo-architecture)
- [Checklist](#checklist)


## Repo Architecture
```
├── .github
│   └── workflows
│
├── README.md
│
├── LICENSE
│
├── environment.yml
│
├── media
|
├── storage
│
└── utils
    │
    └── recipe_url_scraper.py

```

## Roadmap
- [Done] Get informations for each recipe
- [Done] Scrap recipes URL