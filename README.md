# AI Challenge 4 Health

### For more about this repository, see the competition page:
### [AIChallenge4Health](https://competitions.codalab.org/competitions/21639).

This repository contains the starting kit of the machine learning competition
AIChallenge4Health 2019 organized by Thales AVS France, in collaboration with Kaizen Solutions and Data Institute of Grenoble. 

The starting kit is a jupyter notebook. It allows an easy an clean introduction
to the challenge.

## Requirements 

### Competition dataset

In order to run the starting kit you need to download the competition dataset
from the [competition page](https://competitions.codalab.org/competitions/21639). Do not forget to sign in `CodaLab` and
register to the competition to be allowed to download the competition dataset.

Competition dataset must be stored in a directory named `Data`. Then you
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

For this starting kit you need `python 3.6`. If you do not have python installed on your
computer, we advise you to install it using
[annaconda](https://docs.anaconda.com/anaconda/install/).

Then you should install the following python packages:

- numpy
- pandas
- tifffile
- matplotlib

These packages can be installed using `pip` or `conda` depending on your python
setup.

### Other tools

In addition to this python environment, it is advised to install the following useful
tool:

- [imageJ](https://imagej.nih.gov/ij/index.html): this tool allows quick visualization
  of tiff imaje stack.

