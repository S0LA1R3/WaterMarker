import PyPDF2
from reportlab.lib.colors import red
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
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
    can = canvas.Canvas(packet, pagesize=letter)  # Usando o tamanho padrão da carta (letter)

    # Adicionar marcas d'água
    for marca in marcas_dagua:
        text_obj = can.beginText(marca['x'], marca['y'])
        text_obj.setFont("Helvetica", 12)  # Fonte e tamanho do texto
        text_obj.setFillColor(red)  # Cor vermelha
        text_obj.setFillAlpha(0.5)  # Opacidade de 30%

        # Adicionar quebra de linha no texto
        for line in marca['texto'].split('\n'):
            text_obj.textLine(line)

        can.drawText(text_obj)

        # Mover para a próxima posição vertical
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

nome = 'Josivaldo Maria Pinto\n769.568.423-07'

marcas_dagua = [
    {'x': 15, 'y': 70, 'texto': nome},
    {'x': 165, 'y': 20, 'texto': nome},
    {'x': 315, 'y': -30, 'texto': nome},
    {'x': 465, 'y': -80, 'texto': nome},
    {'x': 15, 'y': -30, 'texto': nome},
    {'x': 165, 'y': -80, 'texto': nome},
    {'x': 315, 'y': -130, 'texto': nome},
    {'x': 465, 'y': -180, 'texto': nome},
    {'x': 15, 'y': -130, 'texto': nome},
    {'x': 165, 'y': -180, 'texto': nome},
    {'x': 315, 'y': -230, 'texto': nome},
    {'x': 465, 'y': -280, 'texto': nome},
    {'x': 15, 'y': -230, 'texto': nome},
    {'x': 165, 'y': -280, 'texto': nome},
    {'x': 315, 'y': -330, 'texto': nome},
    {'x': 465, 'y': -380, 'texto': nome},
    {'x': 15, 'y': -330, 'texto': nome},
    {'x': 165, 'y': -380, 'texto': nome},
    {'x': 315, 'y': -430, 'texto': nome},
    {'x': 465, 'y': -480, 'texto': nome},
    {'x': 15, 'y': -430, 'texto': nome},
    {'x': 165, 'y': -480, 'texto': nome},
    {'x': 315, 'y': -530, 'texto': nome},
    {'x': 465, 'y': -580, 'texto': nome},
    {'x': 15, 'y': -530, 'texto': nome},
    {'x': 165, 'y': -580, 'texto': nome},
    {'x': 315, 'y': -630, 'texto': nome},
    {'x': 465, 'y': -680, 'texto': nome},
    {'x': 15, 'y': -630, 'texto': nome},
    {'x': 165, 'y': -680, 'texto': nome},
    {'x': 315, 'y': -730, 'texto': nome},
    {'x': 465, 'y': -780, 'texto': nome},
]

espacamento_entre_marcas = 50

adicionar_marcas_dagua(input_pdf, output_pdf, marcas_dagua, espacamento_entre_marcas)
