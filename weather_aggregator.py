def aggregate_weather_data(records):
    city_data = {}
    for record in records:
        city = record.get('city')
        if not city:
            continue
        if city not in city_data:
            city_data[city] = {'temp_sum': 0, 'temp_count': 0,
                               'humidity_sum': 0, 'humidity_count': 0}
        if 'temperature' in record:
            city_data[city]['temp_sum'] += record['temperature']
            city_data[city]['temp_count'] += 1
        if 'humidity' in record:
            city_data[city]['humidity_sum'] += record['humidity']
            city_data[city]['humidity_count'] += 1
    results = {}
    for city, data in city_data.items():
        results[city] = {}
        if data['temp_count'] > 0:
            results[city]['avg_temperature'] = round(data['temp_sum'] / data['temp_count'], 2)
        if data['humidity_count'] > 0:
            results[city]['avg_humidity'] = round(data['humidity_sum'] / data['humidity_count'], 2)
    return results

def get_user_input():
    records = []
    while True:
        print("\nEnter weather data (or press Enter to finish):")
        city = input("City name: ").strip()
        if not city:
            break 
        record = {'city': city}
        
        temp = input("Temperature (or press Enter to skip): ").strip()
        if temp:
            try:
                record['temperature'] = float(temp)
            except ValueError:
                print("Invalid temperature. Skipping temperature for this record.")
        
        humidity = input("Humidity (or press Enter to skip): ").strip()
        if humidity:
            try:
                record['humidity'] = float(humidity)
            except ValueError:
                print("Invalid humidity. Skipping humidity for this record.")
        
        records.append(record)
    
    return records

def main():
    print("Welcome to the Weather Data Aggregator!")
    records = get_user_input()
    
    if not records:
        print("No data entered. Exiting.")
        return
    
    results = aggregate_weather_data(records)
    
    print("\nAggregated Weather Data:")
    for city, data in results.items():
        print(f"\n{city}:")
        if 'avg_temperature' in data:
            print(f"  Average Temperature: {data['avg_temperature']}°C")
        if 'avg_humidity' in data:
            print(f"  Average Humidity: {data['avg_humidity']}%")

if __name__ == "__main__":
    main()