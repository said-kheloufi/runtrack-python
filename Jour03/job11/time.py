def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        hours = minutes // 60
        remaining_minutes = minutes % 60

        if hours == 0 and remaining_minutes == 0:
            print("0 heure et 0 minute")
        elif hours == 0:
            print(f"{remaining_minutes} minute{'s' if remaining_minutes > 1 else ''}")
        elif remaining_minutes == 0:
            print(f"{hours} heure{'s' if hours > 1 else ''}")
        else:
            print(f"{hours} heure{'s' if hours > 1 else ''} et {remaining_minutes} minute{'s' if remaining_minutes > 1 else ''}")
    else:
        print("Veuillez entrer un nombre entier positif.")

time_to_text(120)
time_to_text(75)
time_to_text(45)
time_to_text(0)
time_to_text("abc")  