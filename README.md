# Youtube Stats

Get Channel and Video stats from Youtube Data API v3.


## Setup

Install python dependencies:

```bash
pip install -r requirements.txt
```

## Run

Create an API key via Google Cloud console and add it to `config.json`

Add channel IDs in `channels.csv` and run the main script:

```bash
python main.py
```

Video stats will be dumped in `stats.csv`.