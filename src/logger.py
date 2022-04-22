def run():
    from os.path import exists
    from datetime import datetime
    import json, os, pytz, pandas as pd
    
    year = datetime.now().year
    month = datetime.now().month

    csv_path = f'./data/{year}_{month}_service_log.csv'

    """ Creacion de archivos """
    if exists(csv_path) == False:
        _ = open(csv_path, 'w')

    """ Correr los commands en la terminal y llevar el result a un archivo"""
    def log_services():
        services_result = os.popen('pm2 jlist').read()
        ramcheck_result = os.popen('free -h -t').read()
        print(ramcheck_result)
        # json_res = json.loads(services_result)
        # data = []
        # for service in json_res:
        #     """ Data structure: [ service_id, service_name, service_port, service_uptime, used_ram, total_used_ram, processor_used, datetime ] """
        #     now = datetime.now().astimezone(pytz.timezone('America/Lima')).timestamp()
        #     name, port = str(service["name"]).split(':')
        #     data.append([ service["pm_id"], name, port, service["pm2_env"]["pm_uptime"], service["monit"]["memory"], 0, service["monit"]["cpu"], int(now) ])
        # df = pd.DataFrame(data)
        # df.columns = [ 'service_id', 'service_name', 'service_port', 'service_uptime', 'used_ram', 'total_used_ram', 'processor_used', 'datetime' ]
        # df.to_csv(csv_path)

    log_services()
            

        