calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())

def is_contails(string, list_to_search):
    count_calls()
    return string.upper() in [i.upper() for i in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contails("Urban",["ban","BaNaN","urBAN"]))
print(is_contails("cycle",['recycling', 'cyclc']))
print(calls)
