import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import cairosvg

API_TOKEN = '6799002283:AAGq3QOfXlzYzQQLQw_BOyP-QYKp2qKpT08'

bot = telebot.TeleBot(API_TOKEN)

def get_image(D, ES, EI, es, ei):
    driver = webdriver.Chrome()
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
    cairosvg.svg2png(url='svg_output.svg', write_to='output.png')
    driver.close()

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Привет! Пиши в формат 
D=
ES=
EI=
es=
ei=
К примеру:
45
0,039
0
0
-0,039""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # bot.send_message(message.chat.id, message.text)
    text=message.text
    text=text.replace(",", ".").split("\n")
    #D max = D + ES
    #D min = D + EI
    #d max = D + es
    #d min = D + ei
    #TD = Dmax-Dmin
    #Td = dmax-dmin
    #Smax = Dmax-dmin
    #Smin = Dmin-dmax
    #Nmax = dmax-Dmin
    #Nmin = dmin-Dmax
    #text[0] = D
    #text[1] = ES
    #text[2] = EI
    #text[3] = es
    #text[4] = ei
    Dmax = float(text[0])+float(text[1])
    Dmin = float(text[0])+float(text[2])
    dmax = float(text[0])+float(text[3])
    dmin = float(text[0])+float(text[4])
    print(Dmax,Dmin,dmax,dmin)
    TD = format(float(Dmax)-float(Dmin), ".3f")
    Td = format(float(dmax)-float(dmin), ".3f")
    Smax = format(float(Dmax)-float(dmin), ".3f")
    Smin = format(float(Dmin)-float(dmax), ".3f")
    Smid = format((float(Smax)+float(Smin))/2, ".3f")
    Nmax = format(float(dmax)-float(Dmin), ".3f")
    Nmin = format(float(dmin)-float(Dmax), ".3f")
    Nmid = format((float(Nmax)+float(Nmin))/2, ".3f")
    if (Dmin>dmax):
        case = 2
        answer = "Это зазор"
    elif (Dmax<dmin):
        case = 3
        answer = "Это натяг"
    else:
        case = 1
        answer = "Это общее положение (Переходная)"
    response = f"""
Ответ на ваш вариант:
Dmax = D + ES = {text[0]} + {text[1]} = {Dmax}
Dmin = D + EI = {text[0]}+ {text[2]} = {Dmin}
TD = Dmax - Dmin = {Dmax} - {Dmin} = {TD}
TD = ES - EI = {text[1]} - {text[2]} = {TD}
dmax = D + es = {text[0]} + {text[3]} = {dmax}
dmin = D + ei = {text[0]} + {text[4]} = {dmin}
Td = dmax - dmin = {dmax} - {dmin} = {Td}
Td = es - ei = {text[3]} - {text[4]} = {Td}"""
    match case:
        case 1:
            response += "\n"+answer + f"""
Smax = Dmax - dmin = {Dmax} - {dmin} = {Smax}
Nmax = dmax - Dmin = {dmax} - {Dmin} = {Nmax}"""
        case 2:
            response += "\n"+answer + f"""
Smax = Dmax - dmin = {Dmax} - {dmin} = {Smax}
Smin = Dmin - dmax = {Dmin} - {dmax} = {Smin}
Smid = (Smax + Smin)/2 = ({Smax} + {Smin}) / 2 = {Smid}"""
        case 3:
            response += "\n"+answer + f"""
Nmax = dmax - Dmin = {dmax} - {Dmin} = {Nmax}
Nmin = dmin - Dmax = {dmin} - {Dmax} = {Nmin}
Nmid = (Nmax + Nmin)/2 = ({Nmax} + {Nmin}) / 2 = {Nmid}"""
    get_image(text[0], text[1], text[2], text[3], text[4])
    buf = open("output.png", "rb")
    bot.send_photo(message.chat.id, buf, caption=response)
    #bot.send_message(message.chat.id, response)
    print(response)
    print(message.from_user.username)

bot.infinity_polling()