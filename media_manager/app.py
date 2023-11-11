import os
import pathlib
from rarfile import RarFile
from dotenv import load_dotenv
load_dotenv()

base_directory = (f'''/{os.environ.get('BASE_DIRECTORY', 'media')}''')
delete_size = int(os.environ.get('DELETE_SIZE', 200))*1000000
rar_files = ('.rar', '.r01', '.r00')
video_formats = ('.avi', '.mkv', '.mp4', '.m4v', '.mov', '.wmv')
for root, subFolders, files in os.walk(base_directory):
    print(root)
    for folder in subFolders:
        files = [f for f in pathlib.Path(f'{base_directory}/{folder}').iterdir() if f.is_file()]
        has_video = False
        has_rar = False
        for file in files:
            if str(file).endswith(rar_files):
                has_rar = True
            if str(file).endswith(video_formats):
                has_video = True
        if has_video and has_rar:
            has_legit_video = False
            print(f'deleting rar files from {folder}')
            for file in files:
                if str(file).endswith(video_formats):
                    _path = os.path.join(root, file)
                    size = os.stat(_path).st_size
                    if size > delete_size:
                        has_legit_video = True
            for file in files:
                if not str(file).endswith(video_formats) and has_legit_video:
                    os.remove(f'{os.getcwd()}/{file}')
        elif has_rar and not has_video:
            for file in files:
                if str(file).endswith('.rar'):
                    with RarFile(file) as rf:
                        rf.extractall(path=f'{base_directory}/{folder}')

            print(f'extracting rar files for {folder}')