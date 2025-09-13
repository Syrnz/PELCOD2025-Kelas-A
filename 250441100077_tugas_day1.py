# 1. Kamu sedang marathon TV series di netflix
#    1 episode berdurasi 35 min dengan total 10 episode
#    berapa jam kamu menonton TV series tersebut?

print("="*50)
eps = 35
all_eps = 10
marathon = eps * all_eps
print("1 episode = 35 menit")
print("total nonton 10 episode")
print("total durasi ", marathon, "menit")
total_jam = marathon / 60
print(int(total_jam), "jam")
print("="*50)

# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------

# 2. Kamu ingin membeli cupang dg harga 10rb dan koi dg harga 20rb
#    uang yg kamu bawa sebesar Rp.XXX000 (ganti XXX dg 3 angka terakhir NIM + 100)
#    kamu hanya beli 5 cupang dan 2 koi
#    berapa sisa uang kamu?

print("="*50)
cupang = 10000
koi = 20000
uang_reno = 177000

uang_reno -= ((cupang*5) + (koi*2))
print(uang_reno)

# atau bisa dengan : 

# beli =(uang_reno) - ((cupang*5) + (koi*2))
# print(beli)


print("="*50)

# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------

# # 3. Kamu ingin pergi liburan dg sepeda motor
#    total jarak perjalanan XXX KM (ganti XXX dg 3 angka terakhir NIM)
#    konsumsi BBM sepeda motor 2.7 KM per Liter
#    kapasitas tangki sepeda motor X Liter (ganti X dg 1 angka terakhir NIM)
#    harga bensin per liter Rp.1XXX0 (ganti XXX dg 3 angka terakhir NIM)
#    jika total bensin yg dibutuhkan > 3 liter, maka dapat diskon Rp.500 per liter
#    berapa total bensin yg dibutuhkan, harga bensin per liter setelah diskon (jika ada)- 
#    total biaya bensin, dan prakiraan berapa kali kamu harus mengisi bensin (dengan asumsi tangki penuh setiap kali isi)?
#    NB: HARUS PAKAI INPUT !!!!!

print("="*50)

import math

jarak_perjalanan = int(input("berapa total jarak perjalanan? "))
konsumsi_bbm = float(input("berapa konsumsi bbm pedmod per liter? "))
kapasitas_tangki = int(input("berapa kapasitas tangki sepeda motor? "))
bensin_per_liter = int(input("harga bensin ialah : "))

total_bensin = jarak_perjalanan / konsumsi_bbm

if total_bensin > 3:
    harga_diskon = bensin_per_liter - 500
else:
    harga_diskon = bensin_per_liter

total_biaya = total_bensin * harga_diskon
jumlah_isi_bensin = math.ceil(total_bensin / kapasitas_tangki)

print("Total bensin yang dibutuhkan :", total_bensin, "liter")
print("Harga bensin per liter       : Rp.", harga_diskon)
print("Total biaya bensin           : Rp.", int(total_biaya))
print("perkiraan isi bensin         :", jumlah_isi_bensin, "kali, samapi tangki penuh" )

print("="*50)



# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------




#                            😀 SELAMAT MENGERJAKAN !!!! 😀