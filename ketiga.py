import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('./new_scenery.jpg') # Memangggil sebuah gambar dengan menggunakan opencv
img2 = cv2.imread('./maple.jpg') # Memanggil gambar lainnya

dim = (6000, 6000) # Membuat variabel untuk dimensi gambar yang baru 
img1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA) # Melakukan resize ulang terhadap gambar 1
img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA) # Melakukan resize ulang terhadap gambar 2
add_image = np.array(img1 + img2).clip(0, 255) # Operasi penjumlahan pada dua gambar (G1 + G2) 

negation = np.array(255 - add_image).clip(0, 255) # Melakukan operasi penurangan pada gambar yang telah ditambahkan

"""
Pada variabel negation, gambar dikurangkan dengan nilai sebesar 255. 
Hal itu dilakukan untuk mendapatkan inverse dari hasil gambar yang 
telah ditambahkan (G! + G2)
"""

# cv2.imshow("Negation Image", negation)
# cv2.waitKey(0)


fig = plt.figure() # Membuat sebuah figure dengan menggunakan matplotlib
fig.add_subplot(211).set_title('G1 + G2') # Menambah subplot pada figure
plt.imshow(cv2.cvtColor(add_image, cv2.COLOR_BGR2RGB)) # MEnampilkan gambar G1 + G2
fig.add_subplot(212).set_title('Negation') # Menambah subplot pada figure
plt.imshow(cv2.cvtColor(negation, cv2.COLOR_BGR2RGB)) # Menampilan gambar negasi
plt.show()

