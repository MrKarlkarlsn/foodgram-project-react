from io import BytesIO

from django.http import HttpResponse
from django.templatetags.static import static

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont


def generate_pdf(queryset):
    """Создание PDF файла для отправки пользователю"""
    buffer = BytesIO()

    path_font = static('fonts/fontawesome-webfont.ttf')
    pdfmetrics.registerFont(TTFont('fontawesome-webfont',
                                   path_font))

    pdf_file = canvas.Canvas(buffer, bottomup=0)
    pdf_file.setFont('fontawesome-webfont', 14)

    y = 150
    pdf_file.drawString(40, 100, text='Cписок покупок:')
    for obj in queryset:
        text = (f'{obj["ingredient__name"].capitalize()} '
                f'--> {obj["quantity"]} '
                f'{obj["ingredient__measurement_unit"]}')
        pdf_file.drawString(100, y, text=text)
        y += 20

    pdf_file.showPage()
    pdf_file.save()
    pdf = buffer.getvalue()
    buffer.close()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        'attachment; filename="list_in_shop.pdf"'
    )
    response.write(pdf)
    return response
