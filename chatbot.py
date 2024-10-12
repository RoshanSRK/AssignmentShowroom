import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import subprocess

# Define chatbot response logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    elif "display database" in user_input:
        return "Fetching database records..."
    elif "remind customers" in user_input:
        return "Sending reminders to customers..."
    else:
        return "I'm sorry, I don't understand that."

def remind_customers(window):
    try:
        # Run the UiPath process after minimizing the window
        uipath_workflow_path = r"D:\rsrko\Documents\UiPath\Assignment Showroom\Main.xaml"
        subprocess.run([r"C:\Program Files\UiPath\Studio\UiRobot.exe", "-file", uipath_workflow_path], check=True)

        # Show success message
        messagebox.showinfo("UiPath Workflow", "UiPath workflow has been triggered!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to start UiPath workflow: {e}")
    finally:
        # Restore and bring the window to the front after the process is complete
        window.state('normal')  # Restore the window
        window.lift()  # Bring the window to the front
        window.focus_force()  # Ensure it gets focus


# Function to handle "Remind Customers" logic
def handle_remind_customers():
    # Display the bot response before triggering the reminder
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "Bot: Sending reminders to customers...\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    # Wait 2 seconds before minimizing and starting the process
    window.after(2000, lambda: minimize_and_remind())

def minimize_and_remind():
    # Minimize the window before running the UiPath process
    window.iconify()

    # Call the function to trigger the UiPath workflow
    remind_customers(window)

# Create the GUI window
def create_chatbot_gui():
    global window, chat_area  # Declare window and chat_area as global to be used in other functions
    # Create main window
    window = tk.Tk()
    window.title("Chatbot")

    # Create the chat area with scroll
    chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=20, width=50)
    chat_area.pack(padx=10, pady=10)
    chat_area.config(state=tk.DISABLED)

    # Initial greeting from the bot
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "Bot: Hi! How can I assist you today?\n\n")
    chat_area.config(state=tk.DISABLED)

    # Create the input field
    input_field = tk.Entry(window, width=40)
    input_field.pack(padx=10, pady=10, side=tk.LEFT)

    # Function to send user input and get a response from the bot
    def send_message(user_input=None):
        if user_input is None:
            user_input = input_field.get()  # Get input from the entry field
        if user_input.strip() == "":
            return
        
        # Add user message to the chat
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        chat_area.config(state=tk.DISABLED)

        # Get bot response
        bot_response = get_bot_response(user_input)

        # Add bot response to the chat
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n")
        chat_area.config(state=tk.DISABLED)

        # Scroll to the end of the chat
        chat_area.yview(tk.END)

        # Clear input field
        input_field.delete(0, tk.END)  # Always clear the input field after sending

        # Check if the user said "bye"
        if "bye" in user_input.lower():
            window.after(2000, window.destroy)  # Close the window after 2 seconds

        # If the user types "remind customers", trigger the reminder logic
        if "remind customers" in user_input.lower():
            handle_remind_customers()

    # Function to send predefined messages from buttons
    def send_command_message(command):
        send_message(command)

    # Create the send button
    send_button = tk.Button(window, text="Send", command=lambda: send_message())
    send_button.pack(padx=10, pady=10, side=tk.LEFT)

    # Bind the Enter key to send messages
    window.bind('<Return>', lambda event: send_message())

    # Create "Display Database" button
    # display_db_button = tk.Button(window, text="Display Database", command=lambda: send_command_message("Display Database"))
    # display_db_button.pack(padx=10, pady=10, side=tk.LEFT)

    # Create "Remind Customers" button
    remind_customers_button = tk.Button(window, text="Remind Customers", command=lambda: handle_remind_customers())
    remind_customers_button.pack(padx=10, pady=10, side=tk.LEFT)

    # Start the GUI event loop
    window.mainloop()

# Run the chatbot GUI
if __name__ == "__main__":
    create_chatbot_gui()
