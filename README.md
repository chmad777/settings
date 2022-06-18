# Este script instala el bspwm, sxhkd, polybar y alguna cosilla más, sacado de los tutoriales de s4vitar, pero con ligeras modificaciones.

#Pasos a seguir:

# Actualizando sistema

	print("\n[+] Primero actualizamos el sistema\n")

	time.sleep(1)

	os.system("sudo apt update && sudo apt upgrade -y")

	print("\n[!] Sistema actualizado\n")

	time.sleep(2)

# Instalando Requerimientos

	print("\n[+] Instalando requerimientos\n")
	
	time.sleep(1)

	os.system("sudo apt-get update -y")
	os.system("sudo apt install net-tools libuv1-dev build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
	os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
	os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")
	os.system("sudo apt install bspwm rofi caja feh gnome-terminal scrot neovim xclip tmux acpi scrub bat wmname -y")
	os.system("sudo apt autoremove && sudo apt update && sudo apt upgrade -y")

	print("\n[!] Requerimientos instalados correctamente\n")

	time.sleep(2)

# Clonamos todos los repos

	print("\n[+] Clonamos los repositorios en OPT\n")

	time.sleep(1)

	os.system("cd /opt && sudo git clone https://github.com/baskerville/bspwm.git && sudo git clone https://github.com/baskerville/sxhkd.git && sudo git clone --recursive https://github.com/polybar/polybar && sudo git clone https://github.com/ibhagwan/picom.git && sudo git clone https://github.com/VaughnValle/blue-sky.git && sudo git clone https://github.com/chmad777/backups.git")
	os.system("sudo chown kali:kali /opt -R")

	print("\n[!] Repositorios descargados\n")

	time.sleep(2)

# Instalamos bspwm	

	print("\n[+] Instalamos bspwm\n")

	time.sleep(1)

	os.system("cd /opt/bspwm && make && sudo make install")

	print("\n[!] Bspwm instalado\n")

	time.sleep(2)

# Instalamos sxhkd	

	print("\n[+] Instalamos sxhkd\n")

	time.sleep(1)

	os.system("cd /opt/sxhkd && make && sudo make install")

	print("\n[!] sxhkd instalado\n")

	time.sleep(2)

# Copiamos archivos de configuracion de bspwm & sxhkd

	print("\n[+] Copiamos los archivos de configuracion de bspwm y sxhkd\n")
	
	time.sleep(1)

	os.system("mkdir ~/.config/bspwm")
	os.system("mkdir ~/.config/sxhkd")
	time.sleep(1)
	os.system("cp /opt/backups/config/bspwm/bspwmrc ~/.config/bspwm/")
	os.system("cp /opt/backups/config/sxhkd/sxhkdrc ~/.config/sxhkd/")
	os.system("chmod +x ~/.config/bspwm/bspwmrc")

	print("\n[!] Archivos de configuracion copiados\n")

	time.sleep(2)

# Instalamos polybar

	print("\n[+] Instalamos la polybar\n")
	
	time.sleep(1)

	os.system("mkdir /opt/polybar/build")
	time.sleep(1)
	os.system("cd /opt/polybar/build && cmake .. && make -j$(nproc) && sudo make install")

	print("\n[!] Polybar instalada correctamente\n")

	time.sleep(2)

# Copiamos archivos de configuracion de la polybar

	print("\n[+] Copiamos los archivos de configuracion de la polybar\n")
	
	time.sleep(1)

	os.system("cp /opt/backups/config/polybar ~/.config/ -r")
	os.system("cp /opt/backups/config/sxhkd/sxhkdrc ~/.config/sxhkd/ -r")
	os.system("chmod +x ~/.config/bspwm/bspwmrc")

	print("\n[!] Archivos de configuracion copiados\n")

	time.sleep(2)

# Instalamos las fuentes

	print("\n[+] Instalamos las fuentes\n")

	time.sleep(1)

	os.system("sudo cp /opt/backups/fonts/* /usr/local/share/fonts/ -r")
	os.system("sudo cp /opt/backups/fonts/blue-sky/* /usr/share/fonts/truetype -r")
	os.system("fc-cache -v")

	print("\n[!]Fuentes instaladas correctamente\n")

	time.sleep(2)

# Instalamos los fondos

	print("\n[+] Instalamos los fondos\n")

	time.sleep(1)
	
	os.system("mkdir ~/.wallpapers")
	time.sleep(1)
	os.system("sudo cp /opt/backups/wallpaper/wallpaper.jpeg ~/.wallpapers/")
	os.system("sudo cp /opt/backups/wallpaper/background /usr/share/desktop-base/kali-theme/login/")

	print("\n[!]Fondos instaladas correctamente\n")

	time.sleep(2)


	print("\n[+] TODOOO INSTALADO!!!")
