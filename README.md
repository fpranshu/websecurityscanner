# WebSecurityScanner

WebSecurityScanner is a Python-based tool designed to help you identify and mitigate security vulnerabilities in your web applications. It performs a thorough scan of your web application, checking for common security issues and providing detailed reports to help you secure your application.

## Features

- **Automated Scanning:** Automatically scans your web application for common security vulnerabilities.
- **Detailed Reports:** Generates detailed reports with information about identified vulnerabilities and suggested fixes.
- **Customizable:** Easily configurable to suit your specific security needs.
- **Easy to Use:** Simple command-line interface for quick and easy scans.

## 🛠 Prerequisites

Before running the tool, ensure you have the following installed:

- Python 3.8+  
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `tkinter` (comes with Python)

## Installation

To install WebSecurityScanner, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/fpranshu/websecurityscanner.git
    cd websecurityscanner
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run a scan on your web application, use the following command:

```bash
python scan.py --url <URL>

### **Using the GUI**
- **Enter the target URL** in the input box.  
- **Click the "Analyze Links" button** to start scanning.  
- **View the results**, which include:  
  - ✅ **HTTP status codes** for each link.  
  - ⚠️ **Detection of unsafe and obsolete attributes.**  
