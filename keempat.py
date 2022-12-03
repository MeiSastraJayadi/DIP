import numpy as np
import cv2 
from matplotlib import pyplot as plt

img1 = cv2.imread('./new_scenery.jpg') # Memangggil sebuah gambar dengan menggunakan opencv
img2 = cv2.imread('./maple.jpg') # Memanggil gambar lainnya

dim = (6000, 6000) # Membuat variabel untuk dimensi gambar yang baru 
img1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA) # Melakukan resize ulang terhadap gambar 1
img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA) # Melakukan resize ulang terhadap gambar 2
add_image = np.array(img1 + img2).clip(0, 255) # Operasi penjumlahan pada dua gambar (G1 + G2) 

"""
np.histogram adalah fungsi dalam numpy yang digunakan untuk membuat histogram dari 
data yang telah dimasukan. Pada variabel hist di bawah, np.histogram akan 
mengkalkulasi seberapa banyak nilai pixel dari 0 - 255 muncul pada gambar 
"""

hist,bins = np.histogram(add_image.flatten(),256,[0,256])

"""
CDF adalah fungsi akumulasi daei sebaran data atau nilai pixel
"""
cdf = hist.cumsum() # Culmulatif Distribution Function
cdf_normalized = cdf * float(hist.max()) / cdf.max() # Melakukan normalisasi pada cdf

cdf_m = np.ma.masked_equal(cdf, 0) # Membuat cdf mask
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min()) # Melakukan Kalkuasi pada cdf mask
cdf = np.ma.filled(cdf_m,0).astype('uint8') # Mengisi sebuah nilai jika terdapat value 0 pada cdf mask
equalize_img = cdf[add_image] # Hasil gambar yang telah di ekualisasi

hist2,bins2 = np.histogram(equalize_img.flatten(),256,[0,256]) # Membuat histogram dari hasil gambar yang telah di ekualisasi
cdf2 = hist.cumsum() # Menghitung akumulasi dari hist2
cdf_normalized2 = cdf * float(hist.max()) / cdf.max() # cdf yang telah di normalisasi

fig = plt.figure() # Membuat sebuah fiure dari matplotlib 
fig.add_subplot(221).set_title('Sebelum') # Membuat subplot
plt.imshow(add_image) # Menampilkan gambar sebelum di ekualisasi
fig.add_subplot(222)
plt.plot(cdf_normalized, color = 'b') # Membuat sebuah plot untuk cdf yang telah di normalisasi
plt.hist(add_image.flatten(),256,[0,256], color = 'r') # Membuat histogram
plt.xlim([0,256]) # Menentukan nilai minimum dna maksimal dari plot
plt.legend(('cdf','histogram'), loc = 'upper left')
fig.add_subplot(223).set_title('Sesudah')
plt.imshow(equalize_img) #Menampilkan gambar yang telah di ekualisasi
fig.add_subplot(224)
plt.plot(cdf_normalized2, color = 'b')
plt.hist(equalize_img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()


