from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  

def search_and_extract(term):
    driver.get("https://www.wikipedia.org/")
    
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys(term)
    
    driver.find_element(By.CSS_SELECTOR, "button.pure-button").click()
    
    time.sleep(2)
    
    try:
        title = driver.find_element(By.ID, "firstHeading").text
        print(f"\n📘 Title: {title}")
    except Exception as e:
        print(f"\n❌ Could not get title for {term} — {e}")
        return

    try:
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p")
        first_para = ""
        for p in paragraphs:
            text = p.text.strip()
            if text:
                first_para = text
                break

        if first_para:
            print(f"📝 First Paragraph:\n{first_para}")
        else:
            print("📝 No meaningful paragraph found.")
    except Exception as e:
        print(f"❌ Error while extracting paragraph: {e}")

search_terms = ["Python (programming language)", "Selenium (software)", "Test automation"]

for term in search_terms:
    search_and_extract(term)

driver.quit()
