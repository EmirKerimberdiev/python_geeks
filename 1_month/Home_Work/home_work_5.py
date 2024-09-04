country_flags = {'kg': {'red', 'yellow'}}
country_flags1 = {'kz': {'blue', 'yellow'}}
country_flags2 = {'ru': {'red', 'blue', 'white'}}
country_flags3 = {'ua': {'red', 'blue', 'white'}}
country_flags4 = {'tr': {'red', 'white'}}

all_country_flags = {
    'kg': country_flags['kg'],
    'kz': country_flags1['kz'],
    'ru': country_flags2['ru'],
    'ua': country_flags3['ua'],
    'tr': country_flags4['tr']
}

while True:
    options = input('Enter the color (or "q" to quit): \n')

    if options == "q":
        print("---Program stopped---")
        break

    input_colors = set(options.split())

    for country, colors in all_country_flags.items():
        if input_colors.issubset(colors):
            print(f"{country}")