from flask import Flask, request, jsonify
import subprocess
import os
import uuid

app = Flask(__name__)

@app.route("/", methods=["POST"])
def slice_audio():
    data = request.json
    audio_url = data["audio_url"]
    timestamps = data["timestamps"]
    naming_format = data["naming_format"]

    # Download audio
    audio_filename = f"temp_{uuid.uuid4()}.mp3"
    subprocess.run(["curl", "-o", audio_filename, audio_url])

    output_files = []
    for i, ts in enumerate(timestamps):
        start = ts["start"]
        end = ts["end"]
        output_file = naming_format.replace("{{start}}", start).replace("{{end}}", end)
        output_path = f"slices/{output_file}"
        subprocess.run([
            "ffmpeg", "-i", audio_filename,
            "-ss", start, "-to", end,
            "-c", "copy", output_path
        ])
        output_files.append(output_path)

    return jsonify({"slices": output_files})

if __name__ == "__main__":
    os.makedirs("slices", exist_ok=True)
    app.run(host="0.0.0.0", port=10000)
