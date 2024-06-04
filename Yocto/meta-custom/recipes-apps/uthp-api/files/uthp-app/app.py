from flask import Flask, request, jsonify
import threading, pamela, pwd, hashlib, websockets, can, asyncio, logging

app = Flask(__name__)
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
clients = set()
candump_running = False  # Default state: CAN dump service is off

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello Word - UTHP Tools"}), 200

def check_password(username, password):
    try:
        pamela.authenticate(username, password)
        user_info = pwd.getpwnam(username)
        return True, user_info.pw_uid  # Return the UID of the user
    except pamela.PAMError as e:
        # Authentication failed
        return False, None
    except KeyError:
        # The username is not found in the local system
        return False, None


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    authentication_successful, user_id = check_password(username, password)
    if authentication_successful:
        return jsonify({"message": "User authenticated", "user_id": hash_uid(user_id)}), 200
    else:
        return jsonify({"message": "Authentication failed"}), 401
def hash_uid(uid):
    # Ensure the UID is in string format
    uid_str = str(uid)
    # Create a new SHA-256 hash object
    hasher = hashlib.sha256()
    # Encode the UID string to bytes and update the hash object
    hasher.update(uid_str.encode('utf-8'))
    # Return the hexadecimal digest of the hash
    return hasher.hexdigest()


# Function to broadcast messages to all connected clients
async def broadcast(data):
    for client in clients:
        await client.send(data)

# WebSocket handler
async def handle_websocket(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            pass  # You can add message handling logic here if needed
    finally:
        clients.remove(websocket)

# Start CAN message processing
async def process_messages():
    while True:
        if candump_running:
            msg = bus.recv()
            if msg.arbitration_id in [0x0CF00400, 0x18FEF100]:
                data_to_send = msg.__str__()
                await broadcast(data_to_send)
        else:
            await asyncio.sleep(1)  # Sleep for 1 second if CAN dump is stopped

# Start the WebSocket server
async def start_websocket_server():
    await websockets.serve(handle_websocket, "192.168.7.2", 8081)

# Start the CAN message processing loop
async def start_can_processing():
    await process_messages()

# REST API endpoint to start the CAN dump service
@app.route('/api/can/start', methods=['POST'])
def start_candump():
    global candump_running
    candump_running = True
    return jsonify({'message': 'CAN dump service started'}), 200

# REST API endpoint to stop the CAN dump service
@app.route('/api/can/stop', methods=['POST'])
def stop_candump():
    global candump_running
    candump_running = False
    return jsonify({'message': 'CAN dump service stopped'}), 200

# REST API endpoint to check if the CAN dump service is running
@app.route('/api/can/status')
def check_candump():
    return jsonify({'candump_running': candump_running}), 200

def start_flask():
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

def main():
    loop = asyncio.get_event_loop()
    loop.create_task(start_can_processing())
    loop.create_task(start_websocket_server())

    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()

    loop.run_forever()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

