"""
Recipe name & URL scraper
"""
# Version : 0.1.0
# Current state : Dev
# Author : Guillaume Pot
# Contact : guillaumepot.pro@outlook.com


"""
LIBS
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import time

"""
VARS
"""
parser = "lxml"
base_url = "https://www.magimix.fr/content/23-recettes?page=1"

recipe_url_file = "./storage/recipes_url.csv"


"""
Functions
"""
def scrap_recipes_url() -> None:
    """
    Scrapes the URLs of recipes from the Magimix website and saves them in a CSV file.

    This function performs the following steps:
    1. Retrieves the total number of pages from the website.
    2. Iterates over each page and extracts recipe names, tags, images, and links.
    3. Appends the extracted data to a list.
    4. Creates a DataFrame from the list and saves it as a CSV file.

    Note: This function requires the 'requests', 'beautifulsoup4', 'time', and 'pandas' libraries.

    Returns:
        None
    """

    # Get page number
    source_code = requests.get(base_url)
    soup = bs(source_code.content, parser)
    last_page_class = soup.find('span', class_= "page-link page-number")
    last_page_number = int(last_page_class.text.strip().split('/')[-1])
    print(f"There is {last_page_number} pages")


    # Initialize recipes list
    recipes = []


    # Iterate over pages
    print("Scraping...")

    start_time = time.time()
    for i in range(1, last_page_number+1):
        url = f"https://www.magimix.fr/content/23-recettes?page={i}"
        page = i

        # Get source
        source_code = requests.get(url)
        soup = bs(source_code.content, parser)

        # Get recipe names
        recipe_names = soup.find_all('div', class_="rse_results-recipes_title")
        # Get recipe tags
        recipe_tag = soup.find_all('div', class_="rse_results-recipes_type")
        # Get recipe images
        recipe_images_url = soup.find_all('img', class_="rse_results-recipes_picture")
        # Get recipe links
        recipe_links = soup.find_all('a', class_='rse_results-recipes_href')


        # Iterate over recipes
        for recipe_name, tag, image, link in zip(recipe_names, recipe_tag, recipe_images_url, recipe_links):
            # Access attributes inside the loop
            image_url = image['src']
            link_url = link['href']
            recipes.append((recipe_name.text.strip(), tag.text.strip(), image_url, link_url, page))


    end_time = time.time()
    print(f"Scraping done in {end_time - start_time} seconds")



    # Create DataFrame & save a CSV file
    print("Creating DataFrame...")
    df = pd.DataFrame(recipes, columns=['recipe_name', 'tag', 'image_url', 'recipe_url', 'page'])
    df['recipe_url'] = df['recipe_url'].apply(lambda x: f"https://www.magimix.fr{x}")
    df.to_csv(recipe_url_file, index=False)
    print(f"DataFrame created and saved in {recipe_url_file}")



def scrap_recipes_ingredients(recipe_url_file = "./storage/recipes_url.csv") -> None:
    """
    Scrapes recipe information from the provided URLs and saves the data as a CSV file.

    Args:
        recipe_url_file (str): The file path of the CSV file containing recipe URLs. Default is "./storage/recipes_url.csv".

    Returns:
        None

    Raises:
        None

    """

    # Recipes URL DF
    recipe_url_df = pd.read_csv(recipe_url_file)

    recipe_not_found_nb = 0

    # Initialize recipes list
    recipes = []


    # Iterate over each recipe
    print("Scraping...")
    start_time = time.time()

    for i in range(len(recipe_url_df)):
        try:
            # Get recipe name & url
            recipe_name = recipe_url_df.loc[i, 'recipe_name']
            recipe_url = recipe_url_df.loc[i, 'recipe_url']

            print(f"Scraping {recipe_name}, number {i} of {len(recipe_url_df)}")

            # Get source
            source_code = requests.get(recipe_url)
            soup = bs(source_code.content, parser)

            # Get Recipe informations
            ## Author
            author = soup.find('span', class_ = "author").text.split(":")[1].strip()


            ## Recipe Preparation block
            preparation_block = soup.find_all('div', class_ = "recipe-preparation-info")

            # Iterate over each div in preparation_block
            times = []
            for div in preparation_block:
                # Convert div to text
                div_text = div.text

                # Preparation time
                t = div_text.split(":")[1].strip()
                times.append(t)

            # Preparation time
            preparation_time = times[0]
            # Cooking time
            cook_time = times[1]
            # Total time
            total_time = times[2]
            # Rest time
            rest_time = times[3]


            ## Quantity
            quantity = soup.find('div', class_ = "recipe-ingredients-title").text.strip()

            ## Ingredients
            ingredients = []
            ingredient_list = soup.find_all('div', class_ = "recipe-ingredients-content")
            for ingredient in ingredient_list:
                ingredients.extend([line.strip() for line in ingredient.text.split('\n') if line.strip()])

            recipes.append((recipe_name, author, preparation_time, cook_time, total_time, rest_time, quantity, ingredients))

        except Exception as e:
            print(f"Error scraping {recipe_name}: {e}")
            recipe_not_found_nb += 1
            print("Recipe not found")
            author = "Not found"
            preparation_time = "Not found"
            cook_time = "Not found"
            total_time = "Not found"
            rest_time = "Not found"
            quantity = "Not found"
            ingredients = "Not found"
            recipe_not_found_nb += 1
            recipes.append((recipe_name, author, preparation_time, cook_time, total_time, rest_time, quantity, ingredients))


    end_time = time.time()
    print(f"Scraping done in {end_time - start_time} seconds \n {recipe_not_found_nb} recipes not found.")


    # Create DF & Save as CSV file
    print("Creating DataFrame...")
    df = pd.DataFrame(recipes, columns=['recipe_name', 'author', 'preparation_time', 'cook_time', 'total_time', 'rest_time', 'quantity', 'ingredients'])
    df.to_csv(f'../storage/recipes_ingredients.csv', index=False)
    print(f"DataFrame created and saved in {recipe_url_file}")




if __name__ == "__main__":
    print("Choose a task to perform: \n 1 - Scrap recipes URL \n 2 - Scrap recipes ingredients \n")
    task = input("Enter a number: ")
    task = int(task)

    if task == 1:
        scrap_recipes_url()
    elif task == 2:
        scrap_recipes_ingredients()
    else:
        print("Invalid input")