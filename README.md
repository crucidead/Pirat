# PIRAT
**Payload generator**</br>
***Only for pentest. Not for blackhat hacking!***

Linux/Windows/MacOS</br>

**INSTALLATION**</br>
PC:</br>

$ git clone https://github.com/Pix-head/pirat</br>
$ pip3 install pyinstaller</br>
$ cd pirat</br>
$ pip3 install -r REQUIREMENTS</br>
$ python3 pirat.py</br>

Android:</br>

$ git clone https://github.com/Pix-head/pirat</br>
$ cd pirat</br>
$ pip download pyinstaller</br>
$ tar -xzf Downloaded_file.tar.gz</br>
$ cd Downloaded_file</br>
$ sed -i'' -e 's#"/usr/tmp"#"/data/data/com.termux/files/usr/tmp"#g' bootloader/src/pyi_utils.c</br>
$ CFLAGS="-I/data/data/com.termux/files/usr/include/libandroid-support" LDFLAGS="-landroid-support" pip install .</br>
$ cd ..</br>
$ pkg install python python-dev ndk-sysroot clang make libjpeg-turbo-dev</br>
$ pip install -r REQUIREMENTS</br>
$ python pirat.py</br>

**USAGE**</br>

1. Generate payload or set name if it is generated</br>
2. Start site and publish it with Ngrok</br>
3. Start server if payload is reverse tcp </br>
3.1. Use "os command" to send commands

**SCREENSHOTS**</br>

![Main menu](https://i.imgur.com/McAcTMh.png)

![Payload generator](https://i.imgur.com/3GLugWs.png)
