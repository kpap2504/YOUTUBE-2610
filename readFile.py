from pytubefix import YouTube
import pandas as pd
import time

#'title','description','duration','views','likes','dislikes','comments'

def read_file(file_path, header=0):
    try:
        data = pd.read_csv(file_path,header=header,names=['url','video_id'])
        return data
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def get_video_info(url):
    try:
        yt = YouTube(url)
        video_info = {
            'url': url,
            'video_id': yt.video_id,
            'title': yt.title,
            'description': yt.description,
            'duration': yt.length,
            'views': yt.views,
            'likes': yt.rating,  # Note: pytubefix may not provide likes/dislikes
            'dislikes': None,   # Placeholder for dislikes
            'comments': None    # Placeholder for comments
        }
        return video_info
    except Exception as e:
        print(f"An error occurred while fetching video info: {e}")
        return None

def process_videos(file_path):
    data = read_file(file_path, header=None)
    if data is not None:
        video_info_list = []
        for index, row in data.iterrows():
            # wait for 1 second to avoid hitting rate limits
            print(f"Processing video {index + 1}/{len(data)}: {row['url']}")
            time.sleep(1)

            url = row['url']
            video_info = get_video_info(url)
            if video_info is not None:
                video_info_list.append(video_info)
        return video_info_list
    else:
        return None

        
# Example usage
if __name__ == "__main__":
    file_path = "video3.txt"  # Replace with your file path
    data = read_file(file_path, header=None)
    '''
    if data is not None:
        #print(data.head())
        print(data)
    '''
    list_url = []
    list_video_id = []
    list_title = []
    list_description = []
    list_duration = []
    list_views = []
    list_likes = []
    list_dislikes = []
    list_comments = []

    processed_videos = process_videos(file_path)
    if processed_videos is not None:
        for video_info in processed_videos:
            list_url.append(video_info['url'])
            list_video_id.append(video_info['video_id'])
            list_title.append(video_info['title'])
            list_description.append(video_info['description'])
            list_duration.append(video_info['duration'])
            list_views.append(video_info['views'])
            list_likes.append(video_info['likes'])
            list_dislikes.append(video_info['dislikes'])
            list_comments.append(video_info['comments'])

            #print(video_info)   
    data = {
        'url': list_url,
        'video_id': list_video_id,
        'title': list_title,
        'description': list_description,
        'duration': list_duration,
        'views': list_views,
        'likes': list_likes,
        'dislikes': list_dislikes,
        'comments': list_comments
    }
    #print(data)
    df = pd.DataFrame(data)
    df.to_csv('video_info.csv', index=False)
    df.to_excel('video_info.xlsx', index=False)

