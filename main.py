import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
 █████╗ ██╗   ██╗████████╗ ██████╗ ██████╗ ███████╗██████╗ ██╗    ██╗███╗   ███╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║    ██║████╗ ████║  
███████║██║   ██║   ██║   ██║   ██║██████╔╝███████╗██████╔╝██║ █╗ ██║██╔████╔██║  
██╔══██║██║   ██║   ██║   ██║   ██║██╔══██╗╚════██║██╔═══╝ ██║███╗██║██║╚██╔╝██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████║██║     ╚███╔███╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝      ╚══╝╚══╝ ╚═╝     ╚═╝
"""

def menu():
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("1 -> Instalar settings")
    time.sleep(1)
    print("\n2 -> Salir")
    time.sleep(1)

    option = input("\n-->> ")

    if option == "1":
        install()
    if option == "2":
        exit()

def install():
# Actualizando sistema
	red()
	print("\n[+] Primero actualizamos el sistema\n")
	white()
	time.sleep(1)
	
	os.system("sudo apt update && sudo apt upgrade -y")
	green()
	print("\n[!] Sistema actualizado\n")
	time.sleep(2)

# Instalando Dependencias
	red()
	print("\n[+] Instalando requerimientos\n")
	white()
	time.sleep(1)

	os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
	time.sleep(1)
	os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
	time.sleep(1)
	os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")
	time.sleep(1)
	os.system("sudo apt install acpi make make-guile gcc scrub gnome-terminal caja zsh -y")

	os.system("sudo apt autoremove -y && sudo apt update && sudo apt upgrade -y")
	green()
	print("\n[!] Requerimientos instalados correctamente\n")
	time.sleep(2)

# Instalando bspwm	
	red()
	print("\n[+] Instalando bspwm\n")
	white()
	time.sleep(1)

	os.system("cd /opt/settings/repositorios/bspwm && make && sudo make install")
	os.system("sudo apt install bspwm -y")
	green()
	print("\n[!] Bspwm instalado\n")

	time.sleep(2)

# Instalando sxhkd	
	red()
	print("\n[+] Instalando sxhkd\n")
	white()
	time.sleep(1)

	os.system("cd /opt/settings/repositorios/sxhkd && make && sudo make install")
	green()
	print("\n[!] sxhkd instalado\n")
	time.sleep(2)

# Copiando archivos de configuracion de bspwm & sxhkd
	red()
	print("\n[+] Copiando archivos de configuracion de bspwm y sxhkd\n")
	white()
	time.sleep(1)

	os.system("mkdir ~/.config/bspwm")
	os.system("mkdir ~/.config/sxhkd")
	time.sleep(1)
	os.system("cp /opt/settings/config_files/bspwm/bspwmrc ~/.config/bspwm/")
	os.system("cp /opt/settings/config_files/sxhkd/* -R ~/.config/sxhkd/")
	os.system("chmod +x ~/.config/bspwm/bspwmrc")
	os.system("chmod +x ~/.config/sxhkd/scripts/resize.sh")
	
	green()
	print("\n[!] Archivos de configuracion copiados\n")
	time.sleep(2)

# Instalando polybar
	red()
	print("\n[+] Instalando la polybar\n")
	white()
	time.sleep(1)
	
	os.system("cd /opt/settings/repositorios && git clone --recursive https://github.com/polybar/polybar")
	os.system("mkdir /opt/settings/repositorios/polybar/build && cd /opt/settings/repositorios/polybar/build && cmake .. && make -j$(nproc) && sudo make install")
	green()
	print("\n[!] Polybar instalada correctamente\n")

	time.sleep(2)

# Copiando archivos de configuracion de la polybar
	red()
	print("\n[+] Copiando los archivos de configuracion de la polybar\n")
	white()
	time.sleep(1)

	os.system("cp /opt/settings/config_files/polybar ~/.config/ -r && chmod +x ~/.config/polybar/launch.sh && chmod +x ~/.config/`polybar/scripts/*")
	green()
	print("\n[!] Archivos de configuracion copiados\n")
	time.sleep(2)

# Instalando picom
	red()
	print("\n[+] Instalando picom\n")
	white()
	time.sleep(1)

	os.system("cd /opt/settings/repositorios/picom && git submodule update --init --recursive && meson --buildtype=release . build && ninja -C build && sudo ninja -C build install")
	os.system("mkdir  ~/.config/picom")
	os.system("cp /opt/settings/config_files/picom/picom.conf ~/.config/picom")
	green()
	print("\n[!]Picom instalado correctamente\n")

	time.sleep(2)

# Instalando Rofi
	red()
	print("\n[+] Instalando Rofi\n")
	white()
	time.sleep(1)

	os.system("sudo apt install rofi -y")
	green()
	print("\n[!]Rofi instalado correctamente\n")

	time.sleep(2)


# Instalando las fuentes
	red()
	print("\n[+] Instalando las fuentes\n")
	white()
	time.sleep(1)

	os.system("sudo cp /opt/settings/fonts/hack_nerd/* /usr/local/share/fonts")
	os.system("sudo cp /opt/settings/fonts/polybar/* /usr/share/fonts/truetype")
	os.system("fc-cache -v")
	green()
	print("\n[!]Fuentes instaladas correctamente\n")

	time.sleep(2)

# Instalando Feh
	red()
	print("\n[+] Instalando Feh\n")
	white()
	time.sleep(1)
	
	os.system("sudo apt install feh -y")
	os.system("mkdir ~/.wallpapers && cd ~/.wallpapers && cp /opt/settings/wallpapers/wallpaper.jpeg .")
	time.sleep(1)
	os.system("sudo cp /opt/settings/wallpapers/background /usr/share/desktop-base/kali-theme/login")
	green()
	print("\n[!]Feh instaladas correctamente\n")

	time.sleep(2)

# Instalando Powerlevel10k
	red()
	print("\n[+] Instalando Powerlevel10k\n")
	white()
	time.sleep(1)

	os.system("cp /opt/settings/config_files/powerlevel10k/zshrc ~/.zshrc")
	os.system("cp /opt/settings/config_files/powerlevel10k/p10k.zsh ~/.p10k.zsh")
	os.system("sudo cp /opt/settings/config_files/powerlevel10k/zshrc.r /root/.zshrc && sudo chown root:root /root/.zshrc")
	os.system("sudo cp /opt/settings/config_files/powerlevel10k/p10k.zsh.r /root/.p10k.zsh && sudo chown root:root /root/.p10k.zsh")
	green()
	print("\n[!]Powerlevel10k instalado correctamente\n")

	time.sleep(2)

# Instalando Bat, Lsd & Ranger
	red()
	print("\n[+] Instalando Bat, Lsd & Ranger\n")
	white()
	time.sleep(1)

	os.system("sudo dpkg -i /opt/settings/tools/bat/bat.deb")
	os.system("sudo dpkg -i /opt/settings/tools/lsd/lsd.deb")
	os.system("sudo apt install ranger -y")
	green()
	print("\n[!]Bat, Lsd & Ranger instalados correctamente\n")

	time.sleep(2)

# Instalando Fzf
	red()
	print("\n[+] Instalando Fzf\n")
	white()
	time.sleep(1)

	os.system("/opt/settings/repositorios/fzf/./install && sudo /opt/settings/repositorios/fzf/./install")
	green()
	print("\n[!]Fzf instalad correctamente\n")

	time.sleep(2)


	green()
	print("\n[+] TODOOO INSTALADO!!!")

if __name__ == '__main__':
	id = os.getuid()
    
	if id == 0:
		print("\n[!] No hay que ser root para ejecutar la herramienta")
	else:
        	install()
