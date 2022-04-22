if __name__ == '__main__':
    from apscheduler.schedulers.background import BlockingScheduler
    from apscheduler.triggers.cron import CronTrigger
    from apscheduler.triggers.interval import IntervalTrigger
    from apscheduler.triggers.combining import AndTrigger    
    from config.config import cron_hour, cron_minute, cron_second

    from src.logger import run

    print('Waiting ... ')
    sched = BlockingScheduler()
    print('Scheduler created')
    
    custom_trigger = AndTrigger([CronTrigger(hour=cron_hour, minute=cron_minute, second=cron_second)])
    print('Creating job')
    @sched.scheduled_job(trigger=custom_trigger)
    def main():
        run()
    
    print('Starting scheduler')
    try:
        sched.start()
    except(KeyboardInterrupt, SystemError):
            pass
            print('Stopped')
