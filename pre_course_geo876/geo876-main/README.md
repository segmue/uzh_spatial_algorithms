## Repository for the UZH Geography Course GEO876


This gitlab repository contains the code base for the demos, practicals and their solutions in jupyter notebook format `(.ipynb)`. 

You have two options to run and experiment with our code examples:


1. Use Binder, which allows you to execute the code in the browser __(easiest, least flexible)__

You find the appropriate links to access Binder on [OLAT](https://lms.uzh.ch/auth/RepositoryEntry/17335388018/CourseNode/105047262099626) 

2. Setup a local Python environment and run the code on your own machine __(takes effort, most flexible)__

There is a guided video on how to set up your local environment [here](add_link.com). In the video we explain what virtual environments are and what they are used for. We also go step by step through the setup process together. Below you find the key components to copy+paste and follow along.  

#### Setup local Python environment

1. Download the entire [code repository](https://gitlab.uzh.ch/geocomp/geo876/-/archive/main/geo876-main.zip) and extract it at your prefered PATH

2. Download and install [Anaconda](https://www.anaconda.com/products/distribution)

3. Open `Anaconda Prompt` by searching in your start menu

4. Enter the code (without `>`) into the console
```
> conda update -n base -c defaults conda
> cd <geo876 practicals PATH>
> conda env create -f env.yml
> conda activate geo876
> jupyter notebook
```

#### In case of errors:

Install packages separately

```
> conda update -n base -c defaults conda
> conda create env -n geo876 python
> conda activate geo876
> conda install -y -c conda-forge numpy pandas matplotlib seaborn
> conda install -y jupyter
> cd <geo387 practicals PATH>
> jupyter notebook
```

5. The last command `jupyter notebook` will start a webclient in your browser through which you can access the Notebooks of the directory that you openend it from (that's why you should change path `cd` to the directory where you downloaded and extracted the practicals to)






