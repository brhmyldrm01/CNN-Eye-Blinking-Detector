from PIL import Image
from autocrop import Cropper

#Auto crop kütüphanesi kullanılarak verilerin yüz kısımları kırpılır. Böylece arkaplandaki gürültüler azaltılmış olur.

cropper = Cropper()

cropped_array = cropper.crop('enter_test_2.jpg')

if cropped_array is not None:
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save('deneme.jpg')