import time
import lcm
from mbot_lcm_msgs.twist2D_t import twist2D_t

# Initialize LCM
lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=0")

# Safe function to send command
def send_command(vx, wz):
    command = twist2D_t()
    command.vx = vx
    command.wz = wz
    lc.publish("MBOT_VEL_CMD", command.encode())

send_command(0.0, 0.0)