# import ffmpeg
# import os

# def merge_video_audio_subs(video_path, audio_path, subtitle_path, output_path):
#     # Ensure output directory exists
#     output_directory = os.path.dirname(output_path)
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     try:
#         # Proper FFmpeg chaining (each input is called on ffmpeg, not on a stream)
#         input_video = ffmpeg.input(video_path)
#         input_audio = ffmpeg.input(audio_path)

#         (
#             ffmpeg
#             .output(
#                 input_video.video.filter('subtitles', subtitle_path),
#                 input_audio.audio,
#                 output_path,
#                 vcodec='libx264',
#                 acodec='aac',
#                 shortest=None
#             )
#             .overwrite_output()
#             .run()
#         )
#         print(f"✅ Final video saved to {output_path}")
#     except ffmpeg.Error as e:
#         print(f"❌ FFmpeg failed:\n{e.stderr.decode()}")
#         raise RuntimeError("Video merging failed") from e




import ffmpeg
import os

def merge_video_audio_subs(video_path, audio_path, subtitle_path, output_path):
    output_directory = os.path.dirname(output_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        input_video = ffmpeg.input(video_path)
        input_audio = ffmpeg.input(audio_path)

        (
            ffmpeg
            .output(
                input_video.video.filter('subtitles', subtitle_path, charenc='UTF-8', force_style='FontName=Arial'),
                input_audio.audio,
                output_path,
                vcodec='libx264',
                acodec='aac',
                shortest=None
            )
            .overwrite_output()
            .run()
        )
        print(f"✅ Final video saved to {output_path}")
    except ffmpeg.Error as e:
        print(f"❌ FFmpeg failed:\n{e.stderr.decode()}")
        raise RuntimeError("Video merging failed") from e
