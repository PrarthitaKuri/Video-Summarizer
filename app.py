from youtube_transcript_api import YouTubeTranscriptApi

video_id = "vU3dL1cNqgQ"
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Print transcript text
for entry in transcript:
    print(entry['text'])
