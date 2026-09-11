import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk  
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- Cores do Tema Escuro ---
BG_MAIN = "#2b2b2b"      # Fundo principal
BG_CENTER = "#1e1e1e"    # Fundo do painel central
BG_INPUT = "#3c3f41"     # Fundo da caixa de texto
FG_TEXT = "#ffffff"      # Texto principal
FG_DIM = "#aaaaaa"       # Texto secundário/dicas
COLOR_GOLD = "#FFD700"   # Cor de destaque para o botão selecionado

# --- Tipografia ---
FONT_TITLE = ("Trebuchet MS", 12, "bold")
FONT_LABEL = ("Trebuchet MS", 10)
FONT_MONO = ("Consolas", 10, "bold") 

# --- Dados Base do PSO:BB ---
SECTION_IDS = {
    0: {"nome": "Viridia",    "cor": "#00AA00", "desc": "Focado em armas de tiro e Partisans."},
    1: {"nome": "Greenill",   "cor": "#88FF88", "desc": "Especializado em Rifles e armas de longo alcance."},
    2: {"nome": "Skyly",      "cor": "#00CCFF", "desc": "Especialista em Swords, sendo ótimo para Hunters."},
    3: {"nome": "Bluefull",   "cor": "#0033FF", "desc": "Focado em Partisans e Rods."},
    4: {"nome": "Purplenum",  "cor": "#AA00AA", "desc": "Especialista em Mechguns e ótimo para Rangers."},
    5: {"nome": "Pinkal",     "cor": "#FF66CC", "desc": "Focado em Wands e equipamentos para Forces."},
    6: {"nome": "Redria",     "cor": "#FF0000", "desc": "Versátil, com ótimas opções de equipamentos variados."},
    7: {"nome": "Oran",       "cor": "#FF6600", "desc": "Focado em Daggers e Wands."},
    8: {"nome": "Yellowboze", "cor": "#EEEE00", "desc": "Equilibrado, com distribuição uniforme de armas."},
    9: {"nome": "Whitill",    "cor": "#FFFFFF", "desc": "Especialista em Slicers e boas opções de Mechguns."}
}

# --- Dados Base das Classes ---
CLASSES_INFO = {
    "HUmar":     {"offset": 5, "cor": "#B32400", "img": "humar.png"},
    "HUnewearl": {"offset": 6, "cor": "#B32400", "img": "hunewearl.png"},
    "HUcast":    {"offset": 7, "cor": "#B32400", "img": "hucast.png"},
    "HUcaseal":  {"offset": 4, "cor": "#B32400", "img": "hucaseal.png"},
    "RAmar":     {"offset": 8, "cor": "#00802b", "img": "ramar.png"},
    "RAmarl":    {"offset": 6, "cor": "#00802b", "img": "ramarl.png"},
    "RAcast":    {"offset": 9, "cor": "#00802b", "img": "racast.png"},
    "RAcaseal":  {"offset": 0, "cor": "#00802b", "img": "racaseal.png"},
    "FOmar":     {"offset": 5, "cor": "#0033cc", "img": "fomar.png"},
    "FOmarl":    {"offset": 1, "cor": "#0033cc", "img": "fomarl.png"},
    "FOnewm":    {"offset": 2, "cor": "#0033cc", "img": "fonewm.png"},
    "FOnewearl": {"offset": 3, "cor": "#0033cc", "img": "fonewearl.png"}
}

# --- Funções ---
ICON_DIR = "icons"

