from flask import Blueprint, request, jsonify
from streaming import start_streaming, stop_streaming, get_client_ids, delete_client

streaming_routes = Blueprint('streaming_routes', __name__)

@streaming_routes.route('/start_streaming', methods=['POST'])
def start_streaming_route():
    if not request.json:
        return jsonify({'error': 'No JSON payload provided'}), 400

    resolution = request.json.get('resolution')
    frame_rate = request.json.get('frame_rate')
    video_codec = request.json.get('video_codec')
    audio_codec = request.json.get('audio_codec')
    audio_bitrate = request.json.get('audio_bitrate')

    result = start_streaming(resolution, frame_rate, video_codec, audio_codec, audio_bitrate)
    return jsonify({'message': result}), 200

@streaming_routes.route('/stop_streaming', methods=['POST'])
def stop_streaming_route():
    streaming_result = stop_streaming()
    
    client_ids = get_client_ids()
    if isinstance(client_ids, str): 
        return jsonify({'error': client_ids}), 500

    delete_results = []
    for client_id in client_ids:
        result = delete_client(client_id)
        delete_results.append(result)
    
    return jsonify({
        'streaming_result': streaming_result,
        'delete_results': delete_results
    }), 200
