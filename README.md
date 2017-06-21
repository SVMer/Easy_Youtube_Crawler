# Easy_youtube_dl
This is an easy to use youtube downloader, with somewhat anti-anti-spider technique
<br>

## Requirment
* selenium 3.4.3
* pytube
* lxml
<br>

## Usage
First, use `python crawl.py` to crawl video links, which will be saved in video_links.txt. For example:

    # this command will use 'lecture video' as a search query , and crawl all video links from the search page
    python crawl.py lecture video
<br>
Then, use `python download.py` to download videos, which will be saved in tmp directory. For example:

    # this command will download the video links just crawled
    python download.py lecture video
<br>
