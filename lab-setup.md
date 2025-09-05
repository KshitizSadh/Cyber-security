

# Penetration Testing Lab Setup

This guide documents my penetration testing lab environment using **Kali Linux** (on VirtualBox) and **Websploit Labs** for practicing ethical hacking and security testing.

---

## 🖥️ System Requirements

- **Host Machine**
  - CPU: 4+ cores recommended
  - RAM: 8 GB minimum (16 GB preferred)
  - Storage: 100 GB free space
  - Virtualization enabled in BIOS

- **Software**
  - [VirtualBox](https://www.virtualbox.org/)
  - [Kali Linux ISO / VM Image](https://www.kali.org/get-kali/)
  - [Websploit Labs](https://websploit.org/) (preconfigured vulnerable labs)

---

## ⚙️ VirtualBox Setup

1. **Install VirtualBox**  
   Download and install VirtualBox on your host machine.

2. **Import / Create Kali VM**
   - Use the Kali Linux ISO or pre-built VM.
   - Recommended settings:
     - **RAM:** 4 GB+
     - **CPU:** 2 cores+
     - **Networking:** Bridged Adapter / NAT (depending on lab setup)

3. **Update Kali Linux**
   ```bash
   sudo apt update && sudo apt full-upgrade -y


4. **Install Guest Additions (Optional)**
   For better display, clipboard, and performance.

   <img width="480" height="470" alt="image" src="https://github.com/user-attachments/assets/37e6258b-0764-4adf-95ba-ba075b184b25" />


---

## 🔧 Installing Websploit Labs

<img width="656" height="453" alt="image" src="https://github.com/user-attachments/assets/d6b479bc-acfd-41fc-928d-ed559a4cbf72" />

1. **Download Websploit Labs**

   ```bash
   git clone https://github.com/websploit/websploit-labs.git
   cd websploit-labs
   ```

2. **Run the Installer**

   ```bash
   sudo ./install.sh
   ```

3. **Verify Installation**

   ```bash
   websploit-labs --list
   ```

---

## 🧪 Running Vulnerable Labs

1. **Start a Lab**

   ```bash
   websploit-labs --start <lab_name>
   ```

2. **Check Running Services**

   ```bash
   docker ps
   ```

3. **Access the Lab**

   * Open your browser in Kali.
   * Navigate to the lab’s URL (e.g., `http://127.0.0.1:8080`).

---

## 📂 Useful Notes

* Labs are containerized (using Docker).

* You can stop labs anytime:

  ```bash
  websploit-labs --stop <lab_name>
  ```

* To stop all labs:

  ```bash
  docker stop $(docker ps -aq)
  ```

---

## 🔒 Disclaimer

This setup is **for educational purposes only**.
Do **not** use these tools or techniques on systems you do not own or have explicit permission to test.

---




