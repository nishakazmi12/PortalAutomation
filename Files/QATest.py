def process_word(word):
    if word.endswith("ed") or word.endswith("ly"):
        word = word[:-2]
    elif word.endswith("ing"):
        word = word[:-3]

    if len(word) > 8:
        word = word[:8]

    return word

sentence = "Walking running playing beautifully coding programming"
words = sentence.split(" ")

processed_words = [process_word(word) for word in words]
output_sentence = " ".join(processed_words)

print(output_sentence)


Absolutely, here are the questions along with their answers:

**Question 1: Counting Elements in a List**

```python
def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count, odd_count = count_even_odd(numbers)
print("Even count:", even_count)
print("Odd count:", odd_count)
```

**Question 2: Web Scraping with Selenium**

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium")
search_button = driver.find_element_by_name("btnK")
search_button.click()

results = driver.find_elements_by_css_selector("h3")
for result in results:
    print(result.text)

driver.quit()
```

**Question 3: Finding Palindromes**

```python
def is_palindrome(word):
    return word == word[::-1]

word = "radar"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
```

**Question 4: Sorting a List of Dictionaries**

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)
```

**Question 5: Data Validation**

```python
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

email = "test@example.com"
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
```

**Question 6: Webpage Interaction with Selenium**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.example.com")
link = driver.find_element_by_link_text("Learn More")
link.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2")))
print(element.text)

driver.quit()
```

**Question 7: Reverse Words in a Sentence**

```python
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

sentence = "Hello World"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)
```

**Question 8: File Processing and Regex**

```python
import re

pattern = r'\b\d{3}-\d{2}-\d{4}\b'
with open("data.txt", "r") as file:
    content = file.read()
    matches = re.findall(pattern, content)
    print(matches)
```

**Question 9: Handling Dropdowns with Selenium**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.example.com")
dropdown = Select(driver.find_element_by_name("dropdown"))
dropdown.select_by_visible_text("Option 2")

selected_option = dropdown.first_selected_option.text
print("Selected option:", selected_option)

driver.quit()
```

**Question 10: String Manipulation**

```python
def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

sentence = "hello world"
capitalized_sentence = capitalize_words(sentence)
print(capitalized_sentence)
```

These answers should help you understand how to approach each scripting question. Feel free to experiment and modify the code as needed for your practice.

