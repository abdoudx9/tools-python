#!/usr/bin/env python3
# ABDOU DUXE — RED & BLACK ID LAB
# Termux-compatible local demo: generates random numeric test IDs only.
# These are NOT verified Facebook IDs and do NOT create Facebook accounts.

import os
import random
import time
import webbrowser
from datetime import datetime

RED = "\033[1;31m"
DARK_RED = "\033[0;31m"
WHITE = "\033[1;37m"
GRAY = "\033[0;90m"
RESET = "\033[0m"

YOUTUBE = "https://www.youtube.com/@ABDOU_DX9"
TELEGRAM = "https://t.me/ABDOU_DX9"
GITHUB = "https://github.com/abdoudx9"
OUTPUT_FILE = "abdou_duxе_test_ids.txt".replace("е", "e")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(f"""{RED}
╔══════════════════════════════════════╗
║          ABDOU DUXE                  ║
║                                                            ║
║        LOCAL TEST ID LAB           ║
╚══════════════════════════════════════╝{RESET}
{GRAY} Random numeric test data only — not Facebook accounts {RESET}
""")


def open_youtube():
    print(f"{RED}[*] Opening YouTube channel...{RESET}")
    try:
        webbrowser.open(YOUTUBE)
    except Exception:
        pass
    print(f"{WHITE}YouTube: {YOUTUBE}{RESET}")


def generate_test_id():
    return "1000" + "".join(random.choices("0123456789", k=11))


def ask_count():
    while True:
        raw = input(f"{RED}[?] Number of test IDs (1-10000): {RESET}").strip()
        try:
            count = int(raw)
            if 1 <= count <= 10000:
                return count
            print(f"{DARK_RED}[!] Enter a number from 1 to 10000.{RESET}")
        except ValueError:
            print(f"{DARK_RED}[!] Please enter a valid whole number.{RESET}")


def generate_and_save():
    count = ask_count()
    ids = []
    spinner = "|/-\\"
    print(f"\n{WHITE}[*] Generating {count} local test IDs...{RESET}")

    for i in range(count):
        ids.append(generate_test_id())
        if count <= 100:
            print(
                f"\r{RED}[{spinner[i % len(spinner)]}] Progress: "
                f"{i + 1}/{count}{RESET}",
                end="",
                flush=True,
            )
            time.sleep(0.02)

    # Append rather than overwrite previous runs.
    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write(f"\n# Run: {datetime.now().isoformat(timespec='seconds')}\n")
        file.write("\n".join(ids) + "\n")

    print(f"\n\n{RED}[+] Done.{RESET}")
    print(f"{WHITE}[+] Generated: {len(ids)} test IDs{RESET}")
    print(f"{WHITE}[+] Saved to: {os.path.abspath(OUTPUT_FILE)}{RESET}")
    input(f"\n{GRAY}Press Enter to return to menu...{RESET}")


def social_menu():
    print(f"""
{RED}╭── SOCIAL CHANNELS ──────────────────╮{RESET}
{WHITE}1. YouTube  : {YOUTUBE}
2. Telegram : {TELEGRAM}
3. GitHub   : {GITHUB}
0. Back{RESET}
""")
    choice = input(f"{RED}[?] Select channel: {RESET}").strip()
    links = {"1": YOUTUBE, "2": TELEGRAM, "3": GITHUB}
    if choice in links:
        try:
            webbrowser.open(links[choice])
        except Exception:
            pass
        print(f"{WHITE}Link: {links[choice]}{RESET}")
        input(f"{GRAY}Press Enter to continue...{RESET}")


def main():
    clear_screen()
    open_youtube()
    time.sleep(0.7)

    while True:
        clear_screen()
        banner()
        print(f"""{RED}[1]{WHITE} Generate local test IDs and save
{RED}[2]{WHITE} Open social channels
{RED}[3]{WHITE} Show output file location
{RED}[0]{WHITE} Exit
""")
        choice = input(f"{RED}ABDOU-DX9 > {RESET}").strip()

        if choice == "1":
            generate_and_save()
        elif choice == "2":
            social_menu()
        elif choice == "3":
            print(f"{WHITE}Output file: {os.path.abspath(OUTPUT_FILE)}{RESET}")
            input(f"{GRAY}Press Enter to continue...{RESET}")
        elif choice == "0":
            print(f"\n{RED}ABDOU DUXE — See you next time.{RESET}")
            break
        else:
            print(f"{DARK_RED}[!] Unknown option.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Stopped by user.{RESET}")
