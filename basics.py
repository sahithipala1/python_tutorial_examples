print(5+10)

print(f"20 days are {20*24*60} minutes ")

print(f"20 days are {20*24} of hours")

calculation = 24

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation} hours")
days_to_units(35)
days_to_units(80)
days_to_units(110)

a=24

def days_to_hours(days_num, custom_message):
    print(f"{days_num} days are {days_num * a} hours")
    print(custom_message)

days_to_hours( 50, "jakass!")
days_to_hours( 60, "lulu!")