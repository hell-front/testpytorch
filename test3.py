from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = "Dataset\\val\\bees\\54736755_c057723f64.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)

writer.add_image("train",img_array,3,dataformats='HWC')

for i in range(100):
    writer.add_scalar("y = 2x",2*i,i)

writer.close()

