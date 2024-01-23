import unittest
import os
from app import app


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_upload_file(self):
        file_path = 'Nfe_assinada.xml'

        with open(file_path, 'rb') as xml_file:
            response = self.app.post('/upload',
                                     content_type='multipart/form-data',
                                     data={'file': (xml_file, 'Nfe_assinada.xml')})

            self.assertEqual(response.status_code, 200)

    # Teste para verificar se o processamento é feito dentro do timeout
    def test_upload_file_within_timeout(self):
        file_path = 'Nfe_assinada.xml'

        with open(file_path, 'rb') as xml_file:
            response = self.app.post('/upload',
                                     content_type='multipart/form-data',
                                     data={'file': (xml_file, 'Nfe_assinada.xml')})
            self.assertEqual(response.status_code, 200)
            self.assertIn('data', response.json)

    # Teste para verificar se o timeout está funcionando conforme esperado
    def test_upload_file_exceeds_timeout(self):
        file_path = 'Nfe_assinada.xml'

        # Simula um processamento longo com um sleep dentro do método get_xml_data
        with patch('app.get_xml_data', side_effect=lambda x: time.sleep(2)):
            with open(file_path, 'rb') as xml_file:
                response = self.app.post('/upload',
                                         content_type='multipart/form-data',
                                         data={'file': (xml_file, 'Nfe_assinada.xml')})
                self.assertEqual(response.status_code, 408)
                self.assertIn('error', response.json)
                self.assertEqual(response.json['error'], 'Request timed out')


if __name__ == '__main__':
    unittest.main()
