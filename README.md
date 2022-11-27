# Crack Detection Tools
This is a set of programs to find a cracks in surfaces using OpenCV.
It also provides tools to prepare a dataset for further processing using deep learning techniques.

## Application Breakdown
This is the breakdown of a project.
```
crack-detection-opencv
│   README.md
│  .gitignore
│   requirements.txt
│   utils.py
│   split_images.py
│   resize_images.py
│   crack_detection.py
│
└───input
│   │   ...
│   │
└───output
│   │   ...
│   │
└───line_segmentation_examples
    │   ...

```

## Deployment
Lets walk through setting up your development environment and deploying this application on your local machine

1. Install Python, pip, and virtualenv
  - [Python](https://www.python.org/)
  - [pip](https://pip.pypa.io/en/stable/installing/)
  - [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

```
sudo apt-get install python3
sudo apt install python3-pip
sudo apt install python3-virtualenv
```

2. Clone this repo and CD into the projects directory
```
git clone https://github.com/hpcbg/crack-detection-opencv.git
cd crack-detection-opencv
```
3. Create and activate a virtualenv
```
virtualenv venv
source venv/bin/activate
```
4. Install packages
```
pip install -r requirements.txt
```

5. Run it
```
python3 resize_images.py -s 50 -i /input_folder -o /output_folder
python3 split_images.py -s 100 -i /input_folder -o /output_folder

python3 crack_detection.py

```
