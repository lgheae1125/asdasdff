import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("1400x800")

header = tk.Frame(root, width=1400, height=60, background="#ffffff")
mapArea = tk.Frame(root, width=960, height=340, background="#ffffff")
listArea = tk.Frame(root, width=960, height=340, background="#ffffff")
infoArea = tk.Frame(root, width=380, height=700, background="#ffffff")

imgSizes = []

for i in range (5):
  width = 960
  height = 960
  r = (width - 960) / 2
  t = (header - 340) / 2
  l = r + 960
  b = t + 340

n = 0 # +버튼을 누르면 n이 증감함

map_img = Image.open("map.png")
map_img = map_img.resize((imgSizes[n]['width'], imgSizes[n]['height']))
map_img = map_img.crop((imgSizes[n]['r'],imgSizes[n]['t'],imgSizes[n]['l'],imgSizes[n]['b']))

map_img = ImageTk.PhotoImage(map_img)

width = 960

map = tk.Label(mapArea, image=map_img, width=width)
map.place(x=0, y=0)

header.place(x=0, y=0)
mapArea.place(x=20, y=80)
listArea.place(x=20, y=440)
infoArea.place(x=1000, y=80)

root.mainloop()