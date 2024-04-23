nama_file = input("Nama file: ")

try:
    with open(nama_file, "r", encoding="utf8") as file:
        pertanyaan_jawaban = [line.strip().split("||") for line in file]

        for pertanyaan, jawaban in pertanyaan_jawaban:
            print(pertanyaan)
            if input().strip().lower() == jawaban.strip().lower():
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")

except FileNotFoundError:
    print("File tidak ditemukan.")
except Exception as e:
    print("Terjadi kesalahan:", e)
