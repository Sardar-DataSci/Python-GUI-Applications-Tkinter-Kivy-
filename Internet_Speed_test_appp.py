import tkinter as tk
import Internet_speed_test
import threading

# ---------------- SPEED TEST FUNCTION ----------------

def run_speed_test():
    try:
        st = Internet_speed_test.Speedtest()
        st.get_best_server()

        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000

        download_value.config(text=f"{download:.2f} Mbps")
        upload_value.config(text=f"{upload:.2f} Mbps")

    except Exception as e:
        download_value.config(text="Failed")
        upload_value.config(text="Failed")

# Thread wrapper (VERY IMPORTANT)
def check_speed():
    download_value.config(text="Testing...")
    upload_value.config(text="Testing...")
    thread = threading.Thread(target=run_speed_test)
    thread.start()

# ---------------- UI ----------------

app = tk.Tk()
app.title("Speed Test")
app.geometry("460x520")
app.config(bg="#0b132b")

title = tk.Label(
    app,
    text="SPEED TEST",
    font=("Helvetica", 26, "bold"),
    fg="white",
    bg="#0b132b"
)
title.pack(pady=25)

# ---------------- DOWNLOAD ----------------

download_box = tk.Frame(app, bg="#1c2541", width=380, height=110)
download_box.pack(pady=15)
download_box.pack_propagate(False)

tk.Label(
    download_box,
    text="DOWNLOAD",
    font=("Helvetica", 14),
    fg="#5bc0be",
    bg="#1c2541"
).pack(pady=10)

download_value = tk.Label(
    download_box,
    text="0.00 Mbps",
    font=("Helvetica", 22, "bold"),
    fg="white",
    bg="#1c2541"
)
download_value.pack()

# ---------------- UPLOAD ----------------

upload_box = tk.Frame(app, bg="#1c2541", width=380, height=110)
upload_box.pack(pady=15)
upload_box.pack_propagate(False)

tk.Label(
    upload_box,
    text="UPLOAD",
    font=("Helvetica", 14),
    fg="#5bc0be",
    bg="#1c2541"
).pack(pady=10)

upload_value = tk.Label(
    upload_box,
    text="0.00 Mbps",
    font=("Helvetica", 22, "bold"),
    fg="white",
    bg="#1c2541"
)
upload_value.pack()

# ---------------- BUTTON ----------------

check_btn = tk.Button(
    app,
    text="GO",
    font=("Helvetica", 18, "bold"),
    bg="#5bc0be",
    fg="#0b132b",
    activebackground="#3aa7a3",
    width=10,
    height=2,
    bd=0,
    command=check_speed
)
check_btn.pack(pady=35)

app.mainloop()


