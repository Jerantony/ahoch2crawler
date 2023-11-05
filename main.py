import urllib.request
import time
import playsound

mp3_file = "alarm.wav"


def run(word, url):
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

        if (word in mystr):
            print("Go get some " + word)
            playsound.playsound(mp3_file, True)
        else:
            print("No " + word + " today")
            time.sleep(2)

    except Exception as e:
        print("Could not establish a connection: " + e.__str__())


if __name__ == '__main__':
    run("Graupenrisotto", "https://www.ahoch2-suppenbar.de/")