def load_section_icons():
    images_list = []
    if not os.path.exists(ICON_DIR):
        print(f"[ERRO] A pasta '{ICON_DIR}' não foi encontrada.")
        return [None] * 10 
    
    for i in range(10):
        img_path = os.path.join(ICON_DIR, f"{i}.png")
        try:
            img = Image.open(img_path).convert("RGBA")
            datas = img.getdata()
            new_data = []
            for item in datas:
                if item[0] < 15 and item[1] < 15 and item[2] < 15:
                    new_data.append((0, 0, 0, 0)) 
                else:
                    new_data.append(item)
            img.putdata(new_data)
            
            img = img.resize((60, 60), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            images_list.append(tk_img)
        except Exception as e:
            print(f"[AVISO] Erro ao carregar {img_path}: {e}")
            images_list.append(None)

    return images_list

CLASS_DIR = "classes"

def load_class_images():
    class_images = {}
    if not os.path.exists(CLASS_DIR):
        print(f"[ERRO] A pasta '{CLASS_DIR}' não foi encontrada.")
        return {k: None for k in CLASSES_INFO.keys()}
    
    for c_name, c_info in CLASSES_INFO.items():
        img_path = os.path.join(CLASS_DIR, c_info["img"])
        try:
            img = Image.open(img_path).convert("RGBA")
            datas = img.getdata()
            new_data = []
            for item in datas:
                if item[0] > 230 and item[1] > 230 and item[2] > 230:
                    new_data.append((0, 0, 0, 0)) 
                else:
                    new_data.append(item)
            img.putdata(new_data)
            
            img = img.resize((45, 25), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            class_images[c_name] = tk_img
        except Exception as e:
            print(f"[AVISO] Erro ao carregar rosto {img_path}: {e}")
            class_images[c_name] = None
            
    return class_images

def calcular_section_id(event=None):
    nome = entry_nome.get()
    class_choice = selected_class.get()
    
    if not nome or nome == "":
        messagebox.showwarning("Aviso", "Por favor, digite o nome do personagem!")
        return

    class_offset = CLASSES_INFO[class_choice]["offset"]

    ascii_sum = sum(ord(c) for c in nome)
    indice = (ascii_sum + class_offset) % 10

    id_info = SECTION_IDS[indice]
    
    lbl_nome_id.config(text=id_info['nome'].upper(), fg=id_info['cor'])
    lbl_descricao.config(text=f"{id_info['nome']} - {id_info['desc']}")
    
    main_icon = loaded_icons[indice]
    if main_icon:
        lbl_main_icon.config(image=main_icon)
        lbl_main_icon.image = main_icon

# --- Configuração da Interface Gráfica ---
janela = tk.Tk()
janela.title("PSO:BB Section ID Calculator (Ephinea)")
janela.geometry("850x800")
janela.resizable(True, True)
janela.configure(bg=BG_MAIN) 

# --- Configuração do Ícone da Janela ---
try:
    # Usamos o Pillow para abrir a imagem (pode ser .png ou .ico)
    icon_img = Image.open(resource_path("icone.ico"))
    photo_icon = ImageTk.PhotoImage(icon_img)
    
    # O 'True' aplica o ícone na janela principal e em todas as subsequentes
    janela.iconphoto(True, photo_icon)
except Exception as e:
    print(f"[AVISO] Não foi possível carregar o ícone da janela: {e}")

loaded_icons = load_section_icons()

# --- Painel Esquerdo: Entrada de Dados ---
frame_input = tk.Frame(janela, bg=BG_MAIN, padx=20, pady=20)
frame_input.pack(side="left", fill="y")

tk.Label(frame_input, text="Character Name:", font=FONT_TITLE, bg=BG_MAIN, fg=FG_TEXT).pack(anchor="w")
entry_nome = tk.Entry(frame_input, font=FONT_LABEL, width=32, bg=BG_INPUT, fg=FG_TEXT, insertbackground=FG_TEXT)
entry_nome.pack(fill="x", pady=(5, 15))

tk.Label(frame_input, text="Select Class:", font=FONT_TITLE, bg=BG_MAIN, fg=FG_TEXT).pack(anchor="w", pady=(0, 5))

selected_class = tk.StringVar(value="HUmar") 
loaded_class_icons = load_class_images()     

frame_classes = tk.Frame(frame_input, bg=BG_MAIN)
frame_classes.pack(fill="x", pady=(0, 15))

# Dicionário para guardar os widgets dos botões de rádio e atualizar as cores
radio_widgets = {}

def update_radio_colors(*args):
    # Essa função é chamada sempre que a classe selecionada muda
    ativo = selected_class.get()
    for c_name, rb in radio_widgets.items():
        if c_name == ativo:
            rb.config(fg=COLOR_GOLD) # Texto dourado no selecionado
        else:
            rb.config(fg="white")    # Texto branco nos inativos

selected_class.trace_add("write", update_radio_colors)

# Variável para rastrear a categoria atual durante o loop
current_category = ""

for c_name, c_info in CLASSES_INFO.items():
    # --- Lógica de Separação de Categorias ---
    prefix = c_name[:2] # Pega as 2 primeiras letras (HU, RA, FO)
    
    if prefix != current_category:
        if current_category != "":
            # Adiciona um espaço vazio (frame invisível) antes da próxima categoria
            tk.Frame(frame_classes, bg=BG_MAIN, height=12).pack(fill="x")
        
        # Define o nome da categoria com base no prefixo
        if prefix == "HU":
            cat_name = "HUNTER"
        elif prefix == "RA":
            cat_name = "RANGER"
        else:
            cat_name = "FORCE"
            
        # Cria o texto do separador
        tk.Label(
            frame_classes, 
            text=cat_name, 
            font=("Trebuchet MS", 9, "bold"), 
            bg=BG_MAIN, 
            fg=FG_DIM, 
            anchor="w"
        ).pack(fill="x", pady=(0, 2))
        
        current_category = prefix
    # -----------------------------------------------

    nome_com_espacos = c_name.ljust(18) 
    
    rb = tk.Radiobutton(
        frame_classes,
        text=nome_com_espacos, 
        variable=selected_class,
        value=c_name,
        bg=c_info["cor"],
        fg="white" if c_name != selected_class.get() else COLOR_GOLD,
        selectcolor=c_info["cor"], 
        activebackground=c_info["cor"], 
        indicatoron=False,     
        compound="right",      
        font=FONT_MONO, 
        anchor="w",
        padx=10,
        pady=3,
        bd=1,
        relief="raised"
    )
    if loaded_class_icons[c_name]:
        rb.config(image=loaded_class_icons[c_name])
        
    rb.pack(fill="x", pady=1)
    radio_widgets[c_name] = rb

btn_calcular = tk.Button(
    frame_input, 
    text="CALCULATE", 
    command=calcular_section_id, 
    bg="#28a745", 
    fg="white", 
    activebackground="#218838",
    activeforeground="white",
    font=FONT_TITLE,
    borderwidth=0,
    pady=8
)
btn_calcular.pack(fill="x", pady=20)

tk.Label(frame_input, text="Ephinea Base - Modulo 10 logic.", font=("Trebuchet MS", 8, "italic"), bg=BG_MAIN, fg=FG_DIM).pack(side="bottom")

# --- Painel Direito: Galeria ---
frame_gallery = tk.Frame(janela, bg=BG_MAIN, padx=15, pady=15)
frame_gallery.pack(side="right", fill="y")

tk.Label(frame_gallery, text="All IDs Reference:", font=FONT_TITLE, bg=BG_MAIN, fg=FG_TEXT).pack(anchor="w", pady=(0, 10))

frame_grid = tk.Frame(frame_gallery, bg=BG_MAIN)
frame_grid.pack(fill="both", expand=True)

for i in range(10):
    row = i // 2
    col = i % 2
    
    cell_frame = tk.Frame(frame_grid, bg=BG_MAIN, padx=5, pady=5)
    cell_frame.grid(row=row, column=col)
    
    gallery_icon = loaded_icons[i]
    if gallery_icon:
        small_img = ImageTk.getimage(gallery_icon).resize((30, 30), Image.Resampling.LANCZOS)
        tk_small_img = ImageTk.PhotoImage(small_img)
        
        lbl_img_ref = tk.Label(cell_frame, image=tk_small_img, bg=BG_MAIN, bd=0, highlightthickness=0)
        lbl_img_ref.image = tk_small_img
        lbl_img_ref.pack()

    id_name = SECTION_IDS[i]['nome']
    id_color = SECTION_IDS[i]['cor']
    tk.Label(cell_frame, text=f"{id_name} ({i})", font=("Trebuchet MS", 8, "bold"), bg=BG_MAIN, fg=id_color).pack()

# --- Painel Central: Resultado (Information Box) ---
# 1. Container invisível para dar margem
frame_center_container = tk.Frame(janela, bg=BG_MAIN, padx=20, pady=30)
frame_center_container.pack(side="left", fill="both", expand=True)

# 2. A "Moldura" (Information Box)
frame_result = tk.Frame(
    frame_center_container, 
    bg=BG_CENTER, 
    bd=4,                 # Borda interna 3D
    relief="ridge",       # Estilo da borda
    highlightthickness=2, # Espessura da borda externa
    highlightbackground="#00CCCC" # Cor da borda externa (Ciano)
)
frame_result.pack(fill="both", expand=True, pady=(40, 40)) # Margens verticais para centralizar

# 3. Barra de título "Information" (Estilo PSO)
lbl_info_title = tk.Label(
    frame_result, 
    text="  Information  ", 
    font=("Trebuchet MS", 11, "bold", "italic"), 
    bg="#B32400", 
    fg="white",
    anchor="w"
)
lbl_info_title.pack(fill="x")

# 4. Conteúdo da Caixa
lbl_titulo_id = tk.Label(frame_result, text="YOUR SECTION ID:", font=("Trebuchet MS", 12, "bold"), bg=BG_CENTER, fg=FG_TEXT)
lbl_titulo_id.pack(pady=(30, 0))

lbl_nome_id = tk.Label(frame_result, text="-", font=("Trebuchet MS", 22, "bold"), bg=BG_CENTER, fg=FG_TEXT)
lbl_nome_id.pack(pady=(0, 20))

lbl_main_icon = tk.Label(frame_result, bg=BG_CENTER)
lbl_main_icon.pack(pady=10)

lbl_descricao = tk.Label(
    frame_result, 
    text="Digite o nome e escolha a classe ao lado\npara calcular o seu Section ID.", 
    font=("Trebuchet MS", 10, "italic"), 
    bg=BG_CENTER, 
    fg=FG_DIM,
    wraplength=280, 
    justify="center"
)
lbl_descricao.pack(pady=20)

# --- Atalho do Teclado ---
janela.bind('<Return>', calcular_section_id)

janela.mainloop()