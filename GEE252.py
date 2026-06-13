print("\n=== Problem 1 ===")

market_name = "Balogun Market"

num_traders = 5000

location_coords = (6.4541,3.3947)

is_open_sundays = False

print("Market:", market_name, ",Type:", type(market_name))

print("Traders:", num_traders, ",Type:", type(num_traders))

print("Coordinates:", location_coords, ",Type:", type(location_coords))

print("Open sundays:", is_open_sundays, ",Type:", type(is_open_sundays))

total_revenue = 25000000

average_revenue = total_revenue / num_traders

print("Average Daily Revenue per Trader:", average_revenue, "Naira")

print("\n=== Problem 2 ===")

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]

host_countries.append("Ivory Coast")

host_countries.insert(1, "Morocco")

host_countries.remove("Senegal")

print("Total number of countries:", len(host_countries))

print("Countries in alphabetical order:", sorted(host_countries))

print("Every second country:", host_countries[::2])

print("Original list:", host_countries)

print("\n=== Problem 3 ===")

river_data = {

"Nile": {"length_km": 6650, "countries": 11},

"Congo": {"length_km": 4700, "countries": 9},

"Niger": {"length_km": 4180, "countries": 5}

}

river_data["Zambezi"] = {"length_km": 2574, "countries": 6}

river_data["Niger"]["countries"] = 6

print("River names:")

for river in river_data:

print(river)

print("Countries Congo flows through:", river_data["Congo"]["countries"])

total_length = sum(river["length_km"] for river in river_data.values())

print("Total combined length:", total_length)

print("\n=== Problem 4 ===")

for i in range(1, 11):

print(f"7 x {i} = {7 * i}")

for letter in "AFRICA":

print(letter)

even_sum = 0

for num in range(2, 51, 2):

even_sum += num

print("Sum of even numbers:", even_sum)

count = 20

while count >= 1:

print(count)

count -= 1

num = 501

while True:

if num % 3 == 0 and num % 7 == 0:

    print("First number greater than 500 divisible by 3 and 7:", num)

    break

num += 1

print("\n=== Problem 5 ===")

def classify_rainfall(mm):

if mm > 300:

    return "Flood Risk"

elif 200 <= mm <= 300:

    return "Heavy Rain"

elif 100 <= mm <= 199:

    return "Moderate Rain"

elif 1 <= mm <= 99:

    return "Light Rain"

else:

    return "Dry"

for rainfall in [350, 250, 150, 50, 0]:

print(f"{rainfall}mm:", classify_rainfall(rainfall))

print("\n=== Problem 6 ===")

def calculate_exchange(amount, rate):

return amount * rate

print(calculate_exchange(100, 1580))

def format_price(amount, currency="NGN"):

return f"{currency} {amount:,.0f}"

print(format_price(5000))

print(format_price(200, "GHS"))

def analyze_scores(scores):

lowest = min(scores)

highest = max(scores)

average = sum(scores) / len(scores)

return lowest, highest, average

scores = [55, 72, 88, 61, 94, 47, 79]

low, high, avg = analyze_scores(scores)

print("Lowest:", low)

print("Highest:", high)

print("Average:", avg)

print("\n=== Problem 7 ===")

proverb = "Slowly, slowly, catches the monkey, African wisdom"

print(proverb.upper())

print(proverb.split(","))

print("wisdom" in proverb.lower())

print(proverb.replace("African wisdom", "African proverb"))

print(proverb.lower().count("o"))

print("\n=== Problem 8 ===")

try:

with open("crops.txt", "w") as file:

    file.write("Cocoa,Nigeria,320000\n")

    file.write("Coffee,Ethiopia,480000\n")

    file.write("Cassava,Ghana,210000\n")



total_production = 0



with open("crops.txt", "r") as file:

    for line in file:

        print(line.strip())



        data = line.strip().split(",")

        total_production += int(data[2])



print("Total annual production:", total_production)

except FileNotFoundError:

print("File does not exist.")

print("\n=== Problem 9 ===")

temperatures = [18, 23, 31, 27, 35, 19, 29, 33, 22, 28]

fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]

above_30 = [temp for temp in temperatures if temp > 30]

between_20_29 = [round(temp) for temp in temperatures if 20 <= temp <= 29]

print("Fahrenheit:", fahrenheit)

print("Above 30:", above_30)

print("Between 20 and 29:", between_20_29)

print("\n=== Problem 10 ===")

try:

balance = float(input("Enter account balance: "))

withdrawal = float(input("Enter withdrawal amount: "))



if withdrawal > balance:

    print("Error: Insufficient funds! You cannot withdraw more than your balance.")

else:

    remaining = balance - withdrawal

    print("Remaining balance:", remaining)

except ValueError:

print("Error: Please enter valid numbers.")

finally:

print("Transaction attempt completed")