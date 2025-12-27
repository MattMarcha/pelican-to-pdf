import locale
import os
from shutil import rmtree
from tempfile import mkdtemp
import unittest

import pdfkit

from pelican import Pelican
from pelican.readers import MarkdownReader
from pelican.settings import read_settings
import to_pdf

CUR_DIR = os.path.dirname(__file__)


class TestToPDF(unittest.TestCase):
    def setUp(self, override=None):
        self.temp_path = mkdtemp(prefix="pelicantests.")
        settings = {
            "PATH": os.path.join(CUR_DIR, "test-data"),
            "OUTPUT_PATH": self.temp_path,
            "PLUGINS": [to_pdf],
            "LOCALE": locale.normalize("en_US"),
        }
        if override:
            settings.update(override)

        self.settings = read_settings(override=settings)
        pelican = Pelican(settings=self.settings)

        try:
            pdfkit.configuration()
            self.wk_ok = True
        except OSError:
            # wkhtmltopdf not found
            self.wk_ok = False

        pelican.run()

    def tearDown(self):
        rmtree(self.temp_path)

    def test_pdf_exists(self):
        if self.wk_ok:
            self.assertTrue(
                os.path.exists(os.path.join(self.temp_path, "my-super-post-rst.pdf"))
            )
            self.assertFalse(
                os.path.exists(
                    os.path.join(self.temp_path, "my-super-post-rst-no-pdf.pdf")
                )
            )
            if MarkdownReader.enabled:
                self.assertTrue(
                    os.path.exists(os.path.join(self.temp_path, "mysuperpdf.pdf"))
                )
                self.assertFalse(
                    os.path.exists(
                        os.path.join(self.temp_path, "my-super-post-md-no-pdf.pdf")
                    )
                )
