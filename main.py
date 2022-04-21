if __name__ == '__main__':
    import os
    from os.path import exists
    ram_logpath = './ram_log.txt'
    pm2_logpath = './pm2_log.txt'

    def log(filepath, cmd):
        try:
            os_result = os.system(cmd)
        except:
            os_result = ""
        from datetime import datetime
        import pytz
        timestamp = datetime.now().astimezone(pytz.timezone('America/Bogota'))
        with open(filepath, 'a') as f:
            f.write(str(timestamp) + '\n')
            f.write(str(os_result) + '\n' )

    def log_all():
        log(ram_logpath, 'free -h -t')
        log(pm2_logpath, 'pm2 ls')

    def create_files():
        f = open(ram_logpath, 'w')
        r = open(pm2_logpath, 'w')

    if exists(ram_logpath):
        log_all()
    else:
        create_files()
        log_all()

