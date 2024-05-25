from flask import Flask, request, jsonify
import pamela, pwd, hashlib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello Word - UTHP"}), 200

# def check_password(username, password):
#     print("In check_password", username)
#     try:
#         # Fetch user info from /etc/passwd
#         pw = pwd.getpwnam(username)
#         print("username: ", pw)
#         # Fetch encrypted password from /etc/shadow
#         spw = spwd.getspnam(username)
#         # Verify the password
#         if crypt.crypt(password, spw.sp_pwdp) == spw.sp_pwdp:
#             return True
#     except KeyError:
#         return False
#     return False


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

