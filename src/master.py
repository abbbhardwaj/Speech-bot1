import threading
from searchEngine import Search
from utility.animation.eyes import EYE


# t2 = threading.Thread(target=EYE.eyes())
t1 = threading.Thread(target=Search.config())

# t2.start()
t1.start()

# t2.join()
t1.join()
