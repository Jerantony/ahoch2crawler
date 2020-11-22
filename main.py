import urllib.request
import time
import playsound

mp3_file = "alarm.wav"


def mine(word):
    found = False
    for i in range(3):
        if found is False:
            try:
                fp = urllib.request.urlopen("https://www.lttstore.com/collections/all?page=" + str(i+1))
                mybytes = fp.read()
                mystr = mybytes.decode("utf8")
                fp.close()

                found = word in mystr
                print("\tSearch #" + str(i+1) + ": Finished.")
            except Exception as e:
                print("\tSearch #" + str(i+1) + ": Could not establish a connection: " + e.__str__())
        else:
            return found
        time.sleep(1)
    return found


def run(word_to_search):
    word_3080_found = mine(word_to_search)
    counter = 1
    while word_3080_found is False:
        print(str(counter) + ": Not found. Wait 1 sec and try again...")
        time.sleep(1)
        word_3080_found = mine(word_to_search)
        counter += 1

    print(str(counter) + ": FOUND!!! GO GO GO!")

    f = open("log.log", "a")
    f.write("Tries done and three times seconds elapsed: " + str(counter) + "\n\n")
    f.close()

    playsound.playsound(mp3_file, True)


if __name__ == '__main__':
    run("3080")
