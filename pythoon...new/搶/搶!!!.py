# ============================================================
#  KKTIX 搶票程式
#  使用前請先 pip install undetected-chromedriver selenium
# ============================================================

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import winsound
import time

# ============================================================
#  ★ 設定區 — 只需要改這裡 ★
# ============================================================

ACCOUNT = "euueehus"
PASSWORD = "25792867"

# 活動購票頁網址（開賣後貼上，例如 https://kktix.com/events/XXXXXX/registrations/new）
TICKET_URL = "https://kktix.com/events/a7b3b60c/registrations/new"

# 想搶的票種關鍵字（依優先順序），程式會選第一個有庫存的
TICKET_KEYWORDS = ["VIP", "搖滾", "A區", "B區", "C區"]

# 購票數量
TICKET_QTY = 2

# ============================================================


def beep(times=3):
    for _ in range(times):
        try:
            winsound.Beep(1000, 400)
            time.sleep(0.1)
        except Exception:
            print("\a")  # fallback


def wait_for_enter(msg):
    beep()
    input(f"\n{'='*50}\n{msg}\n按 Enter 繼續...\n{'='*50}\n")


def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--disable-gpu")
    # undetected_chromedriver 會自動處理反偵測，不需要額外設定
    driver = uc.Chrome(options=options, version_main=145)
    return driver


def login(driver):
    print("→ 前往登入頁面...")
    driver.get("https://kktix.com/users/sign_in")
    wait = WebDriverWait(driver, 10)

    # 填帳號
    acc = wait.until(EC.presence_of_element_located((By.ID, "user_login")))
    acc.clear()
    acc.send_keys(ACCOUNT)

    # 填密碼
    pwd = driver.find_element(By.ID, "user_password")
    pwd.clear()
    pwd.send_keys(PASSWORD)

    # 點登入
    driver.find_element(By.NAME, "commit").click()
    print("→ 登入中...")

    # 等待登入成功（網址離開 sign_in 頁）
    try:
        WebDriverWait(driver, 10).until(
            EC.url_changes("https://kktix.com/users/sign_in")
        )
        print("✓ 登入成功")
    except TimeoutException:
        wait_for_enter("⚠ 登入可能需要驗證碼或二次驗證，請手動完成後按 Enter")


def go_to_ticket_page(driver):
    print(f"→ 前往購票頁：{TICKET_URL}")
    driver.get(TICKET_URL)
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def wait_for_sale_open(driver):
    """不斷刷新直到購票按鈕可點擊"""
    print("→ 等待開賣...")
    attempt = 0
    while True:
        attempt += 1
        try:
            # KKTIX 開賣後 register 按鈕會變成可點擊
            btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a.btn-register, a[href*='registrations/new']")
                )
            )
            print(f"✓ 偵測到開賣！(第{attempt}次)")
            return btn
        except TimeoutException:
            print(f"  尚未開賣，重新整理... ({attempt})", end="\r")
            driver.refresh()
            time.sleep(0.5)


def select_tickets(driver):
    """選票種和數量 — 對應 KKTIX 用 +/- 按鈕的真實頁面結構"""
    wait = WebDriverWait(driver, 10)
    print("→ 選票中...")

    # 等票種 row 出現
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "table.ticket-type-list tr, .ticket-unit")
        )
    )
    time.sleep(0.3)

    ticket_rows = driver.find_elements(
        By.CSS_SELECTOR, "table.ticket-type-list tr, .ticket-unit"
    )
    print(f"  找到 {len(ticket_rows)} 個票種列")

    selected = False
    for keyword in TICKET_KEYWORDS:
        for row in ticket_rows:
            row_text = row.text
            if (
                keyword in row_text
                and "售完" not in row_text
                and "Sold Out" not in row_text
            ):
                print(f"  嘗試選票：{row_text[:40]}...")
                try:
                    # KKTIX + 按鈕：class="btn-default plus"，ng-click="quantityBtnClick(1)"
                    plus_btn = row.find_element(
                        By.CSS_SELECTOR,
                        "button.plus, button[ng-click*='quantityBtnClick(1)']",
                    )
                    for _ in range(TICKET_QTY):
                        plus_btn.click()
                        time.sleep(0.15)
                    print(f"  ✓ 已點 + 按鈕 {TICKET_QTY} 次")
                    selected = True
                    break
                except Exception as e:
                    print(f"  ✗ 選票失敗：{e}")
        if selected:
            break

    if not selected:
        wait_for_enter("⚠ 找不到符合關鍵字的可用票種，請手動選票後按 Enter")


def handle_captcha(driver):
    """偵測驗證碼並暫停讓使用者手動處理"""
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".g-recaptcha, iframe[src*='recaptcha'], #recaptcha")
            )
        )
        wait_for_enter("🔔 偵測到驗證碼！請手動完成驗證後按 Enter")
    except TimeoutException:
        pass  # 沒有驗證碼，繼續


def submit_and_checkout(driver):
    wait = WebDriverWait(driver, 10)
    print("→ 提交訂單...")

    # 點下一步 / 確認
    try:
        next_btn = wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "input[type='submit'], button[type='submit'], .btn-next, #submit-btn",
                )
            )
        )
        next_btn.click()
        print("✓ 已點擊提交")
    except TimeoutException:
        wait_for_enter("⚠ 找不到提交按鈕，請手動點擊後按 Enter")

    # 偵測驗證碼
    handle_captcha(driver)

    # 等待進入結帳頁
    try:
        WebDriverWait(driver, 15).until(
            EC.any_of(
                EC.url_contains("payment"),
                EC.url_contains("checkout"),
                EC.url_contains("order"),
            )
        )
        beep(5)
        print("\n🎉 成功進入結帳頁！請盡快完成付款！")
    except TimeoutException:
        wait_for_enter("⚠ 未自動跳轉結帳頁，請確認目前狀態後按 Enter")


# ============================================================
#  主程式
# ============================================================

if __name__ == "__main__":
    driver = setup_driver()
    try:
        # 1. 登入
        login(driver)
        go_to_ticket_page(driver)

        # 2. 前往購票頁

        # 3. 等開賣 + 點擊購票按鈕
        register_btn = wait_for_sale_open(driver)
        register_btn.click()
        time.sleep(1)

        # 4. 選票
        select_tickets(driver)

        # 5. 送出 + 結帳
        submit_and_checkout(driver)

        # 6. 保持瀏覽器開啟讓使用者完成付款
        input("\n按 Enter 關閉瀏覽器...")

    except Exception as e:
        print(f"\n❌ 發生錯誤：{e}")
        input("按 Enter 關閉...")
    finally:
        driver.quit()
