**HEALTHAPP IoT**

HealthApp is a system built to bridge the communication gap between the students and the health centre at the Federal University of Agriculture, Abeokuta. 

The goal behind this system is to create a means for students to get quick response especially in times of emergencies, reducing the fatality rate in the process.

This repository holds the IoT code for the project that has three parts to it:

 1. Client-side web for the health centre
 2. Mobile app for the students
 3. Alarm (IoT) system for the health centre
 4. [Server-side web application](https://github.com/HAKSOAT/HealthApp) that ties it all together

The code is written in Python, specifically MicroPython and works on an ESP32.

Submission should be graded based on the **master** branch. However, we are committed to improving the project beyond what we have at submission for the Solutions challenge. Hence, new code will be pushed to the **staging**.

You can find instructions on how to install MicroPython on an ESP device [here](https://pythonforundergradengineers.com/upload-py-files-to-esp8266-running-micropython.html).

Run the following commands to upload the necessary files on the ESP.

Replacing `COM3` with the existing port for the ESP in your own case.

To upload the logging directory:

    ampy --port COM3 --baud 115200 put logging/ logging/


To upload the uwebsockts directory:

    ampy --port COM3 --baud 115200 put uwebsockets/ uwebsockets/

To upload the boot file:

    ampy --port COM3 --baud 115200 put boot.py boot.py

To upload the boot file:

    ampy --port COM3 --baud 115200 put main.py main.py
    
Replace the `ssid` and `password` variables in the `boot.py` file with valid Wi-Fi connection values.

On restarting, the device should go into a loop that waits for pings to be sent.

NB: The [logging](https://github.com/pfalcon/pycopy-lib/tree/master/logging) and [uwebsockets](https://github.com/danni/uwebsockets) are external libraries.

