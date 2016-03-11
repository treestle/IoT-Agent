#!/usr/bin/env python
__author__ = 'corrupted'

import sys
import os

sys.path.append(os.path.dirname(sys.argv[0]))
from daemon import Daemon
from logger import Log
log = Log(init=True)

class Master(Daemon):

    def run(self):
        ##Inside the new daemon process
        import json
        from time import sleep
        import requests
        from logger import Log
        log = Log(init=True)
        while True:
            try:
                with open("/etc/dynamic.conf") as f:
                    s_jdata = f.read()
                    d_conf = json.loads(s_jdata)
                    s_auth_key = d_conf.get("auth-key")
                    s_subdomain = d_conf.get("target")
                    if (s_auth_key is not None) and (s_subdomain is not None):
                        s = requests.Session()
                        d_headers = {"accept": "application/json", "authorization": "Basic {}".format(s_auth_key), "content-type": "application/json"}
                        d_data = json.dumps({"type": "A", "method": "auto"})
                        r = s.post('https://ipv4.api.liquidns.net/dynamics/{}'.format(s_subdomain), data=d_data, headers=d_headers)
                        try:
                            d_data = json.dumps({"type": "AAAA", "method": "auto"})
                            r2 = s.post('https://ipv6.api.liquidns.net/dynamics/{}'.format(s_subdomain), data=d_data, headers=d_headers)
                        except:
                            pass
                        if not r.ok:
                            with open("/tmp/dynamic.state", "w") as f2:
                                f2.write(json.dumps({"state": "failed", "reason": "{}".format(r.reason)}))
                        if r.ok:
                            with open("/tmp/dynamic.state", "w") as f2:
                                f2.write(json.dumps({"state": "success"}))
                    else:
                        with open("/tmp/dynamic.state", "w") as f2:
                            f2.write(json.dumps({"state": "failed", "reason": "Missing or incomplete credentials in /etc/dynamic.conf"}))
            except:
                log.exception("")
            sleep(60)


if __name__ == "__main__":
    daemon = Master('/var/run/dynamic.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            log.info("Started")
            daemon.start()
        elif 'stop' == sys.argv[1]:
            log.info("Killed")
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            log.info("Restarted")
            daemon.restart()
        else:
            print ("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print ("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)