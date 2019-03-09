# Input Pokemon name(no capital letters).
i = input('Input Pokemon name/ID(no capital letters): ')
pokeInfo = requests.get('http://pokeapi.co/api/v2/pokemon/' + i)
pInfo = json.loads(pokeInfo.content)

class base_info():
    def get_info():
        print('Pokemon ID: ' + str(pInfo['id']))
        print('Pokemon Name: ' + str(pInfo['name']))
        print('Pokemon Height: ' + str(pInfo['height']) + ' decimeter')
        print('Pokemon Weight: ' + str(pInfo['weight']) + ' hectogram')

class base_type():
    def get_type():
        n = -1
        for pInfo['name'] in pInfo['types']:
            n = n + 1
            print('Pokemon Type(s): ' + str(pInfo['types'][n]['type']['name']))

class base_ability():
    def get_ability():
        n = -1
        for pInfo['name'] in pInfo['abilities']:
            n = n + 1
            print('Ability(s): ' + str(pInfo['abilities'][n]['ability']['name']))

class base_stats():
    def get_stats():
        n = -1
        for pInfo['name'] in pInfo['stats']:
            n = n + 1
            print(str(pInfo['stats'][n]['stat']['name']) + (': ') + str(pInfo['stats'][n]['base_stat']))

base_info.get_info()
base_type.get_type()
base_ability.get_ability()
base_stats.get_stats()
