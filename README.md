# spot-detection-thales-competition

### For more about this repository, see the competition page:
### TODO URL of the competition

This repository contains the starting kit of the machine learning competition
"spot detection organized by thales AVS. 

The starting kit is a jupyter notebook. It's allow an easy an clean introduction
to the challenge.

## Requirements 

### Competition dataset

In order to run the starting kit you need to download the competition dataset
from the competition page: TODO add URL. Do not forget to sign in `CodaLab` and
subscribe to the competition to be allowed to download the competition dataset.

You need to put the competition data in a directory named `Data`. Then you
should have: 

```
.
├── Data
│   ├── imagesTest.tiff <- Validation dataset 
│   ├── imagesTraining.tiff <- Training dataset 
│   └── descriptions_training.csv <- The truth labels of the training dataset
├── startingkit_challenge.ipynb <- This notebook
└── submission_sample.zip <- An example submission
```

### Python 

For this starting kit you need `python 3.6`. If you do not have python on your
computer we advise to install it using
[annaconda](https://docs.anaconda.com/anaconda/install/).

Then you should install the following python packages:

- numpy
- pandas
- tifffile
- matplotlib

These packages can be installed using `pip` or `conda` depending on your python
setup.

### Other tools

In addition to this python environment we advise to install the following useful
tool:

- [imageJ](https://imagej.nih.gov/ij/index.html): this allow quick visualization
  of tiff stack.

