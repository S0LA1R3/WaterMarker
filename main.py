import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import io

def adicionar_marcas_dagua(input_pdf, output_pdf, marcas_dagua, espacamento, imagem_width, imagem_height):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Criar um arquivo PDF de saída
        with open(output_pdf, 'wb') as output_file:
            pdf_writer = PyPDF2.PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                
                packet = io.BytesIO()
                can = canvas.Canvas(packet, pagesize=letter)

                # Adicionar marcas d'água
                for marca in marcas_dagua:
                    x, y, imagem_path = marca['x'], marca['y'], marca['imagem_path']
                    image = ImageReader(imagem_path)
                    can.drawImage(image, x, y, width=imagem_width, height=imagem_height, mask='auto')

                    # Mover para a próxima posição vertical
                    can.translate(0, espacamento)

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

# Exemplo de uso
input_pdf = r'pdfs\CFPOnline_REDAÇÃO_A-dissertação-e-o-texto-argumentativo.pdf'
output_pdf = 'arquivo_com_marcas_dagua.pdf'
imagem_path = r'watermarks\marca702.png'

# largura da pagina: 595.276
# altura da pagina: 793.701

marcas_dagua = []

# x entre elementos: 20
# y entre elementos: 10
# padrao de elemento: {'x': 465, 'y': -130, 'imagem_path': imagem_path}


for y in range(78):
    for x in range(33):
        marcas_dagua.append({'x': 0 + 20 * x, 'y': 0 + 10 * y, 'imagem_path': imagem_path})

espacamento_entre_marcas = 0
imagem_width = 18  # Defina a largura desejada da imagem
imagem_height = 10  # Defina a altura desejada da imagem

adicionar_marcas_dagua(input_pdf, output_pdf, marcas_dagua, espacamento_entre_marcas, imagem_width, imagem_height)
