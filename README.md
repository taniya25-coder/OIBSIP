# 💬 Python Real-Time Chat Application (OIBSIP)

A real-time, bidirectional command-line chat application built using Python sockets, threading, and datetime modules. This project is developed as part of the Oasis Infobyte Python Development Internship.

---

## 🚀 Features
* **Single-File Execution:** Integrated server and client logic using Python multi-threading for easy setup and testing.
* **Real-time Bidirectional Messaging:** Instant message exchange between connected users on localhost.
* **Timestamp Prefix:** Every message automatically includes a timestamp in the format `[HH:MM] Username: Message`.
* **Graceful Disconnection:** Handles client disconnections smoothly and notifies participants when someone leaves.
* **Localhost Support:** Fully runnable on a single machine using `127.0.0.1`.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Modules Used:** `socket`, `threading`, `datetime`

---

## ⚙️ How to Run the Application

1. **Prerequisites:** Make sure you have Python installed on your system.
2. **Save the Code:** Save the provided code into a file named **`chat.py`**.
3. **Open Terminals:** Open **two separate command prompt / terminal windows** on your computer.
4. **Run the Script:** In *both* terminals, run the following command:
   ```bash
   python chat.py
