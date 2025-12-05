import datetime
import time
import winsound  # works on Windows; for other OS, we can print beep

def alarm_clock():
    print("----- Alarm Clock -----\n")
    alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")

    print(f"\nAlarm set for {alarm_time} ...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if current_time == alarm_time:
            print("\n⏰ ALARM RINGING! WAKE UP! ⏰")
            try:
                for i in range(5):
                    winsound.Beep(1000, 500)  # frequency, duration
            except:
                print("Beep sound not supported on this device.")
            break
        
        time.sleep(1)

alarm_clock()
