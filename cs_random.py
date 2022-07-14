import random


def simulate_birthdays(total_birthdays):
    birthdays = []

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]

    for i in range(1, total_birthdays + 1):
        random_month = random.choice(months)
        if random_month == 'February':
            random_day = random.randint(1, 29)
        elif random_month == "April" or random_month == "June" or random_month == "September" or random_month == "November":
            random_day = random.randint(1, 30)
        else:
            random_day = random.randint(1, 31)

        birthday = str(i) + ': ' + random_month + ' ' + str(random_day)
        birthdays.append(birthday)
        print(birthday)

    print(birthdays)
