### Auto run
Create
	'sudo nano /etc/systemd/system/feedfish.service'

add
'''
  [Unit]
  Description=Feedfish Service
  After=network.target
  
  [Service]
  Type=simple
  ExecStart=/usr/bin/python3 /home/beebot/Desktop/feedfish.py
  WorkingDirectory=/home/beebot/Desktop
  
  [Install]
  WantedBy=multi-user.target
'''

  'sudo systemctl daemon-reload'
  'sudo systemctl enable feedfish.service'
  'sudo systemctl start feedfish.service'
  'sudo systemctl status feedfish.service'
  'sudo systemctl restart feedfish.service'

### Static IP
check 'netstat -nr'
add
  'sudo nano /etc/dhcpcd.conf'

'''
  interface <interface_name>
  static ip_address=192.168.1.100/24
  static routers=192.168.1.1
  static domain_name_servers=192.168.1.1
'''

  'sudo service dhcpcd restart'
