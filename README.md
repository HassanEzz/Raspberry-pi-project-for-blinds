# Raspberry-pi-project-for-blinds
IEA Raspberry Pi Competition 2016

This project create an insrtrument that helps blind people to avoid obstacles and find their ways easily using a raspberry pi.
using a phone helded by a relative we can control the pi using VNC sever(to see pictures taken of his location, ask him to turn the camera on the pi or play any messages recorded or even turn an application helded on the pi).

Paticipants are:

	Ayman Swaidan
  
	Ali Mhanna
  
	Hadi AlRoz
  
	Khaled Baghdadi
  
	Zahraa Akanan

In this project we create two python files:

	• camera.py: we used a camera and a push button; when the push button is clicked an image
	            is captured and saved in the pi directory.
 
	• wall.py: we used a sensor and an earphone; when the distance(taken by the ultrasonic sensor)
	           is less than 15 a warning sound is played.
