# Paz – Password Analyzer CLI   
# ![License](https://img.shields.io/badge/license-MIT-green) [![PyPI](https://img.shields.io/pypi/v/paz-cli)](https://pypi.org/project/paz-cli/) ![Package Size](https://img.shields.io/badge/size-5.0KB-red)

A simple Command Line Interface (CLI) tool for:

- Calculating password strength 
- Checking if it has been leaked in well-known databases (Have I Been Pwned)  
---
## 🚀 Features

- **Strength Scoring**  
  Based on length, combination of uppercase/lowercase letters, digits, special characters, and avoiding very common words, gives your password a score out of 6.

- **Breach Check**  
  Using the well-known [`Have I Been Pwned`](https://haveibeenpwned.com) API, displays the number of times the password has been leaked in the past.
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
paz -p 'MyP@ssw0rd!'
paz --password 'MyP@ssw0rd!'
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
1.	Open an issue to suggest a feature or report a bug
2.	Create a branch from dev:
```bash
git checkout dev
git checkout -b feature/your-feature-name
```
3.	Commit and push your changes:
```bash
git add .
git commit -m "[Short description of changes]"
git push origin feature/your-feature-name
```
4.	Open a Pull Request from your branch to dev
---
## 📄 License
This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
