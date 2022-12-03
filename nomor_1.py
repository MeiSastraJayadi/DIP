import cv2 
import matplotlib.pyplot as plt

# Membaca sebuah image ke dalam file
image = cv2.imread('./new_scenery.jpg')

# Membuat sebuah dimensi untuk image yang akan dibuat
height = int(image.shape[0] * 0.2)
width = int(image.shape[1] * 0.2)
dim = (height, width) ## DImensi baru dari image yang akan di resize

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA) ## Resize image dengan dimensi yang baru
color = ['b', 'g', 'r'] #List dari warna yang akan ditampilkan pada histogram

fig = plt.figure() # Membuat sebuah figure dengan plt
fig.add_subplot(211).set_title('Gambar 1') # Membuat subplot pada figure
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #Tampilkan image dengan menggunakan plt

fig.add_subplot(212).set_title('Histogram') # Membuat subplot pada figure

for i, col in enumerate(color) : #melakukan looping sebanyak tiga kali 
    """
    calcHist digunakan untuk membuat histogram. 
    calcHist di bawah berisi tiga parameter yang terdiri dari : 
    - resized, yaitu image yang telah di resize
    - [i], yaitu index channel gambar yang akan digunakan  
    - None, yang berarti tidak menggunakan mask 
    - [256] yang artinya ada 256 jenis value pada channel dari 0-255
    - [0, 256], yang artinya 0 adalah nilai minimum dan 255 adalah nilai maksimal 
    """
    hist = cv2.calcHist([resized], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)

plt.show() # Menampilkan figure 



