# -*- coding: utf-8 -*-
"""
Gera um PDF a partir de um HTML usando um navegador Chromium headless.
Generate a PDF from an HTML file using a headless Chromium browser.

Uso / Usage:
    python scripts/gerar_pdf.py <entrada.html> <saida.pdf>

Detecta Chrome/Edge/Chromium em Windows, macOS e Linux automaticamente.
Auto-detects Chrome/Edge/Chromium on Windows, macOS and Linux.
"""
import os
import shutil
import subprocess
import sys


def find_browser():
    # 1) Procura no PATH / Look in PATH
    for name in ("google-chrome", "google-chrome-stable", "chromium",
                 "chromium-browser", "chrome", "msedge", "microsoft-edge"):
        path = shutil.which(name)
        if path:
            return path
    # 2) Caminhos comuns por SO / Common per-OS locations
    candidates = [
        # Windows
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        # macOS
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        # Linux
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def main():
    if len(sys.argv) != 3:
        print("Uso / Usage: python scripts/gerar_pdf.py <entrada.html> <saida.pdf>")
        sys.exit(1)

    html_in = os.path.abspath(sys.argv[1])
    pdf_out = os.path.abspath(sys.argv[2])

    if not os.path.exists(html_in):
        print("HTML nao encontrado / HTML not found:", html_in)
        sys.exit(1)

    browser = find_browser()
    if not browser:
        print("Navegador Chromium nao encontrado. Instale Chrome ou Edge.")
        print("Chromium browser not found. Please install Chrome or Edge.")
        sys.exit(1)

    file_url = "file:///" + html_in.replace("\\", "/")
    cmd = [
        browser, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        "--print-to-pdf=" + pdf_out, file_url,
    ]
    subprocess.run(cmd, check=False)

    if os.path.exists(pdf_out):
        print("OK PDF:", pdf_out, "(", os.path.getsize(pdf_out), "bytes )")
    else:
        print("Falha ao gerar o PDF / Failed to generate the PDF.")
        sys.exit(1)


if __name__ == "__main__":
    main()
