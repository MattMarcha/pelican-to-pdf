import logging
import pdfkit

from pelican import signals
from pathlib import Path

log = logging.getLogger(__name__)

def check_pdf(path, context):
    """Check if a pdf has to be generated for this content
    :param str path: The file path
    :param dict context: The context sent to the template
    """
    item = context.get('article', False) or context.get('page', False)
    if item and 'to_pdf' in item.metadata:
        to_pdf = eval(item.metadata['to_pdf']) if item.metadata['to_pdf'] else {}
        output = Path(path).with_suffix('.pdf')
        if 'name' in to_pdf: output = output.with_stem(to_pdf['name'])
        create_pdf(path, output, to_pdf.get('css', False))

def create_pdf(input_path, output_path, stylesheet_path=False):
    options = {
        'encoding': 'UTF-8',
        'margin-top': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'margin-right': '0mm'
    }
    if stylesheet_path:
        options.update({'user-style-sheet': stylesheet_path})

    try:
        pdfkit.from_file(input_path, output_path, options=options)
    except Exception as e:
        log.error(f"Error while generating PDF at {output_path}: {e}")

def register():
    signals.content_written.connect(check_pdf)
