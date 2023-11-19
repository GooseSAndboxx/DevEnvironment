import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variable to store the last accessed path
last_path = None

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)
    return "Webhook received!", 200

@app.route('/execute', methods=['POST'])
def execute_commands():
    global last_path
    data = request.json
    commands = data.get("commands", [])

    results = []
    for command in commands:
        try:
            # Change the current working directory to the last accessed path
            if last_path and os.path.isdir(last_path):
                os.chdir(last_path)

            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()

            # Update the last accessed path
            if command.startswith('cd '):
                last_path = command[3:]

            # Determine if the command was successful or not
            status = "failure" if process.returncode != 0 else "success"
            results.append({"command": command, "status": status, "output": output, "error": error})
        except subprocess.CalledProcessError as e:
            results.append({"command": command, "status": "failure", "error": str(e)})

    return jsonify(results), 200



    
@app.route('/write-file', methods=['POST'])
def write_files():
    operations = request.json.get("operations", [])
    results = []

    for op in operations:
        file_content = op.get("data")
        file_name = op.get("file_name")
        # Use current directory if 'file_path' is not provided or is an empty string
        file_path = op.get("file_path") or '.'

        # Correct file path if it uses backslashes instead of forward slashes
        file_path = file_path.replace('\\', '/')
        full_path = os.path.join(file_path, file_name)

        try:
            # Ensure that the parent directories exist
            if file_path != '.':
                os.makedirs(file_path, exist_ok=True)

            # Write the content to the file
            with open(full_path, 'w') as file:
                file.write(file_content)

            results.append({
                "file_name": file_name,
                "file_path": file_path if file_path != '.' else '',
                "status": "success"
            })
        except Exception as e:
            results.append({
                "file_name": file_name,
                "file_path": file_path if file_path != '.' else '',
                "error": str(e)
            })

    return jsonify(results), 200







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
