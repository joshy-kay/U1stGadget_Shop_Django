# Setup (Windows PowerShell)

1. Create and activate venv

```powershell
py -m venv .venv
. .venv\Scripts\Activate.ps1
```

2. Upgrade packaging tools and install deps

```powershell
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

3. If Pillow build fails

- Try a binary-only install:

```powershell
pip install --only-binary=:all: Pillow==10.4.0
```

- If compilation errors persist, install "Build Tools for Visual Studio" (Desktop development with C++) and re-run step 2.

4. Open project in VS Code

```powershell
code .
```

Notes: If your system uses `python` instead of `py`, replace `py` with `python` in the commands above. If `code` isn't on your PATH, open VS Code and use File → Open Folder.
