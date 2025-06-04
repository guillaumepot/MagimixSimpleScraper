# MagimixSimpleScraper

A comprehensive Python web scraper designed to extract recipe data from the Magimix website (https://www.magimix.fr). This tool efficiently scrapes recipe information including names, categories, cooking times, ingredients, and more, making it perfect for recipe analysis, meal planning applications, or culinary data research.

<img src="./media/magimix_app.jpeg" width="350" height="350" alt="Magimix App Screenshot">

## 🚀 Features

- **Comprehensive Recipe Extraction**: Scrapes detailed recipe information including:
  - Recipe names and categories (tags)
  - Author information
  - Cooking times (preparation, cooking, total, and rest time)
  - Complete ingredient lists with quantities
  - Recipe URLs and image links
  - Page location for reference

- **Two-Stage Scraping Process**:
  1. **URL Collection**: First extracts all recipe URLs from paginated listing pages
  2. **Detailed Scraping**: Then visits each recipe page to extract comprehensive details

- **Robust Error Handling**: Continues scraping even when individual recipes fail to load
- **Progress Tracking**: Real-time progress indicators and performance metrics
- **Data Export**: Saves all data to CSV files for easy analysis and integration

## 📊 Project Information

- **Version**: 0.1.0
- **Development Stage**: Production Ready
- **Author**: Guillaume Pot
- **Contact**: guillaumepot.pro@outlook.com
- **License**: MIT License
- **Language**: French recipes (from Magimix France website)

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Output](#data-output)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

### Prerequisites

- Python 3.7 or higher
- Conda (recommended) or pip

### Using Conda (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/your-username/MagimixSimpleScraper.git
cd MagimixSimpleScraper
```

2. Create and activate the environment:
```bash
conda env create -f environment.yml
conda activate magimix-scraper
```

### Using pip

```bash
pip install beautifulsoup4 lxml pandas requests
```

## ⚡ Quick Start

1. **Scrape Recipe URLs** (First step):
```bash
cd utils
python recipe_url_scraper.py
# Choose option 1 when prompted
```

2. **Scrape Detailed Recipe Information** (Second step):
```bash
python recipe_url_scraper.py
# Choose option 2 when prompted
```

## 🎯 Usage

The scraper provides two main functions that can be used independently or in sequence:

### Option 1: Scrape Recipe URLs

Extracts basic information from all recipe listing pages:
- Recipe names
- Categories/tags
- Image URLs
- Recipe page URLs

```python
from utils.recipe_url_scraper import scrap_recipes_url
scrap_recipes_url()
```

**Output**: `storage/recipes_url.csv` (~3,900+ recipes)

### Option 2: Scrape Detailed Recipe Information

Visits each recipe URL to extract comprehensive details:
- Author information
- Detailed timing information
- Complete ingredient lists
- Serving quantities

```python
from utils.recipe_url_scraper import scrap_recipes_ingredients
scrap_recipes_ingredients()
```

**Output**: `storage/recipes_ingredients.csv`

### Interactive Mode

Run the script interactively:

```bash
python utils/recipe_url_scraper.py
```

You'll be prompted to choose:
- `1` - Scrape recipes URL
- `2` - Scrape recipes ingredients

## 📁 Project Structure

```
MagimixSimpleScraper/
├── utils/
│   └── recipe_url_scraper.py    # Main scraping functionality
├── storage/
│   ├── recipes_url.csv          # Basic recipe information (~654KB)
│   ├── recipes_ingredients.csv  # Detailed recipe data (~1MB)
│   └── recipes_full_datas.csv   # Complete dataset (~1.5MB)
├── media/
│   └── magimix_app.jpeg        # Project screenshot
├── environment.yml             # Conda environment configuration
├── LICENSE                     # MIT License
└── README.md                   # This file
```

## 📈 Data Output

### Basic Recipe Data (`recipes_url.csv`)
- `recipe_name`: Name of the recipe
- `tag`: Recipe category (e.g., DESSERTS, SOUPES, VIANDES)
- `image_url`: Direct link to recipe image
- `recipe_url`: Full URL to recipe page
- `page`: Source page number

### Detailed Recipe Data (`recipes_ingredients.csv`)
- `recipe_name`: Name of the recipe
- `author`: Recipe author
- `preparation_time`: Time needed for preparation
- `cook_time`: Cooking/baking time
- `total_time`: Total time required
- `rest_time`: Resting/waiting time
- `quantity`: Serving size information
- `ingredients`: Complete ingredient list

### Sample Data
Current dataset contains **3,900+ recipes** across categories including:
- DESSERTS (Desserts)
- SOUPES (Soups)
- VIANDES (Meat dishes)
- VÉGÉTARIENS (Vegetarian)
- POISSONS (Fish/Seafood)
- LÉGUMES (Vegetables)
- APÉRITIFS (Appetizers)
- BOISSONS (Beverages)
- And more...

## 🛠 Dependencies

- **beautifulsoup4**: HTML parsing and web scraping
- **lxml**: Fast XML and HTML parser
- **pandas**: Data manipulation and CSV export
- **requests**: HTTP library for web requests
- **time**: Built-in timing and delays

## ⚙️ Configuration

The scraper uses several configurable variables in `recipe_url_scraper.py`:

- `base_url`: Starting URL for recipe listings
- `parser`: HTML parser type ("lxml")
- `recipe_url_file`: Output file path for URLs

## 🔍 Error Handling

The scraper includes robust error handling:
- Continues processing if individual recipes fail
- Reports number of failed recipes
- Logs errors with recipe names for debugging
- Provides timing information for performance monitoring

## 🚧 Roadmap

- [x] Extract basic recipe information
- [x] Scrape detailed recipe data
- [x] Implement error handling and progress tracking
- [ ] Add recipe search functionality by ingredients
- [ ] Implement data filtering and analysis tools
- [ ] Add support for multiple languages/regions
- [ ] Create API endpoints for data access
- [ ] Add recipe recommendation system

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Legal Notice

This scraper is for educational and research purposes. Please ensure you comply with:
- Magimix website's robots.txt and terms of service
- Applicable data protection laws
- Respectful usage patterns (avoid overwhelming the server)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Guillaume Pot**
- Email: guillaumepot.pro@outlook.com
- Project Link: [https://github.com/your-username/MagimixSimpleScraper](https://github.com/your-username/MagimixSimpleScraper)

---

⭐ **Star this repository if you find it helpful!**