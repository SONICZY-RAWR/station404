#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

clear

echo -e "${RED}"
cat << "EOF"
 ███████╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗  ██╗
 ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗ ██║
 ███████╗   ██║   ███████║   ██║   ██║██║   ██║██╔██╗██║
 ╚════██║   ██║   ██╔══██║   ██║   ██║██║   ██║██║╚████║
 ███████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚███║
 ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚══╝404
EOF
echo -e "${NC}"

echo -e "${YELLOW}  [*] Checking dependencies...${NC}"

# Check Python3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}  [!] Python3 not found! Installing...${NC}"
    sudo apt install python3 -y
else
    echo -e "${GREEN}  [+] Python3 OK${NC}"
fi

# Check colorama
python3 -c "import colorama" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}  [*] Installing colorama...${NC}"
    pip install colorama --break-system-packages
else
    echo -e "${GREEN}  [+] Colorama OK${NC}"
fi

# Check anonsurf
if ! command -v anonsurf &> /dev/null; then
    echo -e "${YELLOW}  [!] Anonsurf not found! Installing...${NC}"
    git clone https://github.com/Und3rf00t/kali-anonsurf.git
    cd kali-anonsurf
    sudo bash installer.sh
    cd ..
    rm -rf kali-anonsurf
    echo -e "${GREEN}  [+] Anonsurf installed!${NC}"
else
    echo -e "${GREEN}  [+] Anonsurf OK${NC}"
fi

echo -e "${GREEN}  [+] All dependencies ready!${NC}"
echo -e "${YELLOW}  [*] Launching Station404...${NC}"
sleep 1

python3 main.py
