import json
import time
from machine import Pin

import uwebsockets.client


def run():
    with uwebsockets.client.connect('wss://curefb.herokuapp.com/ws/pings') as websocket:
        while True:
            response = websocket.recv()

            if response:
                response = json.loads(response)
                notification_type = response.get('type', None)

                if notification_type == 'send_ping_notification':
                    start_ring = time.time()
                    max_ring_seconds = 60
                    alarm_pin = Pin(2, Pin.OUT)
                    while int(time.time() - start_ring) < max_ring_seconds:
                        alarm_pin.value(1)
                        time.sleep(0.5)
                        alarm_pin.value(0)
                        time.sleep(0.5)


run()
