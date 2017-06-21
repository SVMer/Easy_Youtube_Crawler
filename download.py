import sys
import os
from pytube import YouTube

def main(query):
    if not os.path.exists(query):
        os.makedirs(query)

    file_links = open('video_links_%s.txt'%query, "a+")
    file_links.seek(0)
    links = [item for item in file_links.read().split('\n') if item != '']

    file_dl_links = open('downloaded_links_%s.txt'%query, "a+")
    file_dl_links.seek(0)
    dl_links = [item for item in file_dl_links.read().split('\n') if item != '']

    dl_queue = [i for i in links if i not in dl_links]
    for l in dl_queue:
        print('downloading', l)
        yt = YouTube(l)
        # print(yt.filter('flv'))
        # print(yt.filter('mp4')[-1])
        # print(yt.filter(resolution='480p'))
        # video = yt.get('3gp', '144p')
        # print(yt.filename)
        video = yt.get_videos()[-1]
        video.download(query + '/')

        file_dl_links.write(l)
        file_dl_links.flush()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please give some words as a query')
    else:
        query = '+'.join( sys.argv[1::] )
        print('query is %s\n' % query)
        main(query)
