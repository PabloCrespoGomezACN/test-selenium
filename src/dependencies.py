import subprocess

# Install required system packages
subprocess.run(["apt-get", "update"])
subprocess.run(["apt-get", "install", "-y", "wget"])

# Download and install Google Chrome
subprocess.run(["wget", "--no-check-certificate", "https://dl.google.com/linux/linux_signing_key.pub"])
subprocess.run(["apt-key", "add", "linux_signing_key.pub"])
with open("/etc/apt/sources.list.d/google-chrome.list", "a") as sources_list:
    sources_list.write("deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\n")
subprocess.run(["apt-get", "update"])
subprocess.run(["apt-get", "install", "-y", "google-chrome-stable"])

# Install Python dependencies
subprocess.run(["pip", "install", "--upgrade", "pip"])
# subprocess.run(["pip", "install", "selenium"])
