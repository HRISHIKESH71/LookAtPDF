def generate_pdf():
    folder = folder_var.get()
    base_filename = filename_var.get().strip()
    if not folder:
        messagebox.showwarning("Missing Folder", "Please select a folder.")
        return
    if not base_filename:
        messagebox.showwarning("Missing Filename", "Please enter a base filename.")
        return
    try:
        result = convert_images_to_pdf(folder, base_filename)
        status_label.config(text=result, fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")
