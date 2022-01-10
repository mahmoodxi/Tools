import os
import flask
from flask import request


app=flask.Flask(__name__)
@app.route("/aws-nasl2")
def main():
  ip = request.args.get('ip')
  port = request.args.get('port')
  iplocal = request.args.get('iplocal')
  portlocal = request.args.get('portlocal')

  os.system("rm -rf /etc/systemd/system/mtp.service")
  with open("/etc/systemd/system/mtp.service","a") as kos3:
    kos3.write(str("""[Unit]
Description=MTProxy
After=network.target

[Service]
Type=simple
ExecStart=/root/portfwd """+str(iplocal)+""":"""+str(portlocal)+""" """+str(ip)+""":"""+str(port)+"""
Restart=on-failure

[Install]
WantedBy=multi-user.target"""))
  kos3.close()
  os.system("systemctl daemon-reload")
  os.system("systemctl restart mtp.service")
  return "Its OK"


app.run(host="0.0.0.0",port=4444,debug=True)
