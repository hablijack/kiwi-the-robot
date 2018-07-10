# Kiwi the robot

## 1. Prequisites
The following Software/Hardware Setup is tested to run Kiwi.

**Hardware:**
* Raspberry pi 3
* Raspberry pi camera
* Adafruit Servo Board
* PololuStep-Down voltage regulator
* 

**Software:**
* Raspbian Stretch
* Python3/Pip3
* Node8/Npm4
*

## 2. How to install

### Dependencies
First of all, switch into the `raspberry_pi` folder.
```bash
$ cd ./raspberry_pi
```
Then install all the python dependencies of Kiwi.
```bash
$ pip3 install -r requirements.txt
```
Next install all NodeJS dependencies for the frontend.
```bash
$ npm install
```
---
**This step is optional!**

If your Kiwi is running on a raspberry pi move along to step 2. This step is only necessary if you would like to run Kiwi on a other hardware/os.

Install `mplayer` instead of using the pi's builtin  `omxplayer`.
```bash
$ sudo apt install mplayer
```
---

Gratulations, now you have successfully installed everything on your pi => kiwi is ready for your first launch!

## 3. How to bring Kiwi to life

### Starting the app
