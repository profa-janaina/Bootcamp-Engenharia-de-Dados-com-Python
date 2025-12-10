from image_processing.processing import combination
from image_processing.utils import io, plot

image1 = io.read_image("C:/Users/Pessoal/Desktop/test_image_processing/fall.jpg") #change the path
image2 = io.read_image("C:/Users/Pessoal/Desktop/test_image_processing/autumn.jpg")

# Transfer histogram from image2 to image1
result = combination.transfer_histogram(image1, image2)

# Plot the result
plot.plot_result(image1, image2, result)