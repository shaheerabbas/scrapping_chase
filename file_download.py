from time import monotonic
import requests


def download_speed(url):
    r = requests.get(url, stream=True)
    file_size = int(r.headers['content-length'])
    downloaded = 0
    speeds = []
    start = last_print = monotonic()

    with open('hello.mkv', 'wb') as fp:
        for chunk in r.iter_content(chunk_size=4096):
            downloaded += fp.write(chunk)
            now = monotonic()
            if now - last_print > 1:
                pct_done = round(downloaded / file_size * 100)
                if pct_done>5:
                    break
                speed = round(downloaded / (now - start) / 1024)
                speeds.append(speed)
                print(f'Download {pct_done}% done, avg speed {speed} kbps')

                last_print = now

    avg = str(sum(speeds)/len(speeds))
    return avg



if __name__ == "__main__":

    site = "https://hypendium.com/downloads/superbestfriendsplay/Extras/Best%20Friends%20Beat%20Em'%20Ups!/20170301___Best%20Friends%20Beat%20'Em%20Ups%20-%20River%20City%20Ransom%20Underground___rZs9OQQ0cVs.mkv"
    average = download_speed(site)
    print("Average speed of server link is : "+average)