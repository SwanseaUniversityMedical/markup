from django.shortcuts import render, redirect
from django.urls import reverse
import tkinter as tk
from tkinter import filedialog
import time

def file_selection_template(request):
    if request.method == 'GET':
        if request.GET.get('open_file_button'):
            root = tk.Tk()
            root.withdraw()
            # TO-DO: Fix "main thread is not in main loop" error
            # and "unable to create widget ".!frameX"" error
            file_path = filedialog.askopenfilename()
            if file_path != '()' and len(file_path) != 0:
                return redirect('/annotate' + file_path)
            else:
                return redirect('/')
        elif request.GET.get('open_dir_button'):
            root = tk.Tk()
            root.withdraw()
            # TO-DO: Fix "main thread is not in main loop" error
            dir_path = filedialog.askdirectory()
            if dir_path != '()' and len(dir_path) != 0:
                return redirect('/annotate' + dir_path)
            else:
                return redirect('/')
    return render(request, 'file_selection/index.html', {})