<img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fhits.dwyl.com%2Fwaseemofficial%2FAllure_Reports_PyTest.json%3Fcolor%3Dpink"/>

<p align="center">
  <div align="center">
    <img src="https://github.com/waseemofficial/DSA_Python/blob/main/Images/github_logo_blue.png"/>
  </div>

  <div align="center">
    <a href="https://github.com/waseemofficial">
      <img src="https://img.shields.io/badge/syed-waseem-93b023?&style=plastic"/>
    </a>
    <img src="https://img.shields.io/badge/gitlab-%23181717.svg?style=plastic&logo=gitlab&logoColor=white"/>
    <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=plastic&logo=visual-studio-code&logoColor=white"/>
    <img src="https://img.shields.io/badge/markdown-%23000000.svg?style=plastic&logo=markdown&logoColor=white"/>
  </div>

  <div align="center">
    <a href="https://github.com/waseemofficial">
      <img src="https://img.shields.io/github/followers/waseemofficial?label=Follow%20Me&style=social"/>
    </a>
    <br>
    <img src="https://img.shields.io/github/license/waseemofficial/Allure_Reports_PyTest.svg?style=flat"/>
    <img src="https://img.shields.io/github/languages/top/waseemofficial/Allure_Reports_PyTest?style=flat"/>
    <img src="https://img.shields.io/github/stars/waseemofficial/Allure_Reports_PyTest.svg?colorB=orange&style=flat"/>
    <img src="https://img.shields.io/github/languages/code-size/waseemofficial/Allure_Reports_PyTest.svg?style=flat"/>
    <img src="https://img.shields.io/github/issues-raw/waseemofficial/Allure_Reports_PyTest.svg?style=flat"/>
  </div>
</p>

---

<div align="center">

### Languages
![Python](https://img.shields.io/badge/-Python-000?&logo=Python)
![Bash](https://img.shields.io/badge/-Bash-000?&logo=gnu-bash&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000?&logo=markdown)

### Technologies
![Docker](https://img.shields.io/badge/-Docker-000?&logo=Docker)
![Linux](https://img.shields.io/badge/-Linux-000?&logo=Linux)
![Node.js](https://img.shields.io/badge/-Node.js-000?&logo=node.js)
![Postman](https://img.shields.io/badge/-Postman-000?&logo=Postman)
![GitHub](https://img.shields.io/badge/-GitHub-000?&logo=GitHub)
![Selenium](https://img.shields.io/badge/-Selenium-000?&logo=Selenium)
![Regex](https://img.shields.io/badge/-Regex-000?&logo=Regex)
![GitHub Actions](https://img.shields.io/badge/-GithubActions-000?&logo=github-actions)

</div>

---

# 📊 Allure Reports in Selenium with Python and PyTest

![Allure Report](https://img.shields.io/endpoint?url=https://waseemofficial.github.io/Allure_Reports_PyTest/allure-report/badge.json)



## 📌 Overview
This repository demonstrates **Allure Reports** integration with **Selenium**, **Python**, and **PyTest** for generating rich, interactive test execution reports.  
Allure allows you to:
- Visualize test execution in a clean, interactive dashboard.
- Capture detailed test steps, logs, and screenshots.
- Improve debugging with structured reporting.

---

## ⚙️ Features
- ✅ **PyTest** as the test framework.
- ✅ **Selenium WebDriver** for browser automation.
- ✅ **Allure Report Integration** for detailed reporting.
- ✅ Supports **screenshots on failure**.
- ✅ Works with **GitHub Actions CI/CD**.

---

## 📂 Project Structure
```bash
Allure_Reports_PyTest/
│
├── tests/               # Test cases
├── pages/               # Page Object Models
├── utilities/           # Helpers and common methods
├── requirements.txt     # Python dependencies
├── pytest.ini           # PyTest configuration
└── README.md            # Project documentation
```
🚀 Installation & Setup
1️⃣ Clone the Repository

```bash
git clone https://github.com/waseemofficial/Allure_Reports_PyTest.git
cd Allure_Reports_PyTest
```

2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate     # Windows
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Install Allure Commandline

- Mac (brew):

```bash
brew install allure
```
- Windows (Scoop):

```bash
scoop install allure
```
- Linux (Manual): [Allure Installation Guide](https://docs.qameta.io/allure/)


🧪 Running Tests with Allure

Run tests and generate results:

```bash
pytest --alluredir=allure-results
```

Generate the HTML report:

```bash
allure serve allure-results
```

📸 Example Allure Report View

Allure Example

🔄 Continuous Integration

This project is configured to work with GitHub Actions to:

- Run tests automatically on push/PR.

- Publish Allure Reports as GitHub Pages.

📜 License

This project is licensed under the MIT License.
📬 Contact

Author: Syed Waseem

GitHub: waseemofficial

⭐ If you like this repository, don’t forget to star it and follow for more updates!