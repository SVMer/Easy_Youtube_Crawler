# Easy_youtube_dl
This is a Simple and Easy to Use youtube video crawler, with somewhat anti-anti-spider technique
<br>
<br>

## Requirment
* selenium 3.4.3
* pytube
* lxml
<br>

## Usage
First, use `python crawl.py` to crawl video links, which will be saved in video_links.txt. For example:

<pre><code># this command will use 'SVM' as a search query , and crawl all video links from the search page
python crawl.py SVM
    
# or you can use this command to search 'lecture video'
python crawl.py lecture video
</code></pre>
<br>

Then, use `python download.py` to download videos, which will be saved in tmp directory. For example:

<pre><code># this command will download 'SVM' video according to the links just crawled
python download.py SVM
    
# or download 'lecture video' video by this command 
python download.py lecture video
</code></pre>
<br>
