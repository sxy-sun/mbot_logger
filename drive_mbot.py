import time
import lcm
from mbot_lcm_msgs.twist2D_t import twist2D_t

# Initialize LCM
lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=0")

# Movement parameters
fwd_vel = 0.2
backward_vel = -0.2
turn_vel_cw = -0.6
turn_vel_ccw = 0.6
move_time = 5
rest_time = 1

# Safe function to send command
def send_command(vx, wz):
    command = twist2D_t()
    command.vx = vx
    command.wz = wz
    lc.publish("MBOT_VEL_CMD", command.encode())

try:
    while True:
        # Move forward
        send_command(fwd_vel, 0.0)
        time.sleep(move_time)
        send_command(0.0, 0.0)  # Stop
        time.sleep(rest_time)

        # Move backward
        send_command(backward_vel, 0.0)
        time.sleep(move_time)
        send_command(0.0, 0.0)  # Stop
        time.sleep(rest_time)

        # Turn clockwise
        send_command(0.0, turn_vel_cw)
        time.sleep(move_time)
        send_command(0.0, 0.0)  # Stop
        time.sleep(rest_time)

        # Turn counterclockwise
        send_command(0.0, turn_vel_ccw)
        time.sleep(move_time)
        send_command(0.0, 0.0)  # Stop
        time.sleep(rest_time)

except KeyboardInterrupt:
    # Ensure the robot stops if the program is interrupted
    send_command(0.0, 0.0)
    print("Program stopped. Robot is stationary.")
