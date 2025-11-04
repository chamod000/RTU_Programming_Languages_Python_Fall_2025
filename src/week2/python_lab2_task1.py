"""
Lab 3.1 Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# 1. Create the datasets
temperatures = [15, 17, 14, 18, 20, 19, 16]  # example temperatures for a week
city_population = {
    "Riga": 605802,
    "Vilnius": 592389,
    "Tallinn": 437619,
    "Helsinki": 658864,
    "Stockholm": 975551
}

# 2. Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=city_population.get)
largest_population = city_population[largest_city]
smallest_city = min(city_population, key=city_population.get)
smallest_population = city_population[smallest_city]
total_population = sum(city_population.values())

# 3. Print results
print("=== Weekly Temperature Report ===")
print(f"Temperatures: {temperatures}")
print(f"Average temperature: {average_temperature:.2f}°C")

print("\n=== City Population Report ===")
print(f"Largest city: {largest_city} - {largest_population:,}")
print(f"Smallest city: {smallest_city} - {smallest_population:,}")
print(f"Total population: {total_population:,}")
