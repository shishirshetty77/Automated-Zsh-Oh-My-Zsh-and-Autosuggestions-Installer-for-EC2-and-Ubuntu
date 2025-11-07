# 🌀 Zsh Auto Setup
### _Automated Zsh, Oh My Zsh, and Autosuggestions Installer for EC2 & Ubuntu_

This repository contains a one-shot Python automation script that installs and configures **Zsh** with **Oh My Zsh**, **zsh-autosuggestions**, and **persistent shell settings**.  
It’s built for developers who frequently create new servers (like EC2 instances) and want their terminal to look and behave like macOS — complete with inline command suggestions and a smart shell prompt.  

---

## 🚀 Features

- 🧩 Installs **Zsh**, **Git**, and **Curl**
- ⚙️ Installs **Oh My Zsh** automatically
- 💡 Enables **zsh-autosuggestions** plugin (gray inline typing hints)
- 🧠 Configures `.zshrc` automatically
- 🔁 Makes **Zsh the permanent default shell**
- 🧰 Works seamlessly on **AWS EC2**, **GCP**, and **Ubuntu**
- 👋 Includes a “Hello from Shishir” completion message

---

## 🧠 Prerequisites
- Ubuntu / Debian-based system (EC2 or local)
- `sudo` access
- Python 3 installed (the script will install it if missing)

---

## ⚙️ Setup Instructions

### 🧩 Step 1 — Clone this Repository
```bash
git clone https://github.com/<your-username>/zsh-auto-setup.git
cd zsh-auto-setup
```

### 🧩 Step 2 — Run the Python Script
```bash
sudo apt update -y && sudo apt install -y python3
sudo python3 setup_zsh_auto.py
```

### 🧩 Step 3 — Log out and log back in
```bash
exit
ssh -i your-key.pem ubuntu@<your-ec2-ip>
```

Then verify:
```bash
echo $SHELL
```
✅ Output should show `/usr/bin/zsh`

Now type a command you’ve used before:
```bash
upt
```
…and you’ll see:
```
uptime
```
in **gray** — press **→** to accept the suggestion.

---

## 🧰 Manual Installation (If You Don’t Want to Run Python Script)

If you prefer manual setup, run these two commands in your terminal:

### **1️⃣ Make Zsh Permanent**
```bash
sudo apt install -y zsh && \
sudo usermod --shell /usr/bin/zsh $USER && \
echo '[ -z "$ZSH_VERSION" ] && exec /usr/bin/zsh' >> ~/.bash_profile && \
echo "✅ Zsh is now your permanent login shell! Log out and SSH back in."
```

### **2️⃣ Install Oh My Zsh and Autosuggestions**
```bash
sudo apt update -y && sudo apt install -y zsh git curl && \
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended && \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions)/' ~/.zshrc && \
echo "source ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc && \
echo "ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#777777'" >> ~/.zshrc && \
sudo usermod --shell $(which zsh) $USER && \
echo '[ -z "$ZSH_VERSION" ] && exec $(which zsh)' >> ~/.bash_profile && \
echo "✅ Zsh + autosuggestions installed! Logout and SSH back in, and you’ll start in Zsh with gray inline suggestions."
```

---

## 🧩 Verification
After logging back in:
```bash
echo $SHELL
```
✅ Should show `/usr/bin/zsh`

Try typing:
```bash
upt
```
→ should display `uptime` in **gray** (press → to accept).

---
