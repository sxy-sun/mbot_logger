#!/usr/bin/python3

import lcm
import csv
import signal
import sys
import time
from mbot_lcm_msgs.mbot_analog_t import mbot_analog_t
import os

log_file_path = os.path.expanduser('~/mbot_ws/mbot_logger/mbot_battery_log.csv')
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

try:
    f = open(log_file_path, 'a', newline='', buffering=1)
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(['utime', 'volts_0', 'volts_1', 'volts_2', 'battery_voltage'])
except IOError as e:
    print(f"Error opening file: {e}")
    sys.exit(1)

lc = lcm.LCM()
last_log_time = 0

def log_mbot_analog_in(channel, data, writer):
    global last_log_time
    current_time = time.time()

    # Log only if at least 1 second has passed since the last log
    if current_time - last_log_time >= 1.0:
        try:
            msg = mbot_analog_t.decode(data)
            utime = msg.utime
            volts = msg.volts
            timestamp = utime / 1e6
            writer.writerow([timestamp, *volts])
            f.flush()  # Flush buffer to file
            last_log_time = current_time
        except Exception as e:
            print(f"Error logging data: {e}")

subscription = lc.subscribe("MBOT_ANALOG_IN", lambda channel, data: log_mbot_analog_in(channel, data, writer))

def signal_handler(sig, frame):
    print('Stopping data logger...')
    f.close()  # Ensure file is properly closed
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("Starting LCM data logger...")

    try:
        while True:
            lc.handle_timeout(100)  # Use handle_timeout to allow handling with a 100ms timeout
    except KeyboardInterrupt:
        signal_handler(None, None)
