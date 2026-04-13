<div align="center">

```
  ██████ ██    ██ ██████  ███████ ██      ███████ ██    ██ ████████ ██   ██
 ██      ██    ██ ██   ██ ██      ██      ██      ██    ██    ██    ██   ██
  █████  ██    ██ ██████  ███████ ██      █████   ██    ██    ██    ███████
      ██ ██    ██ ██   ██      ██ ██      ██      ██    ██    ██    ██   ██
 ██████   ██████  ██████  ███████ ███████ ███████  ██████     ██    ██   ██
```

**Simple Subdomain Finder**

[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-39ff14?style=flat-square)](LICENSE)
[![Author](https://img.shields.io/badge/Author-AhanDotID-00e5ff?style=flat-square)](https://ahandotid.github.io)

</div>

---

## 📌 About

SubSleuth adalah tools sederhana untuk mencari subdomain dari sebuah domain target menggunakan teknik DNS resolution. Cocok untuk CTF, bug bounty recon, dan pembelajaran cybersecurity.

> ⚠️ **Disclaimer**: Tools ini hanya untuk keperluan edukasi dan pengujian pada sistem yang kamu miliki atau telah mendapat izin. Penggunaan tanpa izin adalah ilegal.

---

## ⚡ Features

- 🔍 Built-in wordlist 100+ kata umum
- ⚡ Multi-threading untuk scanning lebih cepat
- 📁 Support custom wordlist eksternal
- 💾 Save hasil ke file `.txt`
- 🎨 Colored terminal output
- ⌨️ Ctrl+C safe - hasil tersimpan saat dihentikan

---

## 🔧 Requirements

- Python 3.6+
- Tidak perlu install library tambahan - menggunakan module bawaan Python!

---

## 📥 Installation

**1. Clone repository:**
```bash
git clone https://github.com/AhanDotID/subsleuth.git
cd subsleuth
```

**2. Atau download langsung:**
```bash
wget https://raw.githubusercontent.com/AhanDotID/subsleuth/main/subsleuth.py
```

**3. Beri permission execute (Linux/Mac):**
```bash
chmod +x subsleuth.py
```

---

## 🚀 Usage

### Basic - scan dengan wordlist bawaan
```bash
python3 subsleuth.py example.com
```

### Custom wordlist
```bash
python3 subsleuth.py example.com -w wordlist.txt
```

### Tambah jumlah thread (lebih cepat)
```bash
python3 subsleuth.py example.com -t 100
```

### Simpan hasil ke file
```bash
python3 subsleuth.py example.com -o hasil.txt
```

### Verbose mode (tampilkan semua percobaan)
```bash
python3 subsleuth.py example.com -v
```

### Kombinasi semua opsi
```bash
python3 subsleuth.py example.com -w wordlist.txt -t 100 -o hasil.txt -v
```

---

## 📋 Options

| Argument | Keterangan | Default |
|----------|-----------|---------|
| `domain` | Target domain (wajib) | - |
| `-w, --wordlist` | Path ke file wordlist custom | Built-in list |
| `-t, --threads` | Jumlah thread | `50` |
| `-o, --output` | Simpan hasil ke file | Tidak disimpan |
| `-v, --verbose` | Tampilkan semua percobaan | Off |

---

## 📤 Example Output

```
[*] Target  : example.com
[*] Words   : 100
[*] Threads : 50
[*] Started : 14:32:01

─────────────────────────────────────────────────────
  [+] www.example.com                  → 93.184.216.34
  [+] mail.example.com                 → 93.184.216.50
  [+] api.example.com                  → 93.184.216.51
  [+] dev.example.com                  → 93.184.216.52

─────────────────────────────────────────────────────
[✔] Found   : 4 subdomain(s)
[*] Time    : 3.21s
```

---

## 📁 Custom Wordlist Format

Buat file `.txt` dengan satu kata per baris:

```
www
mail
api
dev
staging
admin
# ini komentar, diabaikan
```

Wordlist publik yang bisa dipakai:
- [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)
- [Assetnote Wordlists](https://wordlists.assetnote.io/)

---

## 📌 Tips Penggunaan

```bash
# Gunakan wordlist dari SecLists untuk hasil lebih maksimal
python3 subsleuth.py target.com -w /path/to/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -t 100 -o results.txt

# Scan cepat dengan thread tinggi
python3 subsleuth.py target.com -t 200

# Simpan dan analisis hasilnya
python3 subsleuth.py target.com -o results.txt && cat results.txt
```

---

## ⚖️ Legal & Ethics

Tools ini dibuat untuk:
- ✅ CTF competitions
- ✅ Bug bounty (pada scope yang diizinkan)
- ✅ Pengujian pada sistem milik sendiri
- ✅ Pembelajaran & edukasi cybersecurity

**DILARANG** digunakan untuk:
- ❌ Scanning tanpa izin
- ❌ Aktivitas ilegal apapun

---

## 👤 Author

**Ahan Pahlevi (AhanDotID)**

[![Website](https://img.shields.io/badge/Portfolio-ahandotid.github.io-39ff14?style=flat-square&logo=github&logoColor=black&labelColor=0d1117)](https://ahandotid.github.io)
[![HackerOne](https://img.shields.io/badge/HackerOne-ahandotid-FF6F61?style=flat-square&logo=hackerone&logoColor=white)](https://hackerone.com/ahandotid)
[![Twitter](https://img.shields.io/badge/Twitter-@paranoiahan-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/paranoiahan)

---

<div align="center">

Made with ♥ by Ahan Pahlevi | CianjurSec 🔐

</div>
