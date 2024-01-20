import PyPDF2
from reportlab.lib.colors import red
from reportlab.pdfgen import canvas
import io

def adicionar_marcas_dagua(input_pdf, output_pdf, marcas_dagua, espacamento):
    # Abrir o arquivo PDF de entrada
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Criar um arquivo PDF de saída
        with open(output_pdf, 'wb') as output_file:
            pdf_writer = PyPDF2.PdfWriter()

            # Adicionar marcas d'água em cada página
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                marca_dagua_pdf = gerar_marcas_dagua_pdf(marcas_dagua, espacamento)
                
                # Aplicar rotação e escala à marca d'água
                marca_dagua_pdf.pages[0].rotate = 45
                marca_dagua_pdf.pages[0].scale(1, 1)
                
                # Mesclar a marca d'água sobre a página existente
                page.merge_page(marca_dagua_pdf.pages[0])

                pdf_writer.add_page(page)

            # Salvar o PDF de saída
            pdf_writer.write(output_file)

def gerar_marcas_dagua_pdf(marcas_dagua, espacamento):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(612, 792))  # Tamanho padrão de uma página (8.5 x 11 polegadas)

    # Adicionar marcas d'água
    for marca in marcas_dagua:
        can.setFont("Helvetica", 12)  # Fonte e tamanho do texto
        can.setFillColor(red)  # Cor vermelha
        can.setFillAlpha(0.3)  # Opacidade de 30%
        can.drawString(marca['x'], marca['y'], marca['texto'])
        can.translate(0, espacamento)

    can.save()

    # Movendo o ponteiro para o início do buffer
    packet.seek(0)

    # Criar um novo objeto PDF
    marca_dagua_pdf = PyPDF2.PdfReader(packet)

    return marca_dagua_pdf

# Exemplo de uso
input_pdf = r'pdfs\documento-8.pdf'
output_pdf = 'arquivo_com_marcas_dagua.pdf'

nome = 'Josivaldo Maria Pinto'

marcas_dagua = [
    {'x': 15, 'y': 10, 'texto': nome},
    {'x': 135, 'y': -40, 'texto': nome},
    {'x': 255, 'y': -90, 'texto': nome},
    {'x': 375, 'y': -140, 'texto': nome},
    {'x': 495, 'y': -190, 'texto': nome},
    {'x': 15, 'y': -90, 'texto': nome},
    {'x': 135, 'y': -140, 'texto': nome},
    {'x': 255, 'y': -190, 'texto': nome},
    {'x': 375, 'y': -240, 'texto': nome},
    {'x': 495, 'y': -290, 'texto': nome},
    {'x': 15, 'y': -190, 'texto': nome},
    {'x': 135, 'y': -240, 'texto': nome},
    {'x': 255, 'y': -290, 'texto': nome},
    {'x': 375, 'y': -340, 'texto': nome},
    {'x': 495, 'y': -390, 'texto': nome},
    {'x': 15, 'y': -290, 'texto': nome},
    {'x': 135, 'y': -340, 'texto': nome},
    {'x': 255, 'y': -390, 'texto': nome},
    {'x': 375, 'y': -440, 'texto': nome},
    {'x': 495, 'y': -490, 'texto': nome},
    {'x': 15, 'y': -390, 'texto': nome},
    {'x': 135, 'y': -440, 'texto': nome},
    {'x': 255, 'y': -490, 'texto': nome},
    {'x': 375, 'y': -540, 'texto': nome},
    {'x': 495, 'y': -590, 'texto': nome},
    {'x': 15, 'y': -490, 'texto': nome},
    {'x': 135, 'y': -540, 'texto': nome},
    {'x': 255, 'y': -590, 'texto': nome},
    {'x': 375, 'y': -640, 'texto': nome},
    {'x': 495, 'y': -690, 'texto': nome},
]
espacamento_entre_marcas = 50

adicionar_marcas_dagua(input_pdf, output_pdf, marcas_dagua, espacamento_entre_marcas)
