from nba_api.stats.static import players
from selenium import webdriver
import random
import os

def getCards():
    player_list = players.get_players()

    pack = []
    for num in range(10):
        pack.append(random.choice(player_list))

    option = webdriver.FirefoxOptions()
    option.add_argument('--headless')
    browser = webdriver.Firefox(options=option)
    browser.set_window_size(2000, 1000)
    browser.execute_script("window.scrollTo(0, 200)")
    query = []
    file_names = []
    for card in pack:
        query = card['full_name'] + " basketball card"
        url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={query}"
        browser.get(url)
        elements = browser.find_elements_by_class_name('rg_i')
        elements[0].click()
        #file_name = card['full_name'] + ".png"
        file_name = "./static/" + card['full_name'] + ".png"
        file_names.append(card['full_name'] + ".png")
        browser.find_element_by_class_name('eHAdSb').screenshot(file_name)

    browser.close()
    return file_names

def getPack():
    # Read in 8 cards from existing files
    player_list = os.listdir('./static/')

    pack = []
    for num in range(10):
        card = random.choice(player_list)
        if card.endswith(".png"):
            pack.append(card)
        print (card)
    return pack
    