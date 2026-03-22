import matplotlib.pyplot as plt

nilai = []
for i in range(10):
    n = float(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(n)

maks = max(nilai)
minim = min(nilai)

rata = sum(nilai) / len(nilai)

lulus = [n for n in nilai if n >= 60]
tidak_lulus = [n for n in nilai if n < 60]

print("\n=== HASIL ===")
print("Nilai:", nilai)
print("Tertinggi:", maks)
print("Terendah:", minim)
print("Rata-rata:", rata)
print("Jumlah lulus:", len(lulus))
print("Jumlah tidak lulus:", len(tidak_lulus))

plt.figure()
plt.bar(["Tertinggi", "Terendah"], [maks, minim])
plt.title("Perbandingan Nilai")
plt.show()

plt.figure()
plt.bar(["Lulus", "Tidak Lulus"], [len(lulus), len(tidak_lulus)])
plt.title("Data Kelulusan")
plt.show()

