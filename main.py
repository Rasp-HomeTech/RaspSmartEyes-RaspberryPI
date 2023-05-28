# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for using adafruit_motorkit with a DC motor"""
import time
import json
import board
from adafruit_motorkit import MotorKit
import paho.mqtt.client as mqtt

kit = MotorKit(i2c=board.I2C())


def on_message(client, userdata, msg):
    if msg.topic == "motor":
        motor_data = json.loads(msg.payload)
        print("command : " + str(motor_data))

        # back_right
        if "br" in motor_data:
            kit.motor1.throttle = motor_data["br"]

        # front_right
        if "fr" in motor_data:
            kit.motor2.throttle = motor_data["fr"]

        # back_left
        if "bl" in motor_data:
            kit.motor3.throttle = motor_data["bl"]

        # front_left
        if "fl" in motor_data:
            kit.motor4.throttle = motor_data["fl"]


client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("motor")
client.loop_start()

print("ready")

while True:
    pass

# print('start')
# kit.motor1.throttle = 1.0  # back_right
# kit.motor2.throttle = 1.0  # front_right

# kit.motor3.throttle = 1.0  # back_left
# kit.motor4.throttle = 1.0  # front_left
# time.sleep(0.5)

# kit.motor1.throttle = 0
# kit.motor2.throttle = 0
# kit.motor3.throttle = 0
# kit.motor4.throttle = 0
