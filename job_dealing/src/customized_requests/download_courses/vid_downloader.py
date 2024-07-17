from configs import PROJECT_BASE_DIRECTORY


def m3u8_video_downloader(m2u8_file='~/Public/temp.m3u8',
                          output_path=f"{PROJECT_BASE_DIRECTORY}/videos/script_output.mp4"):
    import subprocess
    subprocess.run(['ffmpeg',
                    '-protocol_whitelist', 'file,http,https,tcp,tls,crypto',
                    '-i', m2u8_file,
                    '-c', 'copy',
                    '-bsf:a', 'aac_adtstoasc',
                    output_path])
