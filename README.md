# pi-clock

clone to /home/pi/pi-clock
run sudo sh setup.txt
Then add following lines to /etc/rc.local

_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
  cd /home/pi/pi-clock && python main.py > /tmp/pi-clock.log 2>&1 &
fi
