from selenium import webdriver
import time

print('ВАТАФАК')
# Инициализация WebDriver
driver = webdriver.Chrome()
print('АФА')

# Загрузка страницы
driver.get("https://become-iron.github.io/ovz_calc/")

# Ввод значений
driver.execute_script("$('.D').val('49');")
driver.execute_script("$('.Dmax').val('49.039');")
driver.execute_script("$('.Dmin').val('49');")
driver.execute_script("$('.d').val('49');")
driver.execute_script("$('.dmax').val('49');")
driver.execute_script("$('.dmin').val('48,961');")
driver.execute_script("$('.Smax').val('0');")
driver.execute_script("$('.Smin').val('');")
driver.execute_script("$('.Nmax').val('0');")
driver.execute_script("$('.Nmin').val('');")
driver.execute_script("$('.TD').val('0,039');")
driver.execute_script("$('.Td').val('0,039');")

# Нажатие кнопки "Расчет"
driver.execute_script("calculate()")

# Ожидание завершения расчета и отрисовки графика
time.sleep(2)

# Сохранение скриншота страницы с графиком
driver.save_screenshot("graph.png")

# Закрытие браузера
driver.quit()
