# Digital Image Processing Project

This project was carried out during the Topics in Digital Image Processing course at UFPB, taught by Professor Dr. Augusto de Holanda.

The main objective of this project was to compare the results in car identification using the Gaussian Mixture-Based Background/Foreground Segmentation algorithm called MOG2 and the Single Shot Multibox Detector (SSD) neural network.

## Dataset

### Dataset for Training the Neural Network

Initially, an extensive search was carried out to find a dataset with images of Brazilian cars for training the neural network. However, the databases found were not Brazilian and did not reflect the car models present in Brazil.

Therefore, the authors decided to build their own database for training, produced by means of *printscreens* taken in the *Google Maps* tool of cars in different Brazilian states, such as Paraíba, Rio de Janeiro, among others, seeking to obtain a significant diversity of car models present in Brazil. Therefore, a total of 600 images with 3 color channels (RGB scale) and different sizes were obtained.

#### Data Augmentation

Since the data set to train the neural network was small, a data augmentation process was necessary so that it would acquire enough features to identify new instances, adding variability to the set. Thus, rotation, inversion, negative and grayscale operations were applied to the images, with the rotation being performed at an angle of 45º and the flip being done horizontally.

The code for data augmentation performed can be seen here: [Data Augmentation](https://github.com/ryann-arruda/car-detection/blob/main/data_augmentation.ipynb).

#### Annotation

After constructing the dataset, it was necessary to annotate the images (*bounding boxes*), identifying and locating the region containing a car, serving as labels for training the **SSD** neural network, so that it can correctly predict these *bounding boxes* for new input images.

The annotations were made using the LabelImg tool in VOC format, which can be seen below.

![image](https://github.com/user-attachments/assets/aba28896-206a-4a11-9b6d-08c1c4e3d0d0)

#### Requirements for Annotation

Requirements for annotating images are available in the requirements folder: [requirements](https://github.com/ryann-arruda/car-detection/tree/main/requirements)

To install the requirements, you need to run the following command.
```bash
pip install -r "<Path to requirements file for annotation>"
```

### Dataset for Testing and Evaluation

Furthermore, in order to verify the network performance with real data and adjust the variables used by the **MOG2** algorithm, videos were captured at different times of the day (morning, afternoon and evening) in the city of João Pessoa (PB - Brazil).

These videos were captured using mobile devices and have an average duration of 5 seconds, so that their processing does not take too long. Furthermore, despite their short duration, they present a wide variety of vehicles and movement.

## How to Run the Code

### Requirements to Run the Code

Initially, to run the code it is necessary to install the dependencies it uses. Therefore, the following command should be used.

```bash
pip install -r "<Path to requirements file to run code>"
```

The requirements to run the code are available in the requirements folder: [requirements](https://github.com/ryann-arruda/car-detection/tree/main/requirements)

### Run the Code

After all the necessary dependencies have been installed, the code that should be executed is [main.ipynb](https://github.com/ryann-arruda/car-detection/blob/main/main.ipynb).

However, it is important to note that only the desired cells should be executed. In the repository, there is already a file with the weights of the network previously trained by the authors, called **checkpoint_ssd300.pth.tar**. Therefore, if you do not wish to train it again, only the cell from the **Detection** section should be executed for the neural network.

The initial two cells of the **Single Shot Multibox Detector** section before **Training** must be run regardless of what will be run on the model (training, evaluation, or detection).

In order to see the result of MOG2 all cells in the **MOG2** section must be executed.

## Authors

* Alexandre Bezerra ([Alexandreprog](https://github.com/Alexandreprog))
* Florence ([florence-r](https://github.com/florence-r))
* Ryann Carlos ([ryann-arruda](https://github.com/ryann-arruda))
