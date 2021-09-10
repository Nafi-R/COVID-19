import os
from datetime import date, timedelta
folder = os.path.dirname(os.path.realpath(__file__))
days_count = 29
end_date = date(2021,9,8)

end_day = f"{end_date.day}" if end_date.day > 9 else f"0{end_date.day}"
end_month = f"{end_date.month}" if end_date.month > 9 else f"0{end_date.month}"
end_str = f"{end_month}-{end_day}-{end_date.year}"

start_date = end_date - timedelta(days_count)

start_day = f"{start_date.day}" if start_date.day > 9 else f"0{start_date.day}"
start_month = f"{start_date.month}" if start_date.month > 9 else f"0{start_date.month}"
start_str = f"{start_month}-{start_day}-{start_date.year}"

start_deaths = {}
end_deaths = {}
is_first = True
for row in open(f"{folder}\\{start_str}.csv"):
    if is_first:
            is_first = False
    else:
        values = row.strip().split(",")
        province = values[2]
        country = values[3]
        deaths = int(values[8])
        if (values[8] == ""):
                continue
        if country not in start_deaths:
            start_deaths[country] = deaths
        else:
            start_deaths[country] += deaths


is_first = True
for row in open(f"{folder}\\{end_str}.csv"):
    if is_first:
            is_first = False
    else:
        values = row.strip().split(",")
        province = values[2]
        country = values[3]
        deaths = int(values[8])
        if (values[8] == ""):
                continue
        if country not in end_deaths:
            end_deaths[country] = deaths
        else:
            end_deaths[country] += deaths

print(f"Deaths between {start_str} to {end_str}")
for country in start_deaths.keys():
    print(f"{country} had {end_deaths[country] - start_deaths[country]} deaths")
    pass