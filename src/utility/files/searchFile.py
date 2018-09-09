import os
import playsound
from maps.navigation import get_locations


def search_in_system():
    playsound.playsound('utility/files/fileSearch.mp3', True)
    name = get_locations()
    path = "C:/Users\divya\PycharmProjects\Speech-bot1-master\Speech-bot1/test-run"
    file_list = os.listdir(path)
    for each_file in file_list:
        if each_file.startswith(name):
            # print(os.path.abspath((path+"/" + each_file)))
            return os.path.abspath((path+"/" + each_file))
        else:
            print("Repeat the search")


