# TAG IMAGE RECOGNITION

The objective was to use the Clarifai API for image recognition.
Several images are analized to predict if they are related with soccer games or fields.


## Use

For using the app is necessary to get an API_KEY from the service: `https://developer.clarifai.com/` and export this into the environment.

`pip install -r requirements.txt`
`python clarifai_video.py`

The result of analizing the 3 example images are:

```
Prediction for Image: images/girls.jpg
Tag: game - 48.29%
Tag: sport - 38.66%
Tag: soccer - 32.69%
Tag: ball - 31.92%
Tag: football - 23.88%
Tag: goal - 3.35%
Tag: soccer field - 1.29%
Tag: soccer player - 1.25%


Prediction for Image: images/guitar_man.jpg
Tag: game - 53.03%
Tag: sport - 21.42%
Tag: ball - 15.61%
Tag: football - 9.24%
Tag: soccer - 9.23%
Tag: goal - 2.61%
Tag: soccer player - 1.06%
Tag: soccer field - 1.04%


Prediction for Image: images/videogol.jpg
Tag: ball - 99.39%
Tag: soccer - 98.91%
Tag: sport - 98.48%
Tag: football - 97.0%
Tag: soccer field - 96.68%
Tag: soccer player - 96.44%
Tag: game - 95.34%
Tag: goal - 91.25%
```