import subprocess
import os
path="./samples"

def convert_mp3_to_wav(input_file, output_file):
    try:
        subprocess.run(['ffmpeg', '-i', input_file, output_file])
        print('Conversion successful!')
    except Exception as e:
        print('Conversion failed:', str(e))
c=1
for i in os.listdir(path):
    output_file = f'./wavSamples/{c}.wav'
    convert_mp3_to_wav(f"{path}/{i}", output_file)
    c+=1

print("Done Successfully!")