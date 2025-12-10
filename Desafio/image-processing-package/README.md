# Image Processing Package

---

## Description and Features

The package image_processing is a Python library designed to simplify common image processing tasks. This features include:
   Processing:
    - Histogram matching
    - Structural similarity
    - Resize image

   Utils
     - Read and Save image
     - Plot image, result, and histogram

---

## Install and Uninstall

You can locally install the Image Processing Package to test:

```bash
pip install .
```
Uninstallation:
```bash
pip uninstall image-processing
```

---

## Technologies
-  Python
-  matplotlib
-  scikit-image
-  Numpy

## Example

Here are some examples of how to use the Image Processing Package:
### Transferring histogram between images

 ```python
from image_processing.processing import combination
from image_processing.utils import io, plot

# Read two images
image1 = io.read_image('path/to/image1.jpg')
image2 = io.read_image('path/to/image2.jpg')

# Transfer histogram from image2 to image1
result = combination.transfer_histogram(image1, image2)

# Plot the result
plot.plot_result(image1, image2, result)


 ```

![image](https://i.postimg.cc/KzxpvDyZ/Figure-1.png)
---

## License
[MIT](LICENSE.txt)