from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import winsound
import time

# 配置路徑
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chromedriver_path = (
    r"C:\Users\user\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
)

# 配置 Selenium
service = Service(chromedriver_path, log_path="chromedriver.log")
options = webdriver.ChromeOptions()
options.binary_location = chrome_path
options.add_argument("--log-level=3")
options.add_argument("--disable-gpu")
# options.add_argument('--headless')  # 無頭模式（穩定後啟用）

try:
    driver = webdriver.Chrome(service=service, options=options)
except Exception as e:
    print(f"無法啟動瀏覽器：{e}")
    exit(1)


def play_alert_sound():
    """播放提醒蜂鳴聲"""
    try:
        for _ in range(3):
            winsound.Beep(1000, 500)
    except Exception as e:
        print(f"播放聲音失敗：{e}")


# 定義票種優先順序（根據 Global Interpark 常見票種）
priority_order = ["VIP", "R", "S", "A"]

try:
    # 打開網站
    driver.get("https://www.globalinterpark.com/en/product/25005869")

    # 確保頁面加載完成
    WebDriverWait(driver, 5).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    print("頁面加載完成")

    # 檢查是否需要登錄
    time.sleep(50)

    # 點擊「Next Step」按鈕
    try:
        next_step_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "LargeNextBtnLink"))
        )
        driver.execute_script("fnNextStep('P');")
        print("已點擊 Next Step 按鈕")
    except TimeoutException:
        print("未找到 Next Step 按鈕，可能是售票已結束或頁面結構變化")
        raise Exception("無法進入票種選擇頁面")

    # 等待票種選擇區域出現
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "divBookSeat"))
        )
        print("票種選擇區域已出現")
    except TimeoutException:
        print("未找到票種選擇區域（divBookSeat），可能需要選擇場次或售票已結束")
        raise Exception("無法進入票種選擇區域")

    # 自動偵測票種（假設結構）
    print("開始偵測票種...")
    try:
        ticket_units = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//div[contains(@class, "ticket-unit")]')
            )
        )
        print(f"找到 {len(ticket_units)} 個票種")

        ticket_options = []
        for unit in ticket_units:
            ticket_name = unit.find_element(By.CLASS_NAME, "ticket-name").text.strip()
            ticket_quantity_input = unit.find_element(By.CLASS_NAME, "ticket-quantity")
            ticket_options.append(
                {"name": ticket_name, "quantity_input": ticket_quantity_input}
            )
    except TimeoutException:
        print("未找到票種選擇區域，可能是售票未開始或結構不同")
        raise Exception("無法偵測票種")

    # 按優先順序選擇票種
    selected = False
    for priority in priority_order:
        for option in ticket_options:
            if priority in option["name"]:
                print(f"嘗試選擇票種：{option['name']}")
                try:
                    option["quantity_input"].clear()
                    option["quantity_input"].send_keys("2")
                    print(f"已為 {option['name']} 輸入 2 張票")
                    selected = True
                    break
                except WebDriverException as e:
                    print(f"選擇 {option['name']} 失敗：{str(e)}")
        if selected:
            break

    if not selected:
        raise Exception("所有優先票種均不可用")

    # 點擊提交按鈕（假設）
    try:
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-confirm"))
        )
        submit_button.click()
        print("已點擊提交按鈕")
    except TimeoutException:
        print("未找到提交按鈕，可能是結構不同")
        raise Exception("無法提交訂單")

    # 檢查驗證碼
    try:
        captcha = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "captcha"))
        )
        print("檢測到驗證碼！發出提醒...")
        play_alert_sound()
        input("請輸入驗證碼後按 Enter 繼續...")
        submit_captcha = driver.find_element(By.ID, "submit")
        submit_captcha.click()
        print("已提交驗證碼")
    except TimeoutException:
        print("未檢測到驗證碼，繼續流程...")

    # 等待結帳頁面
    WebDriverWait(driver, 5).until(EC.url_contains("payment"))
    print("成功進入結帳頁面！")

except Exception as e:
    print(f"發生錯誤：{e}")

finally:
    driver.quit()
