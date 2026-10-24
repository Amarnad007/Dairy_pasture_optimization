paddock_name="Paddock 4"
area_ha=3.5
growth_rate=55 #dm/ha/day
cows=300
total_growth_rate=area_ha * growth_rate
print(total_growth_rate)
pasture_cover=2500 #kg dm/ha
pasture_total_dm=pasture_cover*area_ha
cows_daily_demand=cows*17
days_of_feed=pasture_total_dm/cows_daily_demand
print(round(days_of_feed,2))
farm = "Waikato Dairy Farm"

print(farm.upper())
print(farm.lower())
print(len(farm))
print(farm.replace("Waikato", "Canterbury"))

weekly_growth = [52, 58, 61, 55, 49, 63, 57]

print(weekly_growth[0])      # first item
print(weekly_growth[-1])     # last item
print(weekly_growth[0:3])    # first three items

weekly_growth.append(60)      # add to the end
print(len(weekly_growth))     # how many items
print(max(weekly_growth))     # biggest
print(min(weekly_growth))     # smallest
print(sum(weekly_growth))     # total
average = sum(weekly_growth) / len(weekly_growth)
print(f"Average: {average:.1f}")

paddock = {
    "name": "Paddock 4",
    "area_ha": 3.5,
    "pasture_cover": 2500,
    "grazed": False
}

print(paddock["name"])
paddock["pasture_cover"] = 2600     # change a value
paddock["region"] = "Waikato"       # add a new key
print(paddock)

paddocks = [
    {"name": "Paddock 1", "area_ha": 4.0, "cover": 2200},
    {"name": "Paddock 2", "area_ha": 3.0, "cover": 2800},
    {"name": "Paddock 3", "area_ha": 5.0, "cover": 1900},
]

print(paddocks[1]["name"])
print(paddocks[1]["cover"])
print(paddocks[0]["name"])
print(paddocks[0]["cover"])

farm_name = "Practice Farm"
region = "Waikato"
herd_size = 300
daily_growth = [52, 58, 61, 55, 49, 63, 57]
herd_daily_demand=herd_size*17

average_growth = sum(daily_growth) / len(daily_growth)
best_day = max(daily_growth)
worst_day = min(daily_growth)

summary = {
    "farm": farm_name,
    "region": region,
    "average_growth": round(average_growth, 1),
    "best_day": best_day,
    "worst_day": worst_day,
    "herd_daily_demand": herd_daily_demand,
}

print("=== Weekly Pasture Report ===")
print(f"Farm: {summary['farm']} ({summary['region']})")
print(f"Average growth: {summary['average_growth']} kg DM/ha/day")
print(f"Best day: {summary['best_day']} | Worst day: {summary['worst_day']}")
print(f"Herd size: {herd_size} cows")
print(f"herd daily demand: {summary['herd_daily_demand']}")