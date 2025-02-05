# Web Security Scanner

A lightweight tool to analyze the security of your web applications by scanning links and detecting unsafe or obsolete attributes.

---

## Features

- Scans web applications for insecure links.
- Detects outdated and unsafe attributes in the web pages.
- Displays HTTP status codes for all scanned links.
- User-friendly GUI for seamless interaction.

---

## Installation

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

---

## Usage

### Command-Line Usage

To run a scan on your web application, use the following command:

```bash
python scan.py --url <URL>
```

### Using the GUI

1. **Enter the target URL** in the input box.
2. **Click the "Analyze Links" button** to start scanning.
3. **View the results**, which include:
   - **HTTP status codes** for each link.
   - **Detection of unsafe and obsolete attributes.**

---

## Output

### Sample Command-Line Output

```plaintext
[INFO] Starting scan for https://example.com
[INFO] Found 10 links.
[OK] Link: https://example.com/home - Status: 200
[WARNING] Link: https://example.com/login - Obsolete attribute detected
[ERROR] Link: https://example.com/about - Status: 404
```

### Sample GUI Output

- A table listing all links, their HTTP status codes, and warnings for unsafe attributes.
- Indicators such as:
  - ✅ Safe links
  - ⚠️ Warnings for unsafe attributes
  - ❌ Broken links

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contact

For any issues or suggestions, please reach out via GitHub Issues or email me at pranshumongia@gmail.com .
