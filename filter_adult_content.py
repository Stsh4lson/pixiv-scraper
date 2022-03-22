import shutil
import pathlib
import os
from tqdm import tqdm
import pandas as pd
import json

def filter_adult_content():
    with open('items.json', 'rt', encoding='utf-8') as filehandle:
        data = json.load(filehandle)
        data = pd.DataFrame(data)

    pathlib.Path("/".join(('images', 'adult'))).mkdir(parents=True, exist_ok=True)

    for index, row in tqdm(enumerate(data.iterrows()), total=data.shape[0]):
        if row[1]['sexual']:
            image_name = row[1]['image_paths'][0].split('/')[-1]
            current_path = "/".join(('images', 'full', image_name))
            move_path = "/".join(('images', 'adult', image_name))
            if os.path.isfile(current_path):
                try:
                    shutil.move(current_path, move_path)
                except Exception:
                    raise ValueError('Problem while moving file between folders')
    print('Moved all files')
    
if __name__=="__main__":
    filter_adult_content()