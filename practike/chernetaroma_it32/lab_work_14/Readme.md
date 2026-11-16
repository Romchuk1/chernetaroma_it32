PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> & "$env:APPDATA\uv\python\cpython-3.14.7-windows-x86_64-none\python.exe" -m venv .venv
PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> .\.venv\Scripts\Activate.ps1
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> where.exe python
C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14\.venv\Scripts\python.exe
C:\Users\2024.cherneta.roman_\AppData\Local\Microsoft\WindowsApps\python.exe
C:\Users\2024.cherneta.roman_\AppData\Roaming\uv\python\cpython-3.14.7-windows-x86_64-none\python.exe
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> python -c "import sys; print(sys.prefix)"
C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14\.venv
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> pip list
ERROR: unknown command "C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14\.venv\Scripts\pip.exe"
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> deactivate
PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> .\.venv\Scripts\Activate.ps1
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> python -m pip --version
pip 26.2.1 from C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14\.venv\Lib\site-packages\pip (python 3.14)
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> python -m pip list
Package Version
------- -------
pip     26.2.1
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> deactivate
PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> .\.venv\Scripts\Activate.ps1
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> python -m pip install tabulate
Collecting tabulate
  Downloading tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
Downloading tabulate-0.10.0-py3-none-any.whl (39 kB)
Installing collected packages: tabulate
Successfully installed tabulate-0.10.0

[notice] A new release of pip is available: 26.2.1 -> 26.3
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> python task2.py
Roman Cherneta, IT-32
| category   |   count |   total |
|------------|---------|---------|
| food       |       3 |  530.00 |
| fun        |       2 |  370.00 |
| transport  |       2 |   90.00 |
| TOTAL      |       7 |  990.00 |
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> deactivate
PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> .\.venv\Scripts\Activate.ps1
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> python -m pip install "qrcode[pil]"
Collecting qrcode[pil]
  Downloading qrcode-8.2-py3-none-any.whl.metadata (17 kB)
Collecting colorama (from qrcode[pil])
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting pillow>=9.1.0 (from qrcode[pil])
  Downloading pillow-13.0.0-cp314-cp314-win_amd64.whl.metadata (9.3 kB)
Downloading qrcode-8.2-py3-none-any.whl (45 kB)
Downloading pillow-13.0.0-cp314-cp314-win_amd64.whl (7.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.3/7.3 MB 549.8 kB/s  0:00:13
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: pillow, colorama, qrcode
Successfully installed colorama-0.4.6 pillow-13.0.0 qrcode-8.2

[notice] A new release of pip is available: 26.2.1 -> 26.3
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> python task3.py
Roman Cherneta, IT-32
saved: contact.png
(.venv) PS C:\Users\2024.cherneta.roman_\chernetaroma_it32\practike\chernetaroma_it32\lab_work_14> 