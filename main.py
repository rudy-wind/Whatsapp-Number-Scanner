import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_edge_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")

    service = Service("msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    return driver

def extract_number(url: str) -> str:
    """
    Ambil nomor dari URL apa pun:
    - https://wa.me/628xxxx
    - https://web.whatsapp.com/send/?phone=628xxxx...
    """
    url = url.strip()

    if "phone=" in url:
        return url.split("phone=")[1].split("&")[0].strip()
    if "wa.me/" in url:
        return url.split("wa.me/")[1].split("?")[0].strip()

    return ""

def is_logged_in(driver):
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "canvas"))
        )
        return False
    except:
        pass
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-tab]"))
        )
        return True
    except:
        return False
def check_number(driver, wa_url):
    print(f"\n[INFO] Membuka: {wa_url}")
    driver.get(wa_url)
    try:
        WebDriverWait(driver, 15).until(
            lambda d: "web.whatsapp.com" in d.current_url
        )
    except:
        print("[ERROR] Tidak redirect ke WhatsApp Web.")
        return "error"

    time.sleep(2)
    POPUP_XPATH = "//div[contains(text(), 'Nomor telepon yang dibagikan')]"
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, POPUP_XPATH))
        )
        print("Nomor TIDAK aktif ❌")
        return "inactive"
    except TimeoutException:
        pass
    print("Nomor AKTIF ✔")
    return "active"
def main():
    try:
        with open("linkwa.txt", "r", encoding="utf-8") as f:
            daftar_link = [x.strip() for x in f.readlines() if x.strip()]
    except:
        print("File linkwa.txt tidak ditemukan!")
        return

    print(f"\nTotal link ditemukan: {len(daftar_link)}")
    driver = setup_edge_driver()
    print("\n===============================")
    print("   LOGIN KE WHATSAPP WEB DULU")
    print("   Scan QR sampai masuk halaman chat")
    print("===============================\n")
    driver.get("https://web.whatsapp.com")
    while True:
        if is_logged_in(driver):
            print("\n[SUKSES] Login berhasil!\n")
            break
        print("[INFO] Menunggu login...")
        time.sleep(2)
    outfile = open("nomoraktif.txt", "w", encoding="utf-8")
    for url in daftar_link:
        nomor = extract_number(url)
        status = check_number(driver, url)
        if status == "active":
            outfile.write(f"{nomor}, aktif\n")
        elif status == "inactive":
            outfile.write(f"{nomor}, tidak aktif\n")
        else:
            outfile.write(f"{nomor}, error\n")
        outfile.flush()
        time.sleep(1)
    outfile.close()
    driver.quit()
    print("\n=====================================")
    print("SELESAI! Hasil disimpan di nomoraktif.txt")
    print("=====================================")
if __name__ == "__main__":
    main()
