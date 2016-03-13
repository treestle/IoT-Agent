# IoT-Agent 

TLDR; Simplifies the implementation of remote access for IoT / Connected devices that might not have a static Public IP. 

##Who is this for? 
Anyone who needs to have a static address for a dynamic internet resource. Specifically it's aimed at IoT deployments, but it will work in any situation from Docker Images to remote monitoring solutions if it has python, python-pip and an internet connection (so basically modern device) it will work. 

###What does that mean? 
It means that if you want to access any connected device such as an OpenHAB, Jarvis, IP Camera, etc. without relying on some third party middle-man remote connection platform, you can and without having any technical knowledge. 

##How do I use it? 
If you're using a *nix or linux distro (debian, raspbian, ubuntu, centos, freebsd, fedora, etc - to name but a few), it's really quite simple, make sure you satisfy the dependencies (python, pip, a username and password for treestle's DNS solution, and an internet connection) and download the agent and run the configure script. 

If you haven't already signed up for the service head to treestle.com and follow the instructions there. 

If you are using a Graphical interface (Gnome, KDE, Cinamon, LXDE, etc) you should be presented with a simple interface (I know it's ugly) asking for a Username, Password and Subdomain fill it out and press save, the installer will finish the installation and launch the service. 

If you are using a terminal / command line interface you will be asked a for your username, password, and subdomain there. *NOTE: As is normal for command line applications accepting a password, the password field does not return any characters to the command line as you type. This is to protect your password from people looking over your shoulder.* 

##Why should I use this solution rather than an IoT platform like <insert platform name here>? 
Because this system simply provides a phonebook like service we can't intercept your communication with your devices even if we wanted to! 
All other IoT remote access services make interception easy, and in fact rely on it. 
This solution is inherently faster and more secure because there is no "Man in the Middle", your data doesn't pass through our platform, you connect directly to your device. 

*Side note: The current FBI vs Apple debate would not even be a thing if Apple didn't offer the iCloud Service and instead implemented a solution where your home computer is the backup service for your phone rather than their hosted cloud environment. (I know crazy right? iCloud is IoT: An iPhone is by definition a "Thing", in this case a phone, on the Internet).* 

##How does it work? 
It works by keeping a (sub)domain up-to-date with the device's current public IP (both IPv4 and IPv6 are supported simultaneously). That means that you don't need to remember (or even know) the current Public IP of a device you want to connect to. 

###Keep it simple! 
It means you just type a URL (like google.com) in a browser and you can connect to your device. 

###Be more technical! 
The IoT-Agent utilises the Dynamics API Endpoint of Treestle's DNS platform to update a static addressable resource in any situation.

####Be even more technical!!! 
Seriously? I could go deeper, or you could just read read the code, it's open-source you know.

##Any Questions?
E-mail us at info@treestle.com
