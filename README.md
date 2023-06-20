# tuto-video-tracking

Ce repository sert de tutoriel pour faire une première captation vidéo ainsi qu'une analyse de tracking sur cette vidéo


## Setup

1. Install python:
> https://www.python.org/downloads/

2. Install requirements:

> pip install -r requirements.txt

## Install

- Conda https://docs.conda.io/en/latest/ 

Or

- Pyhon https://www.python.org/downloads/ and https://code.visualstudio.com/

Modules 

- Opencv https://opencv.org/blog/2022/12/29/opencv-4-7-0/
- Openpose https://github.com/CMU-Perceptual-Computing-Lab/openpose

Docker

- https://www.docker.com/

- Image à utiliser https://github.com/seancook/docker-openpose-cpu

Webcams

- Make sure you have one and it works


Utilisation de l'image Docker

docker run -v`pwd`/frames:/frames -it seancook/openpose-cpu -display 0 -image_dir /frames -write_images /frames -write_json /frames