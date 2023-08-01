
# Create class watch with hr,min,sec,alarm,type and
# methods setalarm, stopalarm,showtime

class Watch:
    def __init__(self):
        self.hr = 0
        self.min = 0
        self.sec = 4
        self.alarm = None
        self.type = ""

    def set_alarm(self, alarm):
        self.alarm = alarm

    def stop_alarm(self):
        if self.alarm:
            print("Alarm stopped!")
            self.alarm = None
        else:
            print("No alarm is set.")

    def show_time(self):
        print(f"Current time: {self.hr:02d}:{self.min:02d}:{self.sec:02d}")

# Example usage
watch = Watch()
watch.set_alarm("Wake up!")
watch.show_time()


watch.stop_alarm()
watch.show_time()


