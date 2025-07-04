# Paz – Password Analyzer CLI

یک ابزار خط فرمانی(CLI) ساده برای:

- محاسبهٔ **قدرت** رمز عبور  
- بررسی **لو رفتن** آن در دیتابیس‌های معروف (Have I Been Pwned)   
---
## 🚀 Features

- **Strength Scoring**  
  بر اساس طول، ترکیب حروف بزرگ/کوچک، اعداد، کاراکترهای خاص و جلوگیری از واژه‌های خیلی رایج، به رمز شما از 6 نمره می‌دهد.

- **Breach Check**  
  با استفاده از API سرویس معروف [`Have I Been Pwned`](https://haveibeenpwned.com)، تعداد دفعات افشای رمز در گذشته را نمایش می‌دهد.

---
## 📦 Installation
**From PyPI**  
```bash
pip install paz-cli
```

**From Source**
```bash
git clone https://github.com/MahdiMirshafiee/password-analyzer-cli
cd password-analyzer-cli
python3 -m venv venv
source venv/bin/activate       # Linux/macOS
# venv\Scripts\activate        # Windows PowerShell
pip install -e .
```
---
## ⚙️ Usage
**Direct flag**
```bash
password-analyzer -p 'MyP@ssw0rd!'
password-analyzer --password 'MyP@ssw0rd!'
# Password: MyP@ssw0rd!
# Strength: Strong (score: 5)
# Password found in 183 data breaches!
```

**Hidden prompt**
```bash
paz
# Enter password (input hidden): 
# Password: hidden input received
# Strength: Strong (score: 4)
# Password not found in known breaches
```
---
## 🆘 Help
```bash
paz --help
```
---
## 🛠 Contributing
1.	یک Issue باز کنید برای پیشنهاد فیچر یا گزارش باگ
2.	از برنچ dev :شاخه‌ای بسازید
```bash
git checkout dev
git checkout -b feature/your-feature-name
```
3.	تغییرات را commit کنید و push:
```bash
git add .
git commit -m "[شرح کوتاه تغییرات]"
git push origin feature/your-feature-name
```
4.	یک Pull Request از شاخهٔ خود به dev باز کنید
---
## 📄 License
This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
