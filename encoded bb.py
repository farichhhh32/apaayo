import time
from threading import Thread, Lock
import sys
import base64

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    print()  

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def decode_lyrics(encoded_lyrics):
    decoded_lyrics = []
    for lyric, speed in encoded_lyrics:
        decoded_lyric = base64.b64decode(lyric).decode('utf-8')
        decoded_lyrics.append((decoded_lyric, speed))
    return decoded_lyrics

def sing_song():
    encoded_lyrics = [
        ("RmF5eWF6YSBQdXRpIFN5YWJhbm51cg==", 0.1), 
        ("SSBsb3ZlIHlvdSBzbyBtdWNo", 0.1), 
        ("VGhhbmtzIGZvciBiZWluZyBleGlzdA==", 0.1), 
        ("SSBkb250IGNvdW50IGEgZGF5IGFzIGEgZGF5IHdoZW4gaW0gbm90IG1pc3NpbmcgdQ==", 0.2), 
        ("SSBnb3QgbGlmZSB0byBzaGFyZSB3aXRoIHlvdSwgc28gc3RheXku", 0.1), 
        ("SSBoYXZlIHNvIG11Y2ggZW5lcmd5IHRvIGxpc3RlbiBhbGwgeW91ciBzdG9yeSwgdG8ga25vdyBhYm91dCB5b3VyIHVwZGF0ZSBhcyBhbHdheXMu", 0.1), 
        ("QmUgYSBnb29kZ2lybCB3aGVuIGltIG5vdCBhcnJvdW5kLCB0cnVzdCBtZSBpbSBhbHNvIGRvaW5nIGdvb2Q=", 0.1), 
        ("bGV0J3MgcnVuIG1pbnV0ZXMgYnkgbWludXRlcyB0byBlbmpveSBvdXIgbG92ZQ==", 0.1),
        ("TWFkZSBieSB5b3VyIGxvdmUsIEZhcmlkIDwz", 0.1)
    ]
    
    lyrics = decode_lyrics(encoded_lyrics)
    delays = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 35.0] 
    threads = []

    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

sing_song()
