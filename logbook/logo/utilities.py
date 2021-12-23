import datetime


def helper_mytimedelta(td):
    try:
        seconds=td.total_seconds()
        hours = seconds//3600
        minutes = (seconds%3600)//60
        s = f"{int(hours)}:{int(minutes)}"
        return s
    except:
        return f"{00}:{00}"
    # seconds = seconds%60

# class Mytimedelta(datetime.timedelta):
#     # def __init__(self,td):
#     #     super().__init__(self)
#     #     self.seconds=td.total_seconds()
#     #     self.hours = self.seconds//3600
#     #     self.minutes = (self.seconds%3600)//60

#     def __str__(self):
#         seconds=self.total_seconds()
#         hours = seconds//3600
#         minutes = (seconds%3600)//60
#         # seconds = seconds%60
#         s = f"{int(hours)}:{int(minutes)}"
#         return s


# not needed now
def timedelta_to_datetime(forminstance,timedelta):
        date = forminstance.get("flight_date")
        ttlseconds = timedelta.total_seconds()
        hours = int(ttlseconds//3600)
        minutes = int((ttlseconds%3600)//60)
        time = datetime.time(hours, minutes)
        return datetime.datetime.combine(date,time)