
def count(now, total):
    if (now > total):
        return
    print(f"Day {now}")
    count(now + 1, total)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count(1, days)
