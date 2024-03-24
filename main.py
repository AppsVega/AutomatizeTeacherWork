from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl
from time import sleep

print("Lembre que caso os dados preenchidos não estiverem corretos o programa pode não funcionar!")
CPF = str(input("Digite aqui seu cpf: "))
SENHA = str(input("Digite aqui sua senha: "))
DESC = str(input("Digite aqui o nome da avalaição: "))
PONTOS = str(input("Digite aqui a quantidade de pontos: "))
ALUNOSQNT = int(input("Digite aqui a quantidade de Alunos: "))
WORKBOOK = str(input("Digite aqui o caminho do arquivo XLSX: "))
PAGINA = str(input("Digite o nome da Página do arquivo xlsx que você deseja usar"))
NOTALIST = []

try:
    wb = openpyxl.load_workbook(filename= WORKBOOK, data_only=True, keep_vba=True)
    sheet = wb[PAGINA]

    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument('log-level=3')

    driver = Chrome(options=options)

    driver.get("https://dedmais.educacao.mg.gov.br/")

    sleep(4)

    cpf_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div[3]/div/div[2]/div/form/div[1]/input')
    cpf_input.send_keys(CPF)

    senha_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div[3]/div/div[2]/div/form/div[2]/div[1]/input')
    senha_input.send_keys(SENHA)

    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div[3]/div/div[2]/div/form/div[4]/button[2]')
    login_button.click()

    sleep(4)

    turma_button = driver.find_element(By.CLASS_NAME, "v-card--link")
    turma_button.click()
    sleep(3)
    ava_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/button")
    ava_button.click()

    sleep(3)

    cad_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/div/div/div[2]/button')
    cad_button.click()

    desc_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[2]/form/div[1]/div/input')
    desc_input.send_keys(DESC)

    val_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[2]/form/div[4]/div/input')
    val_input.send_keys(PONTOS)

    salv_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[2]/form/div[5]/button[2]')
    salv_button.click()

    sleep(3)

    div_desc_xpath = f'//div[contains(text(), "{DESC}")]'
    desc_element = driver.find_element(By.XPATH, div_desc_xpath)
    desc_element.click()

    sleep(3)

    for row in sheet.iter_rows(min_row=1, max_row=ALUNOSQNT, min_col=26, max_col=26):  # Coluna Z é a 26ª coluna
        for cell in row:
            NOTALIST.append(cell.value)

    elements = driver.find_elements(By.XPATH, "//*[@class='rounded-pill custom-input px-2 font-size-15 bg-white nota']")
    for i, val in zip(elements, range(0, ALUNOSQNT)):
        i.send_keys(NOTALIST[val])
        print(val)

    sleep(5)

    salv2_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/main/div/div/template/button')
    salv2_button.click()

    sleep(3)

    driver.close()
except:
    pass