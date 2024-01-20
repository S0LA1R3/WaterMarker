import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import io

def adicionar_marcas_dagua(input_pdf, output_pdf, marcas_dagua, imagem_width, imagem_height):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Criar um arquivo PDF de saída
        with open(output_pdf, 'wb') as output_file:
            pdf_writer = PyPDF2.PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]

                # Criar um buffer para a marca d'água
                packet = io.BytesIO()
                can = canvas.Canvas(packet, pagesize=letter)

                # Adicionar marcas d'água
                for marca in marcas_dagua:
                    x, y, imagem_path = marca['x'], marca['y'], marca['imagem_path']
                    image = ImageReader(imagem_path)
                    can.drawImage(image, x, y, width=imagem_width, height=imagem_height, mask='auto')

                can.save()

                # Mover o ponteiro para o início do buffer
                packet.seek(0)

                # Criar um novo objeto PDF
                marca_dagua_pdf = PyPDF2.PdfReader(packet)

                # Mesclar a marca d'água sobre a página existente
                page.merge_page(marca_dagua_pdf.pages[0])
                pdf_writer.add_page(page)

            # Salvar o PDF de saída
            pdf_writer.write(output_file)

# Restante do código...

# Exemplo de uso
input_pdf = r'pdfs\SEMANA 1 APMBB ATT.pdf'
output_pdf = 'arquivo_com_marcas_dagua.pdf'
imagem_path = r'watermarks\marca30.png'

page = PyPDF2.PdfReader(input_pdf).pages[0]
largura, altura = page.mediabox.upper_right

# Largura e altura da imagem
imagem_width = int(int(largura) * 0.12)  # Defina a largura desejada da imagem
imagem_height = int(int(altura) * 0.048)  # Defina a altura desejada da imagem

marcas_dagua = []

# Loop para adicionar marcas d'água
for y in range(int(int(altura) * 0.1)):
    for x in range(int(int(largura) * 0.055)):
        marcas_dagua.append({'x': 0 + imagem_width * x, 'y': 0 + imagem_height * y, 'imagem_path': imagem_path})

adicionar_marcas_dagua(input_pdf, output_pdf, marcas_dagua, imagem_width, imagem_height)
