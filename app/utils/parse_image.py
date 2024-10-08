from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from cairosvg import svg2png



def parse_image(D: float|int, ES: float|int, EI: float|int, es: float|int, ei: float|int) -> None:
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://become-iron.github.io/ovz_calc/")
    for i in [("D", D),("ES", ES),("EI", EI),("es", es),("ei", ei)]:
        elem = driver.find_element(By.XPATH, f"//input[contains(@class, 'field {i[0]} form-control input-sm')]")
        elem.click()
        elem.send_keys(i[1])
    button = driver.find_element(By.XPATH, "//input[@type='button' and @value='Считать' and contains(@class, 'btn-primary')]")
    button.click()
    button2 = driver.find_element(By.XPATH, "//input[@value='Показать/скрыть схему']")
    button2.click()
    graph = driver.find_element(By.CSS_SELECTOR, "svg")
    svg_content = graph.get_attribute("innerHTML").replace("undefined0", "")
    with open("svg_output.svg", "w", encoding="utf-8") as file:
        file.write(f"<svg xmlns='http://www.w3.org/2000/svg' height='249.76' width='413.75'>{svg_content}</svg>")
    svg2png(url="svg_output.svg", write_to="svg_output.png")
    driver.close()