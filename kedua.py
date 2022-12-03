import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread('./new_scenery.jpg') # Memangggil sebuah gambar dengan menggunakan opencv
img2 = cv2.imread('./maple.jpg') # Memanggil gambar lainnya

dim = (6000, 6000) # Membuat variabel untuk dimensi gambar yang baru 
img1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA) # Melakukan resize ulang terhadap gambar 1
img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA) # Melakukan resize ulang terhadap gambar 2
add_image = np.array(img1 + img2).clip(0, 255) # Operasi penjumlahan pada dua gambar (G1 + G2) 

fig = plt.figure() # Membuat sebuah figure dengan menggunakan matplotlib
fig.add_subplot(221).set_title('G2') # membuat sebuah subplot pada figure yang telah dibuat
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)) # Menampilkan gambar 2 (G2) 
fig.add_subplot(222).set_title('G1') # Menampilkan gambar 1 (G!)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
fig.add_subplot(223).set_title('G1 + G2') 
plt.imshow(cv2.cvtColor(add_image, cv2.COLOR_BGR2RGB)) # Menampilkan Gambar G1 + G2
plt.show()
