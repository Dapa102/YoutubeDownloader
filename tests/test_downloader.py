"""
Unit tests untuk YouTube Downloader
"""

import unittest
import os
import sys

# Tambahkan path src ke PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestDownloader(unittest.TestCase):
    """
    Test cases untuk fungsi downloader
    """
    
    def test_import(self):
        """Test apakah module bisa di-import"""
        try:
            import download_videoYT.app
            self.assertTrue(True)
        except ImportError:
            self.fail("Gagal import download_videoYT.app")
    
    def test_folder_creation(self):
        """Test pembuatan folder downloads"""
        from download_videoYT.app import download_video
        # Fungsi download_video akan membuat folder 'downloads'
        # Test ini bisa dikembangkan lebih lanjut
        self.assertTrue(callable(download_video))


if __name__ == '__main__':
    unittest.main()
