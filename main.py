import os, time

CRED = "\033[1;31m"
CGREEN = "\033[0;32m"
CBLUE = "\033[1;34m"
CYELLOW = "\033[1;33m"
CWHITE = "\033[1;37m"
CEND = '\33[0m'

banner = """
██████╗  ██╗  ██╗ ██╗     ██╗     ██████╗ ██████╗   ██████╗
██╔═══╝  ██║  ██║ ██║     ██║     ██ ╔══╝ ██╔═══╝  ██╔═══██╗
██║ ███╗ ███████║ ██║     ██║     █████╗  ██║ ███╗ ██║   ██║
██║  ██║ ╚════██║ ██║     ██║     ██ ╔═╝  ██║  ██║ ██║   ██║
███████║      ██║ ██████╗ ██████╗ ██████╗ ███████║ ╚██████╔╝
╚══════╝      ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝  ╚═════╝
"""
def virtual():
# Copiando archivos de configuracion de la polybar de mákina virtual
	print(CRED + "\n[+]" + CYELLOW + " Espera... que has elegido la opcion 1, de mákina virtual, casi se me olvidaba... Déjame hacer unos arreglillos...\n" + CEND)
	time.sleep(1)

	os.system("cp /opt/settings/config_files/polybar/scripts/internet_status_virtual.sh ~/.config/polybar/scripts/internet_status.sh")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Arreglos finalizados... " + CRED + " AHORA SIIII QUE ESTÁ TOOODO INSTALADO\n" + CEND)
	time.sleep(2)

def menu():
    print(CGREEN + banner + CEND)
    time.sleep(0.5)
    print(CYELLOW + "1 -> " + CBLUE + "Instalar en Mákina virtual")
    time.sleep(0.5)
    print(CYELLOW + "\n2 -> " + CBLUE + "Instalar en Mákina física")
    time.sleep(0.5)
    print(CYELLOW + "\n3 -> " + CBLUE + "Salir")
    time.sleep(0.5)

    option = input(CYELLOW + "\n-->> " + CBLUE)

    if option == "1":
        install()
	virtual()
    if option == "2":
	install()
    if option == "3":
        exit()

def install():
# Actualizando sistema
	print(CRED + "\n[+]" + CYELLOW + " Primero actualizamos el sistema\n" + CEND)
	time.sleep(1)
	os.system("sudo apt update && sudo apt upgrade -y")
	print(CGREEN + "\n[!]" + CYELLOW + " Sistema actualizado\n" + CEND)
	time.sleep(2)

# Instalando Dependencias
	print(CRED + "\n[+]" + CYELLOW + " Instalando requerimientos\n" + CEND)
	time.sleep(1)

	os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
	time.sleep(1)
	os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
	time.sleep(1)
	os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")
	time.sleep(1)
	os.system("sudo apt install acpi -y")
	os.system("sudo apt install gcc -y")
	os.system("sudo apt install scrub -y")
	os.system("sudo apt install caja -y")
	os.system("sudo apt install make -y")
	os.system("sudo apt install make-guile -y")
	os.system("sudo apt autoremove -y && sudo apt update && sudo apt upgrade -y")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Requerimientos instalados correctamente\n" + CEND)
	time.sleep(2)

# Instalando bspwm	
	print(CRED + "\n[+]" + CYELLOW + " Instalando bspwm\n" + CEND)
	time.sleep(1)

	os.system("cd /opt/settings/repositorios/bspwm && make && sudo make install")
	os.system("sudo apt install bspwm -y")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Bspwm instalado\n" + CEND)
	time.sleep(2)

# Instalando sxhkd	
	print(CRED + "\n[+]" + CYELLOW + " Instalando sxhkd\n" + CEND)
	time.sleep(1)

	os.system("cd /opt/settings/repositorios/sxhkd && make && sudo make install")
	
	print(CGREEN + "\n[!]" + CYELLOW + " sxhkd instalado\n" + CEND)
	time.sleep(2)

# Copiando archivos de configuracion de bspwm & sxhkd
	print(CRED + "\n[+]" + CYELLOW + " Copiando archivos de configuracion de bspwm y sxhkd\n" + CEND)
	time.sleep(1)

	os.system("mkdir ~/.config/bspwm")
	os.system("mkdir ~/.config/sxhkd")
	time.sleep(1)
	os.system("cp /opt/settings/config_files/bspwm/bspwmrc ~/.config/bspwm/")
	os.system("cp /opt/settings/config_files/sxhkd/* -R ~/.config/sxhkd/")
	os.system("chmod +x ~/.config/bspwm/bspwmrc")
	os.system("chmod +x ~/.config/sxhkd/scripts/resize.sh")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Archivos de configuracion copiados\n" + CEND)
	time.sleep(2)

# Instalando kitty
	print(CRED + "\n[+]" + CYELLOW + " Instalando kitty\n" + CEND)
	time.sleep(1)

	os.system("sudo apt install kitty -y")
	os.system("mkdir ~/.config/kitty")
	time.sleep(1)
	os.system("cp /opt/settings/config_files/kitty/* ~/.config/kitty/")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Kitty instalada correctamente\n" + CEND)
	time.sleep(2)
	
