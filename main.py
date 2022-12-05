import subprocess
from glob import glob
import os
import ffmpeg


def uno():
    allaudiofiles=glob('audio\AudioClip\*.wav')

    allaudiofilesname=[]
    for audiofile in allaudiofiles:
        audiofile=audiofile.split('\\')[-1]
        allaudiofilesname.append(audiofile)

    allaudiofilesnamewithout=[]
    for audiofile in allaudiofilesname:
        if audiofile=="Pre-Roll-Loop Level 01 - Processed.wav":
            pass
        else:
            audiofile=audiofile.split(' Audio')[0]
            allaudiofilesnamewithout.append(audiofile)
    for i in range(len(allaudiofilesname)):
        if i==841:
            pass
        else:
            os.rename(rf'audio\AudioClip\{allaudiofilesname[i]}',rf'audio\AudioClip\{allaudiofilesnamewithout[i]}.wav')

    allaudiofilesname.sort()

    allaudiofiles=glob('audio\AudioClip\*.wav')

    allaudiofilesname=[]
    for audiofile in allaudiofiles:
        audiofile=audiofile.split('\\')[-1]
        allaudiofilesname.append(audiofile)

    allaudiofilesname.sort()

    os.makedirs(name=rf"exportmkv")
    os.makedirs(name=rf"exportmp4")

def dos():
    allaudiofiles=glob('audio\AudioClip\*.wav')

    allaudiofilesname=[]
    for audiofile in allaudiofiles:
        audiofile=audiofile.split('\\')[-1]
        allaudiofilesname.append(audiofile)
    allaudiofilesname.sort()

    allvideofiles=glob('video\VideoClip\*.mp4')
    allvideofilesname=[]
    for videofile in allvideofiles:
        videofile=videofile.split('\\')[-1]
        allvideofilesname.append(videofile)

    allvideofilesname.sort()

    for finalfile in range(len(allvideofilesname)):
        try:
            cmd = f'ffmpeg -y -loglevel error -stats -i "audio\AudioClip\{allaudiofilesname[finalfile]}" -r 30 -i "video\VideoClip\{allvideofilesname[finalfile]}" -filter:a aresample=async=1 -c:a flac -c:v copy "exportmkv\{allvideofilesname[finalfile].split(".mp4")[0]}.mkv"'
            subprocess.call(cmd, shell=True)
            print(f'{finalfile}/{len(allvideofilesname)}')
        except:
            pass

def tres():
    if not os.path.exists("exportmkv"):
        raise Exception("Please create and put all your vidoes in assets folder!")

    mkv_liste = os.listdir("exportmkv")
    mp4_liste = os.listdir("exportmp4")
    mkv_list = []
    am=0
    for element in mkv_liste:
        bouh=element.split(".m")[0]
        bouh=f"{bouh}.mp4"
        if bouh in mp4_liste:
            pass
        else:
            if am==0:
                mkv_list.append(element)
                for i in range(len(mkv_liste)):
                    if mkv_liste[i]==element:
                        try:
                            mkv_list.append(mkv_liste[i-1])
                        except:
                            pass
                        break
                    else:
                        pass
                am=1
            else:
                mkv_list.append(element)


    if not os.path.exists("exportmp4"):
        os.mkdir("exportmp4")
    am=1
    for mkv in mkv_list:
        name, ext = os.path.splitext(mkv)
        if ext != ".mkv":
            raise Exception("Please add MKV files only!")

        output_name = name + ".mp4"
        try:
            subprocess.run(f'ffmpeg -y -loglevel error -stats -i exportmkv/"{mkv}" -strict -2 -filter:v fps=30 exportmp4/"{output_name}"', check=True)
            for i in range(4):
                print(f"{am}/{len(mkv_list)}")
            am+=1
        except:
            raise Exception(
                "Please DOWNLOAD, INSTALL & ADD the path of FFMPEG to Environment Variables!"
            )


    print(f"{len(mkv_list)} video(s) converted to MP4!")
    os.startfile("exportmp4")

print("Welcome to NFB Assets Loader !")
print("1. Rename the files")
print("2. Merge Audio and Video to MKV (Do it in one go)")
print("3. Convert MKV to MP4 (to stop and start as many times as possible ;))")

choix=input("Please enter your choice: ")
if choix=="1":
    uno()
elif choix=="2":
    dos()
elif choix=="3":
    tres()
else:
    print("Please enter a valid choice (restart the script to relaunch) !")