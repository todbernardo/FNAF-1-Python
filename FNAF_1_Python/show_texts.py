import sys
import time

def clear_console():
    print("\033[H\033[2J")

def show_title():
    clear_console()
    print('''
███████╗██╗██╗   ██╗███████╗    ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███████╗     █████╗ ████████╗    ███████╗██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝██║██║   ██║██╔════╝    ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝██╔════╝    ██╔══██╗╚══██╔══╝    ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
█████╗  ██║██║   ██║█████╗      ██╔██╗ ██║██║██║  ███╗███████║   ██║   ███████╗    ███████║   ██║       █████╗  ██████╔╝█████╗  ██║  ██║██║  ██║ ╚████╔╝ ███████╗
██╔══╝  ██║╚██╗ ██╔╝██╔══╝      ██║╚██╗██║██║██║   ██║██╔══██║   ██║   ╚════██║    ██╔══██║   ██║       ██╔══╝  ██╔══██╗██╔══╝  ██║  ██║██║  ██║  ╚██╔╝  ╚════██║
██║     ██║ ╚████╔╝ ███████╗    ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ███████║    ██║  ██║   ██║       ██║     ██║  ██║███████╗██████╔╝██████╔╝   ██║   ███████║
╚═╝     ╚═╝  ╚═══╝  ╚══════╝    ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝    ╚═╝   ╚══════╝
''')
    
def show_nights(night):
    clear_console()

    match night:
        case 1:
            print('''                                                                             
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗     ██╗
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝    ███║
██╔██╗ ██║██║██║  ███╗███████║   ██║       ╚██║
██║╚██╗██║██║██║   ██║██╔══██║   ██║        ██║
██║ ╚████║██║╚██████╔╝██║  ██║   ██║        ██║
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═╝                                                            
            ''')
        case 2:
            print('''                
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗    ██████╗ 
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝    ╚════██╗
██╔██╗ ██║██║██║  ███╗███████║   ██║        █████╔╝
██║╚██╗██║██║██║   ██║██╔══██║   ██║       ██╔═══╝ 
██║ ╚████║██║╚██████╔╝██║  ██║   ██║       ███████╗
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝                   
            ''')
        case 3:
            print('''                                        
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗    ██████╗ 
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝    ╚════██╗
██╔██╗ ██║██║██║  ███╗███████║   ██║        █████╔╝
██║╚██╗██║██║██║   ██║██╔══██║   ██║        ╚═══██╗
██║ ╚████║██║╚██████╔╝██║  ██║   ██║       ██████╔╝
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═════╝                          
            ''')
        case 4:
            print('''                           
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗    ██╗  ██╗
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝    ██║  ██║
██╔██╗ ██║██║██║  ███╗███████║   ██║       ███████║
██║╚██╗██║██║██║   ██║██╔══██║   ██║       ╚════██║
██║ ╚████║██║╚██████╔╝██║  ██║   ██║            ██║
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝            ╚═╝               
            ''')
        case 5:
            print('''                                 
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗    ███████╗
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔════╝
██╔██╗ ██║██║██║  ███╗███████║   ██║       ███████╗
██║╚██╗██║██║██║   ██║██╔══██║   ██║       ╚════██║
██║ ╚████║██║╚██████╔╝██║  ██║   ██║       ███████║
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝                 
            ''')

def show_six_am_screen(duration_per_frame=0.15):
    clear_console()

    five_am_art = [
    "███████╗     █████╗ ███╗   ███╗ ",
    "██╔════╝    ██╔══██╗████╗ ████║",
    "███████╗    ███████║██╔████╔██║",
    "╚════██║    ██╔══██║██║╚██╔╝██║",
    "███████║    ██║  ██║██║ ╚═╝ ██║",
    "╚══════╝    ╚═╝  ╚═╝╚═╝     ╚═╝"
]
    six_am_art = [
    " ██████╗      █████╗ ███╗   ███╗",
    "██╔════╝     ██╔══██╗████╗ ████║",
    "███████╗     ███████║██╔████╔██║",
    "██╔═══██╗    ██╔══██║██║╚██╔╝██║",
    "╚██████╔╝    ██║  ██║██║ ╚═╝ ██║",
    " ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝"
]
    num_rows = len(five_am_art)
    if num_rows != len(six_am_art):
        print("Erro: As artes ASCII devem ter o mesmo número de linhas.")
        return

    # O número total de quadros de animação será igual ao número de linhas + 1.
    # Ex: para 6 linhas, teremos 7 quadros (do 0 ao 6).
    num_frames = num_rows + 1

    # Calcula a largura máxima das linhas para garantir que o texto antigo seja apagado.
    max_width = max(len(line) for line in five_am_art + six_am_art)
    # Adiciona um pequeno padding extra para garantir que a linha seja limpa completamente.
    pad_spaces = ' ' * (max_width + 5)

    # Adiciona algumas linhas vazias no topo para centralizar a animação verticalmente.
    sys.stdout.write("\n" * (num_rows // 2))
    sys.stdout.flush() # Garante que as novas linhas sejam impressas.

    # Imprime linhas vazias para reservar o espaço da animação e move o cursor para o topo.
    for _ in range(num_rows):
        sys.stdout.write(pad_spaces + '\n') # Imprime uma linha em branco seguida de uma quebra de linha.
    sys.stdout.write(f"\033[{num_rows}A") # Move o cursor N linhas para cima (N = num_rows).
    sys.stdout.flush() # Garante que o cursor se mova.

    # 2. Loop de animação, quadro a quadro.
    for frame_idx in range(num_frames):
        current_display_lines = []

        # Adiciona as linhas da arte de origem que ainda estão visíveis (deslizando para cima).
        # A cada quadro, uma linha superior de 'from_art' desaparece.
        current_display_lines.extend(five_am_art[frame_idx:])
        
        # Adiciona as linhas da arte de destino que estão aparecendo por baixo.
        # A cada quadro, uma nova linha de 'to_art' surge na parte inferior.
        current_display_lines.extend(six_am_art[:frame_idx])
        
        # 3. Imprime o quadro atual.
        for line_content in current_display_lines:
            # Imprime a linha, preenchendo com espaços até a largura máxima para apagar o texto antigo.
            sys.stdout.write(line_content + ' ' * (max_width - len(line_content)) + '\n')
        
        # 4. Move o cursor de volta para o topo da área de animação para o próximo quadro.
        # Isso é crucial para sobrescrever as linhas anteriores.
        if frame_idx < num_frames - 1: # Não move o cursor para cima após o último quadro.
            sys.stdout.write(f"\033[{num_rows}A")
        
        sys.stdout.flush() # Força a exibição imediata do terminal.

        time.sleep(duration_per_frame) # Pausa para controlar a velocidade da animação.

    # Após a animação, o cursor estará no final da última linha impressa.
    # Adiciona uma nova linha para garantir que o prompt do terminal apareça abaixo da animação.
    sys.stdout.write("\n")
    sys.stdout.flush()

def show_game_over_screen():
    clear_console()
    print('''
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
''')