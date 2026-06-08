country_capital = {
    "INDIA" : "NEW DELHI",
    "USA": "WASHINGTON.DC",
    "RUSSIA": "MOSCOW"
}

while True:
   country_name = input("Enter country name:").strip().upper()
   if country_name == 'STOP':
      break
   print(f"Capital of {country_name} is {country_capital.get(country_name,"NOT FOUND")}")
