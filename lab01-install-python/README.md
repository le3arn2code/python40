# Lab 1 – Installing Python & Environment Setup

## 🎯 Objectives
- Understand and perform the installation process of Python 3.
- Set up an appropriate development environment for Python using IDEs or editors.
- Verify the Python installation to ensure the environment is correctly configured.

## 📋 Prerequisites
- A computer with internet access.
- Basic understanding of using terminal or command line interfaces.

## 🛠️ Tasks

### Task 1: Download and Install Python 3
- Windows: Run installer, check “Add Python to PATH”.
- macOS: Install from `.pkg`.
- Linux:
```bash
sudo apt-get update
sudo apt-get install -y python3
```

### Task 2: Verify Installation
```bash
python3 --version
```

### Task 3: Install IDE or Text Editor
- VS Code: Install + Python extension.
- PyCharm: Install Community Edition.

## ⚠️ Issues Encountered
1. **APT lock error** → Caused by unattended-upgrades. Fixed by killing PID, removing lock files, reconfiguring dpkg.
2. **Expired Puppet GPG Key** → Fixed by removing Puppet repo or re-importing GPG key.
3. **Software mismatch** → Fixed using `dpkg --configure -a` and `apt --fix-broken install`.

## ✅ Conclusion
- Python 3 installed and verified.
- IDE set up (VS Code / PyCharm).
- Issues resolved successfully.
