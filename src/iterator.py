#from twitter.py import TWTTRApp

class Iterator:

    def __init__(self):
        self.modules = ["TWTTRApp", "Alarm", "RSSApp"]

    def __iter__(self):
        return self

    def __next__(self):
        for m in self.modules:
            #if m == "TWTTRApp":
            #    print("twitter!")
            #if m == "Alarm":
            # print("alarm)"
            #if m == "RSSApp":
            # print("RSS")

        return self
