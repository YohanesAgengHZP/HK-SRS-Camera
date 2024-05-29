import requests
import json

payload = {
    "resolution": "640x360",
    "frame_rate": 15,
    "video_codec": "libx264",
    "audio_codec": "aac",
    "audio_bitrate": "128k"
    # "keystream": "livestream"
}

json_payload = json.dumps(payload)

headers = {'Content-Type': 'application/json'}

response = requests.post('http://localhost:5000/start_streaming', data=json_payload, headers=headers)

print(response.text)
