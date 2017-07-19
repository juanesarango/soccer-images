from os import environ, listdir
from os.path import isfile, join

from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Concept


APP = ClarifaiApp(api_key=environ['CLARIFAI_API_KEY'])
MODEL = APP.models.get('general-v1.3')
CONCEPTS = [
    Concept('soccer'),
    Concept('ball'),
    Concept('football'),
    Concept('sport'),
    Concept('soccer field'),
    Concept('soccer player'),
    Concept('game'),
    Concept('goal')
]
IMAGE_PATH = 'images'
IMAGES = [join(IMAGE_PATH, f)
          for f in listdir(IMAGE_PATH)
          if isfile(join(IMAGE_PATH, f)) and f.endswith('.jpg')]


def main():
    for image in IMAGES:
        response = MODEL.predict_by_filename(image, select_concepts=CONCEPTS)
        if response and 'outputs' in response:
            tags = response['outputs'][0]['data']['concepts']
            print(f'Prediction for Image: {image}')
            for tag in tags:
                print(f'Tag: {tag["name"]} - {round(tag["value"]*100,2)}%')
            print('\n')


def get_tags():
    response = MODEL.get_info(verbose=True)
    tags = response['model']['output_info']['data']['concepts']
    for tag in tags:
        print(f'Tag: {tag["name"]} - {tag["language"]}')


if __name__ == '__main__':
    main()
