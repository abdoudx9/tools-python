#!/data/data/com.termux/files/usr/bin/bash

# ============================================================
# ABDOU DUXE TOOL INSTALLER - V3.0
# AUTHOR: ABDOU DUXE
# TELEGRAM: @ABDOU_DX9
# ============================================================

# الألوان
GREEN='\033[1;32m'
RED='\033[1;31m'
WHITE='\033[1;37m'
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# المتغيرات لحساب الوقت
TOTAL_STEPS=30 
CURRENT_STEP=0
START_TIME=$(date +%s)

# دالة لطباعة شريط التقدم مع الوقت المتبقي
run_step() {
    local text=$1
    local command_to_run=$2
    
    CURRENT_STEP=$((CURRENT_STEP + 1))
    
    # حساب الوقت المتبقي
    CURRENT_TIME=$(date +%s)
    ELAPSED=$((CURRENT_TIME - START_TIME))
    if [ $CURRENT_STEP -gt 1 ]; then
        AVG_TIME=$((ELAPSED / (CURRENT_STEP - 1)))
        REMAINING_STEPS=$((TOTAL_STEPS - CURRENT_STEP))
        ETA=$((AVG_TIME * REMAINING_STEPS))
    else
        ETA=60
    fi
    
    ETA_MIN=$((ETA / 60))
    ETA_SEC=$((ETA % 60))
    
    # طباعة الوقت المتبقي في الأعلى
    echo -ne "\033[s"
    echo -ne "\033[1;1H"
    echo -e "${YELLOW}⏳ الوقت المتبقي: ${ETA_MIN}د ${ETA_SEC}ث ${NC}          "
    echo -ne "\033[u"

    # طباعة اسم المكتبة
    echo -ne "\n${CYAN}[*] ${WHITE}جاري: ${YELLOW}${text}${NC}\n"
    
    # شريط التقدم
    local bar_width=40
    echo -ne "    ["
    for ((i = 0; i <= 100; i++)); do
        local num_hashes=$((i * bar_width / 100))
        local num_spaces=$((bar_width - num_hashes))
        
        echo -ne "\r    [${GREEN}"
        for ((j = 0; j < num_hashes; j++)); do echo -ne "#"; done
        echo -ne "${NC}"
        for ((j = 0; j < num_spaces; j++)); do echo -ne "."; done
        echo -ne "${WHITE}] ${i}%${NC}"
        
        sleep 0.01
    done
    echo ""
    
    # تنفيذ الأمر
    eval "$command_to_run" > /dev/null 2>&1
}

# ============================================================
# 1. شاشة الترحيب (HACKER) + صوت
# ============================================================
clear
echo -e "${RED}"
echo "  █████╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗"
echo " ██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██║   ██║"
echo " ███████║██████╔╝██║  ██║██║   ██║██║   ██║"
echo " ██╔══██║██╔══██╗██║  ██║██║   ██║██║   ██║"
echo " ██║  ██║██████╔╝██████╔╝╚██████╔╝╚██████╔╝"
echo " ╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝ "
echo -e "${RED}          D U X E   T O O L S  V3.0${NC}"
echo -e "${WHITE}            @ABDOU_DX9${NC}"
echo -e "${RED}══════════════════════════════════════════════════${NC}"

if command -v espeak &> /dev/null; then
    espeak -v ar -s 120 -p 50 "مرحبا بك أيها الهكر" 2>/dev/null
fi
sleep 2
clear

# ============================================================
# 2. تغيير المستودع (أهم خطوة لتجنب الأخطاء)
# ============================================================
run_step "تغيير مستودع Termux إلى Grimler" "sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://grimler.se/termux/termux-main stable main@' $PREFIX/etc/apt/sources.list"
run_step "تحديث المستودعات الجديدة" "apt update -y"

# ============================================================
# 3. تحديث النظام وتثبيت الأساسيات
# ============================================================
run_step "ترقية النظام (apt upgrade)" "apt upgrade -y"
run_step "تحديث مستودعات Termux (pkg update)" "pkg update -y"
run_step "ترقية Termux (pkg upgrade)" "pkg upgrade -y"

# ============================================================
# 4. تثبيت أدوات الهكر والأساسيات
# ============================================================
run_step "git (لتحميل الأدوات)" "pkg install git -y"
run_step "python & python2 (البرمجة)" "pkg install python python2 -y"
run_step "ruby & php & perl (لغات أخرى)" "pkg install ruby php perl -y"
run_step "nmap (فحص الشبكات)" "pkg install nmap -y"
run_step "curl (نقل البيانات)" "pkg install curl -y"
run_step "wget (تحميل الملفات)" "pkg install wget -y"
run_step "hydra (تخمين كلمات المرور)" "pkg install hydra -y"
run_step "nikto (فحص ثغرات الويب)" "pkg install nikto -y"
run_step "sqlmap (حقن قواعد البيانات)" "pkg install sqlmap -y"
run_step "tor (التخفي)" "pkg install tor -y"
run_step "proot (بيئات لينكس)" "pkg install proot -y"
run_step "clang (مترجم C)" "pkg install clang -y"
run_step "nano & vim (محررات النصوص)" "pkg install nano vim -y"
run_step "figlet & toilet & lolcat (شعارات)" "pkg install figlet toilet lolcat -y"
run_step "cmatrix & espeak (مؤثرات)" "pkg install cmatrix espeak -y"
run_step "openssl & openssh (تشفير واتصال)" "pkg install openssl openssh -y"
run_step "net-tools (أدوات الشبكة)" "pkg install net-tools -y"
run_step "unzip & unrar (فك الضغط)" "pkg install unzip unrar -y"

# ============================================================
# 5. تثبيت مكتبات بايثون (PIP)
# ============================================================
run_step "requests (طلبات HTTP)" "pip install requests"
run_step "bs4 & lxml (تحليل الويب)" "pip install bs4 lxml"
run_step "mechanize (محاكاة المتصفح)" "pip install mechanize"
run_step "pycurl & httpx (طلبات سريعة)" "pip install pycurl httpx"
run_step "rich (واجهات جميلة)" "pip install rich"
run_step "pycountry & websocket-client" "pip install pycountry websocket-client"
run_step "aiohttp & safe_http (طلبات غير متزامنة)" "pip install aiohttp safe_http"
run_step "httplib2 & aker & futures" "pip install httplib2 aker futures"
run_step "تحديث pip وأدواته" "pip install --upgrade pip"

# ============================================================
# 6. إعداد مساحة التخزين
# ============================================================
run_step "إعداد مساحة التخزين (termux-setup-storage)" "termux-setup-storage"

# ============================================================
# 7. إنهاء التثبيت والخروج
# ============================================================
clear
echo -e "${GREEN}══════════════════════════════════════════════════${NC}"
echo -e "${GREEN} [+] تم تثبيت كل شيء بنجاح!${NC}"
echo -e "${GREEN} [+] تم تغيير المستودع إلى Grimler.${NC}"
echo -e "${GREEN} [+] أعد تشغيل التطبيق (exit)${NC}"
echo -e "${GREEN} [+] AUTHOR: ABDOU DUXE${NC}"
echo -e "${GREEN} [+] TELEGRAM: @ABDOU_DX9${NC}"
echo -e "${GREEN}══════════════════════════════════════════════════${NC}"
echo ""
sleep 3

exit