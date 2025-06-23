# ffmpeg-audio-slicer

A webhook-based audio slicer using Flask and FFmpeg. Accepts POST requests with audio URL and timestamp data, returns sliced audio clips.

## Usage

POST to `/` with JSON body:
{
  "audio_url": "https://...",
  "timestamps": [
    {"start": "00:00", "end": "00:10"},
    ...
  ],
  "naming_format": "clip_{{start}}_{{end}}.mp3"
}

### Returns:
{
  "slices": ["slices/clip_0000_0010.mp3", ...]
}
