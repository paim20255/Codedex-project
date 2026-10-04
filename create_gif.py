import imageio.v3 as iio

filenames = ['owl-pic1.png', 'owl-pic2.png', 'owl-pic3.png', 'owl-pic4.png', 'owl-pic5.png']
images = []

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('Owl.gif', images, duration = 700, loop = 0)