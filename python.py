#!/usr/bin/env python3

# Description:
# One-shot setup script for EC2 or Ubuntu machines that
# 1. Installs Zsh, Git, and Curl
# 2. Makes Zsh the permanent default shell
# 3. Installs Oh My Zsh and zsh-autosuggestions
# 4. Configures .zshrc automatically

import os
import subprocess
import shutil

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def install_prereqs():
    print("Installing prerequisites...")
    run("sudo apt update -y")
    run("sudo apt install -y zsh git curl")

def make_zsh_default():
    print("Setting Zsh as the default shell...")
    zsh_path = shutil.which("zsh")
    if not zsh_path:
        raise RuntimeError("Zsh not found even after install.")
    run(f"sudo usermod --shell {zsh_path} $USER")

def install_oh_my_zsh():
    home = os.path.expanduser("~")
    oh_my = os.path.join(home, ".oh-my-zsh")
    if not os.path.exists(oh_my):
        print("Installing Oh My Zsh...")
        run('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    else:
        print("Oh My Zsh already installed.")

def install_autosuggestions():
    print("Installing zsh-autosuggestions plugin...")
    plugin_dir = os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")
    if not os.path.exists(plugin_dir):
        run(f"git clone https://github.com/zsh-users/zsh-autosuggestions {plugin_dir}")
    else:
        print("zsh-autosuggestions already installed.")

def configure_zshrc():
    print("Configuring .zshrc...")
    zshrc_path = os.path.expanduser("~/.zshrc")
    lines = [
        'export ZSH="$HOME/.oh-my-zsh"',
        'ZSH_THEME="robbyrussell"',
        'plugins=(git zsh-autosuggestions)',
        'source $ZSH/oh-my-zsh.sh',
        'source ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh',
        "ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#777777'"
    ]
    with open(zshrc_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(".zshrc configured successfully.")

def main():
    print("🚀 Starting permanent Zsh + autosuggestions setup...")
    install_prereqs()
    make_zsh_default()
    install_oh_my_zsh()
    install_autosuggestions()
    configure_zshrc()
    print("----------------------------------------------------")
    print("✅ Setup complete!")
    print("💡 Log out and SSH back in — you’ll start in Zsh.")
    print("Hello from Shishir — your terminal is now smarter 😎")
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()
