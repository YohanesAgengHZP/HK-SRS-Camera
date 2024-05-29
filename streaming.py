import subprocess
import requests

ffmpeg_process = None
SRS_API_BASE_URL = 'http://localhost:1985/api/v1/clients'

def start_streaming(resolution='640x360', frame_rate=15, video_codec='libx264', audio_codec='aac', audio_bitrate='128k'):
    global ffmpeg_process

    if ffmpeg_process and ffmpeg_process.poll() is None:
        return 'Streaming is already running!'

    ffmpeg_cmd = [
        'ffmpeg',
        '-rtsp_transport', 'udp',
        '-i', 'rtsp://192.168.68.110:8554/test',
        '-max_muxing_queue_size', '1024',
        '-vf', f'scale={resolution}',
        '-r', str(frame_rate),
        '-c:v', video_codec,
        '-preset', 'veryfast',
        '-crf', '23',
        '-c:a', audio_codec,
        '-b:a', audio_bitrate,
        '-f', 'flv',
        'rtmp://localhost/live/livestream'
    ]

    try:
        ffmpeg_process = subprocess.Popen(ffmpeg_cmd)
        return 'Streaming started successfully!'
    except Exception as e:
        return f'Error starting streaming: {str(e)}'

def stop_streaming():
    global ffmpeg_process

    if ffmpeg_process and ffmpeg_process.poll() is None:
        ffmpeg_process.terminate()
        ffmpeg_process.wait()
        return 'Streaming stopped successfully!'
    else:
        return 'Streaming is not currently running!'

def get_client_ids():
    try:
        response = requests.get(SRS_API_BASE_URL)
        response.raise_for_status()
        clients = response.json().get('clients', [])
        return [client['id'] for client in clients]
    except requests.RequestException as e:
        return f'Error fetching client IDs: {str(e)}'

def delete_client(client_id):
    try:
        response = requests.delete(f'{SRS_API_BASE_URL}/{client_id}')
        response.raise_for_status()
        return f'Client {client_id} deleted successfully!'
    except requests.RequestException as e:
        return f'Error deleting client {client_id}: {str(e)}'
