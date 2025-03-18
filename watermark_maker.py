import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Adder")
        self.root.geometry("600x500")
        
        # UI Elements
        self.label = tk.Label(root, text="Upload an image to add a watermark", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)
        
        self.canvas = tk.Canvas(root, width=500, height=300)
        self.canvas.pack()
        
        self.watermark_text = tk.Entry(root, width=40)
        self.watermark_text.insert(0, "Your Watermark Here")
        self.watermark_text.pack(pady=5)
        
        self.add_watermark_btn = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_btn.pack(pady=5)
        
        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_btn.pack(pady=5) 
        
        self.image_path = None
        self.img = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            self.image_path = file_path
            self.img = Image.open(file_path)
            self.display_image()
    
    def display_image(self):
        self.img.thumbnail((500, 300))
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(250, 150, image=self.tk_img)
    
    def add_watermark(self):
        if self.img is None:
            messagebox.showerror("Error", "Please upload an image first.")
            return
        
        watermark_text = self.watermark_text.get()
        image = self.img.copy()
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        width, height = image.size
        
        # Get text size using text b box instead of text size
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Position watermark at the bottom right
        position = (width - text_width - 10, height - text_height - 10)
        draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)
        
        self.img = image
        self.display_image()
        self.save_btn.config(state=tk.NORMAL)
    
    def save_image(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
        if save_path:
            self.img.save(save_path)
            messagebox.showinfo("Success", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()