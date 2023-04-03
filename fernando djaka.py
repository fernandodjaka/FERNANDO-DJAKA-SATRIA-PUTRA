#!/usr/bin/env python
# coding: utf-8

# In[1]:


nama_lengkap = input("Masukkan nama lengkapmu: ")

# Menghitung jumlah huruf dari nama lengkap
jumlah_huruf = len(nama_lengkap) - nama_lengkap.count(" ")

# Menghitung jumlah huruf vokal dari nama lengkap
vokal = "aeiou"
jumlah_vokal = sum(1 for huruf in nama_lengkap.lower() if huruf in vokal)

# Menghitung jumlah huruf konsonan dari nama lengkap
konsonan = "bcdfghjklmnpqrstvwxyz"
jumlah_konsonan = sum(1 for huruf in nama_lengkap.lower() if huruf in konsonan)

# Menampilkan hasil
print(f"Jumlah huruf dari nama lengkapmu: {jumlah_huruf}")
print(f"Jumlah huruf vokal dari nama lengkapmu: {jumlah_vokal}")
print(f"Jumlah huruf konsonan dari nama lengkapmu: {jumlah_konsonan}")


# In[ ]:




