# MagimixSimpleScraper

Simple Magimix recipes scraper from Magimix website.

Current recipes language(s):
- French


**Purpose:**
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

├── .github
│   └── workflows
│
├── README.md
│
├── LICENSE
│
├── environment.yml
│
├── storage
│
└── utils
    │
    └── recipe_url_scraper.py



## Checklist
- [Done] Get informations for each recipe
- [Done] Scrap recipes URL