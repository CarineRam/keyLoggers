from flask import Flask, request

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def receive_logs():
    # log_data = request.form['log']
    # with open("server_log.txt", "a") as log_file:
    #     log_file.write(f"{log_data}\n")
    # return "Log received", 200
    logs = request.form.get('logs')
    print(f"Received logs: {logs}")
    if logs:
        with open("server_log.txt", "a") as log_file:
            log_file.write(logs + "\n")
        return "Logs received", 200
    return "No logs received", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
