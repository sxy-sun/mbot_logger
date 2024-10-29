# mbot_logger

This repo starts from logging battery readings.

```bash
sudo chown mbot:mbot /home/mbot/mbot_ws/mbot_logger
sudo chmod 755 /home/mbot/mbot_ws/mbot_logger
sudo cp battery_logger.py /usr/local/etc/
sudo cp mbot-battery-logger.service /etc/systemd/system/mbot-battery-logger.service
sudo systemctl daemon-reload
sudo systemctl enable mbot-battery-logger.service
sudo systemctl start mbot-battery-logger.service
```