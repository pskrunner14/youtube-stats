from json import load

import warnings
warnings.filterwarnings("ignore")

import pandas as pd

from youtube import YouTube
from tqdm import tqdm


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config_dict = load(f)

    _api_service_name = config_dict['api_service_name']
    _api_version = config_dict['api_version']
    _api_key = config_dict['api_key']

    df = pd.read_csv("channels.csv")
    channel_ids = df["id"].tolist()

    youtube = YouTube(_api_service_name, _api_version, _api_key)

    df = pd.DataFrame()

    for i, ch in enumerate(channel_ids):
        print(i, ": ", ch)
        video_ids = youtube.get_video_ids(ch)
        for vd in tqdm(video_ids):
            try:
                stats = youtube.get_video_stats(vd)
                data = {
                    "video_id": vd,
                    "channel_id": ch
                }
                data.update(stats)
                df = df.append(data, ignore_index=True)
            except Exception as e:
                print(e)

        df.to_csv("stats.csv", index=False)