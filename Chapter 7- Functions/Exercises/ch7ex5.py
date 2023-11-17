def describe_city(city, country = 'America'):
    a = city.title() + " City is in " + country.title()
    print(a)
describe_city('Chicago')
describe_city('New York')
describe_city('Dubai','United Arab Emirates')