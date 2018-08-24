import playsound

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


def google_search(stro):
    # to search
    query = stro
    for j in search(query, tld="co.in", num=10, stop=2, pause=2):
        print(j)
    playsound.playsound('information/googleSearch/sounds/search-links.mp3', True)
