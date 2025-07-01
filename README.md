# NetScope

**NetScope** is a simple, lightweight tool that helps you detect the CIDR block and IP class of any given IP address.

---

## 📌 Features

- ✅ Detects CIDR notation for IPv4 addresses
- ✅ Identifies traditional IP address classes (A, B, C, D, E)
- ✅ Simple to use, lightweight, and easy to integrate
- ✅ Great for learning, quick lookups, or network tools

---

## 🔧 How It Works

NetScope analyzes any IPv4 address:
- Checks which range the address falls into
- Determines its network class (based on legacy classful networking)
- Calculates the CIDR block representation if needed
- Outputs the results in a clear, human-friendly format

---

## 🚀 Usage

**Example**

bash
# Example usage
python netscope.py 192.168.1.1


Expected output:

IP Address: 192.168.1.1
Class: C
CIDR: 192.168.1.0/24

Installation:
git clone https://github.com/Sazz28/NetScope.git
cd NetScope



