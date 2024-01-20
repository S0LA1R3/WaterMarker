import PyPDF2
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
    can = canvas.Canvas(packet)

    # Adicionar marcas d'água
    for marca in marcas_dagua:
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
marcas_dagua = [
    {'x': 15, 'y': 10, 'texto': 'Marca d\'água 1'},
    {'x': 135, 'y': -40, 'texto': 'Marca d\'água 2'},
    {'x': 255, 'y': -90, 'texto': 'Marca d\'água 3'},
    {'x': 375, 'y': -140, 'texto': 'Marca d\'água 4'},
    {'x': 495, 'y': -190, 'texto': 'Marca d\'água 5'},
    {'x': 15, 'y': -90, 'texto': 'Marca d\'água 1'},
    {'x': 135, 'y': -140, 'texto': 'Marca d\'água 2'},
    {'x': 255, 'y': -190, 'texto': 'Marca d\'água 3'},
    {'x': 375, 'y': -240, 'texto': 'Marca d\'água 4'},
    {'x': 495, 'y': -290, 'texto': 'Marca d\'água 5'},
    {'x': 15, 'y': -190, 'texto': 'Marca d\'água 1'},
    {'x': 135, 'y': -240, 'texto': 'Marca d\'água 2'},
    {'x': 255, 'y': -290, 'texto': 'Marca d\'água 3'},
    {'x': 375, 'y': -340, 'texto': 'Marca d\'água 4'},
    {'x': 495, 'y': -390, 'texto': 'Marca d\'água 5'},
    {'x': 15, 'y': -290, 'texto': 'Marca d\'água 1'},
    {'x': 135, 'y': -340, 'texto': 'Marca d\'água 2'},
    {'x': 255, 'y': -390, 'texto': 'Marca d\'água 3'},
    {'x': 375, 'y': -440, 'texto': 'Marca d\'água 4'},
    {'x': 495, 'y': -490, 'texto': 'Marca d\'água 5'},
    {'x': 15, 'y': -390, 'texto': 'Marca d\'água 1'},
    {'x': 135, 'y': -440, 'texto': 'Marca d\'água 2'},
    {'x': 255, 'y': -490, 'texto': 'Marca d\'água 3'},
    {'x': 375, 'y': -540, 'texto': 'Marca d\'água 4'},
    {'x': 495, 'y': -590, 'texto': 'Marca d\'água 5'},
    {'x': 15, 'y': -490, 'texto': 'Marca d\'água 1'},
    {'x': 135, 'y': -540, 'texto': 'Marca d\'água 2'},
    {'x': 255, 'y': -590, 'texto': 'Marca d\'água 3'},
    {'x': 375, 'y': -640, 'texto': 'Marca d\'água 4'},
    {'x': 495, 'y': -690, 'texto': 'Marca d\'água 5'},
    # Adicione mais marcas d'água conforme necessário
]
espacamento_entre_marcas = 50

adicionar_marcas_dagua(input_pdf, output_pdf, marcas_dagua, espacamento_entre_marcas)
