# Computer Vision

Open source project that uses computer vision to help identify ditches in Sweden, Poland, Finland and Latvia done by William Lidberg [Mapping Drainage Ditches In Forested Landscapes Using Deep Learning And Aerial Laser Scanning](https://github.com/williamlidberg/Mapping-drainage-ditches-in-forested-landscapes-using-deep-learning-and-aerial-laser-scanning)

Xception-style UNet Implementation from the resource above:

-   UNet implementation: `utils/unet.py` (implementation adapted from: [Oxford Pets Image Segmentation](https://keras.io/examples/vision/oxford_pets_image_segmentation/))
-   Generator implementation: `utils/generator.py`

## Quiz

13 Out of 16 points (**81.25%**)

Time for this attempt: **19 minutes 31 seconds**

**Your Answers:**

---

### 1. The aim of computer vision is to extract information from audio signals.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 2. Traditional computer vision used handcrafted features to solve vision tasks.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 3. The task in object recognition is to find a certain object in an image.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 4. Semantic segmentation assigns a class label to every pixel in the image.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 5. Given the ground truth mask [1, 0, 0, 1, 1] and the segmentation mask [1, 0, 1, 1, 0], what is the intersection over union?

0 / 1 point

Options:

-   1/2

-   4/2

-   1

-   2/3 <span style="color: orangered"> **Incorrect choice**

-   1/2 <span style="color: lime"> **Correct Answer**

> **Feedback based on answering incorrectly::**
> Ground truth and segmentation mask overlap in 2 places and looking at all the places where there is a 1, we have 4. Thus, the answer is 2/4=1/2.

---

### 6. A common network architecture for semantic segmentation is a encoder-decoder network with skip/long ranging residual connections.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 7. The task in object detection is to find every single object in a given image.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 8. Object detection is challenging because we do not know in advance how many objects are in the image.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 9. The mean average precision for object detection is obtained by averaging over the precision scores for every image in the test set.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 10. The RCNN family of object detectors first creates a large number of region proposals, which are then classified as objects.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 11. The region proposal network is trained to consider 9 different anchors at each location in the extracted feature maps.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 12. The purpose of RoI pooling in faster RCNN is to ensure that each region of interest is represented by vectors with the same dimensionality.

0 / 1 point

Your answer: <span style="color: orangered">
**False**

Correct Answer:
<span style="color: lime">
True

---

### 13. Instance segmentation does not differentiate between objects of the same class.

1 / 1 point

True
Correct answer: <span style="color: lime">
**False**

---

### 14. The segmentation head of Mask R-CNN creates a mask for every considered object class.

0 / 1 point

Your answer: <span style="color: orangered">
**False**

Correct Answer: <span style="color: lime">
**True**

> **Feedback based on answering incorrectly:**
> The mask which is finally returned is decided by the classifcation head of Mask R-CNN.

---

### 15. The purpose of RoIAlign is to achieve a better correspondence between the identified region of interest and the pooled vector representation of the region.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 16. The main idea of visual question answering is to answer questions related to a given image.

1 / 1 point

Correct answer: <span style="color: lime">
**True**
