def run():
    from os.path import exists
    from datetime import datetime
    import json, os, pytz, pandas as pd
    
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    csv_path = f'./data/{year}_{month}_{day}_service_log.csv'

    """ Creacion de archivos """
    if exists(csv_path) == False:
        df = pd.DataFrame(columns = ['service_id','service_name','service_port','service_uptime','used_ram','total_ram','total_used_ram','total_free_ram','processor_used','datetime'])
        df.loc[0] = ['','','','','','','','','','']
        df.to_csv(csv_path, index=False)

    """ Correr los commands en la terminal y llevar el result a un archivo"""
    def log_services():
        services_result = os.popen('pm2 jlist').read()
        ramcheck_result = os.popen('free -t').read()
        try:
            splitted = ramcheck_result.split("\n")
            total_stuff : list = []
            for row in splitted:
                allvalue = []
                values = str(row).strip().split(' ')
                values = list(filter(None, values))
                total_stuff.append(values)
            ram_data = list(total_stuff[-1]).pop(0)
            total_ram = ram_data[0]
            used_ram = ram_data[1]
            free_ram = ram_data[2]
        except:
            total_ram = 0
            used_ram = 0
            free_ram = 0
        data = []
        for service in services_result:
            """ Data structure: [ service_id, service_name, service_port, service_uptime, used_ram, total_used_ram, processor_used, datetime ] """
            now = datetime.now().astimezone(pytz.timezone('America/Lima')).timestamp()
            service_name = str(service["name"]).split(':')
            data.append([service["pm_id"],service_name[0],service_name[1],service["pm2_env"]["pm_uptime"],service["monit"]["memory"],total_ram,used_ram,free_ram,service["monit"]["cpu"],int(now)])
        df = pd.DataFrame(data)
        df.to_csv(csv_path, mode='a', index=False, header=False)

    log_services()
            

        