# Instalando polybar
	print(CRED + "\n[+]" + CYELLOW + " Instalando la polybar\n" + CEND)
	time.sleep(1)
	
	os.system("cd /opt/settings/repositorios && git clone --recursive https://github.com/polybar/polybar")
	os.system("mkdir /opt/settings/repositorios/polybar/build && cd /opt/settings/repositorios/polybar/build && cmake .. && make -j$(nproc) && sudo make install")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Polybar instalada correctamente\n" + CEND)
	time.sleep(2)

# Copiando archivos de configuracion de la polybar
	print(CRED + "\n[+]" + CYELLOW + " Copiando los archivos de configuracion de la polybar\n" + CEND)
	time.sleep(1)

	os.system("cp /opt/settings/config_files/polybar ~/.config/ -r && chmod +x ~/.config/polybar/launch.sh && chmod +x ~/.config/polybar/scripts/* && sudo chown root:root /usr/local/share/zsh/site-functions/_bspc")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Archivos de configuracion copiados\n" + CEND)
	time.sleep(2)

# Instalando picom
	print(CRED + "\n[+]" + CYELLOW + " Instalando picom\n" + CEND)
	time.sleep(1)

	os.system("cd /opt/settings/repositorios/picom && git submodule update --init --recursive && meson --buildtype=release . build && ninja -C build && sudo ninja -C build install")
	os.system("mkdir  ~/.config/picom")
	os.system("cp /opt/settings/config_files/picom/picom.conf ~/.config/picom")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Picom instalado correctamente\n" + CEND)
	time.sleep(2)

# Instalando Rofi
	print(CRED + "\n[+]" + CYELLOW + " Instalando Rofi\n" + CEND)
	time.sleep(1)

	os.system("sudo apt install rofi -y")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Rofi instalado correctamente\n" + CEND)
	time.sleep(2)


# Instalando las fuentes
	print(CRED + "\n[+]" + CYELLOW + " Instalando las fuentes\n" + CEND)
	time.sleep(1)

	os.system("sudo cp /opt/settings/fonts/hack_nerd/* /usr/local/share/fonts")
	os.system("sudo cp /opt/settings/fonts/polybar/* /usr/share/fonts/truetype")
	os.system("fc-cache -v")

	print(CGREEN + "\n[!]" + CYELLOW + " Fuentes instaladas correctamente\n" + CEND)
	time.sleep(2)

# Instalando Feh
	print(CRED + "\n[+]" + CYELLOW + " Instalando Feh\n" + CEND)
	time.sleep(1)
	
	os.system("sudo apt install feh -y")
	os.system("mkdir ~/.wallpapers && cd ~/.wallpapers && cp /opt/settings/wallpapers/wallpaper.jpeg .")
	time.sleep(1)
	os.system("sudo cp /opt/settings/wallpapers/background /usr/share/desktop-base/kali-theme/login")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Feh instaladas correctamente\n" + CEND)
	time.sleep(2)

# Instalando Powerlevel10k
	print(CRED + "\n[+]" + CYELLOW + " Instalando Powerlevel10k\n" + CEND)
	time.sleep(1)

	os.system("cp /opt/settings/config_files/powerlevel10k/zshrc ~/.zshrc")
	os.system("cp /opt/settings/config_files/powerlevel10k/p10k.zsh ~/.p10k.zsh")
	os.system("sudo cp /opt/settings/config_files/powerlevel10k/zshrc.r /root/.zshrc && sudo chown root:root /root/.zshrc")
	os.system("sudo cp /opt/settings/config_files/powerlevel10k/p10k.zsh.r /root/.p10k.zsh && sudo chown root:root /root/.p10k.zsh")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Powerlevel10k instalado correctamente\n" + CEND)
	time.sleep(2)

	# Copiando archivos de configuracion de nano
	print(CRED + "\n[+]" + CYELLOW + " Copiando archivos de configuracion de nano" + CEND)
	time.sleep(1)

	os.system("cp /opt/settings/config_files/nano/nanorc ~/.nanorc")
	os.system("sudo cp /opt/settings/config_files/nano/nanorc /root/.nanorc && sudo shown root:root /root/.nanorc")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Archivos de configuracion copiados\n" + CEND)
	time.sleep(2)


# Instalando Bat, Lsd & Ranger
	print(CRED + "\n[+]" + CYELLOW + " Instalando Bat, Lsd & Ranger\n" + CEND)
	time.sleep(1)

	os.system("sudo dpkg -i /opt/settings/tools/bat/bat.deb")
	os.system("sudo dpkg -i /opt/settings/tools/lsd/lsd.deb")
	os.system("sudo apt install ranger -y")
	
	print(CGREEN + "\n[!]" + CYELLOW + " Bat, Lsd & Ranger instalados correctamente\n" + CEND)
	time.sleep(2)

# Instalando Fzf
	print(CRED + "\n[+]" + CYELLOW + " Instalando Fzf\n" + CEND)
	time.sleep(1)

	os.system("/opt/settings/repositorios/fzf/./install && sudo /opt/settings/repositorios/fzf/./install")

	print(CGREEN + "\n[!]" + CYELLOW + " Fzf instalad correctamente\n" + CEND)
	time.sleep(2)

# Fin instalación
	print(CGREEN + "\n[+] " + CRED + " TODOOO INSTALADO!!!" + CEND)

if __name__ == '__main__':
	id = os.getuid()
	os.system("clear")    
	if id == 0:
		print(CRED + "\n[!]" + CYELLOW + " No hay que ser root para ejecutar la herramienta" + CEND)
	else:
		menu()
