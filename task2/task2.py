import random
import smtplib
import tkinter as tk
from tkinter import messagebox

# function to send OTP via email
def send_otp(email):
    # connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # replace with your own Gmail account credentials
    email_address = 'amankumarjc@gmail.com'
    email_password = 'wedjoehumsqqxtcl'
    server.login(email_address, email_password)
    # generate a 6-digit OTP and send it via email
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
    message = f'Your OTP is {otp}'
    server.sendmail(email_address, email, message)
    server.quit()
    # return the generated OTP
    return otp

# function to verify the OTP
def verify_otp():
    email = email_entry.get()
    # send OTP via email
    otp = send_otp(email)
    # get user input for OTP and verify it
    user_input = otp_entry.get()
    if user_input == otp:
        messagebox.showinfo("OTP Verification", "OTP verified successfully!")
        otp_entry.delete(0, tk.END)  # Clear the entry widget after successful verification
    else:
        messagebox.showerror("OTP Verification", "Invalid OTP, please try again.")

# Create the main application window
app = tk.Tk()
app.title("OTP Verification")
app.geometry("300x200")

# Create the widgets
email_label = tk.Label(app, text="Enter your email address:")
email_label.pack()
email_entry = tk.Entry(app)
email_entry.pack()

otp_label = tk.Label(app, text="Enter the OTP sent to your email:")
otp_label.pack()
otp_entry = tk.Entry(app)
otp_entry.pack()

verify_btn = tk.Button(app, text="Verify OTP", command=verify_otp)
verify_btn.pack()

# Start the main event loop
app.mainloop()

