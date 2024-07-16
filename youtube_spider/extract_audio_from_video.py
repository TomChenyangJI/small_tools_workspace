from audio_extract import extract_audio


def extract_audio_customized(input_path, output_path):
    extract_audio(input_path=input_path, output_path=output_path)
    print("Extraction completed!")

# extract_audio_customized("The Best of Imagine Dragons   Greatest Hits Full Album   Top 12 Songs Collection 2024.mp4", "./Imagine Dragons.mp3")

# extract_audio_customized("./mp4/", "夜猫.mp3")