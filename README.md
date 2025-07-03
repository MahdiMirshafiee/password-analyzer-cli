# Paz – Password Analyzer CLI

**Paz** یک ابزار خط‌فرمانی ساده و قدرتمند برای:

- محاسبهٔ **قدرت** رمز عبور  
- بررسی **لو رفتن** آن در دیتابیس‌های معروف (Have I Been Pwned)  
- امکان وارد کردن رمز به‌صورت **مخفی** یا با فلگ `-p`  

## Features

- **Strength Scoring**  
  بر اساس طول، ترکیب حروف بزرگ/کوچک، اعداد، کاراکترهای خاص و جلوگیری از واژه‌های خیلی رایج، به رمز شما نمره می‌دهد.

- **Breach Check**  
  با استفاده از API **Have I Been Pwned** و روش K-Anonymity، تعداد دفعات لو رفتن رمز در گذشته را نمایش می‌دهد.

- **Hidden Input**  
  اگر گزینهٔ `--password` ارائه نشود، از شما درخواست می‌کند رمز را مخفی وارد کنید (رشته در ترمینال نمایش داده نمی‌شود).

- **Lightweight & Zero-Config**  
  بدون نیاز به تنظیمات پیچیده؛ فقط نصب، اجرا و دریافت خروجی رنگی.



## Installation
<p>🔹 Python 3.10+</p>

**From PyPI**  
pip install paz

**From Source**
git clone https://github.com/MahdiMirshafiee/password-analyzer-cli
cd password-analyzer-cli
python3 -m venv venv
source venv/bin/activate       # Linux/macOS
# venv\Scripts\activate        # Windows PowerShell
pip install -e .

## Usage
**Direct flag**
password-analyzer -p 'MyP@ssw0rd!'
# Password: MyP@ssw0rd!
# Strength: Strong (score: 5)
# Password found in 183 data breaches!

**Hidden prompt**
paz
# Enter password (input hidden): 
# Password: hidden input received
# Strength: Strong (score: 4)
# Password not found in known breaches

## Help
paz --help

## Contributing
1.	یک Issue باز کنید برای پیشنهاد فیچر یا گزارش باگ
2.	از برنچ dev :شاخه‌ای بسازید
git checkout dev
git checkout -b feature/your-feature-name
3.	تغییرات را commit کنید و push:
git add .
git commit -m "[شرح کوتاه تغییرات]"
git push origin feature/your-feature-name
4.	یک Pull Request از شاخهٔ خود به dev باز کنید

## License
This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
