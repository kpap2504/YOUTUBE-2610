from pytubefix import YouTube
def test():
    yt = YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")
    print(yt.title)
    print(yt.author)
    print(yt.length)
    print(yt.views)
    print(yt.rating)


test()