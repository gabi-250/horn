from horn.player.track import Track
from unittest.mock import patch, MagicMock
import unittest


def mock_abspath(path):
    return "ABS_%".format(path)


def mock_get_string(tag_title):
    return ['title', 'test_title']


def mock_get_sample(tag_title):
    return ['image', '/home/image.png']


class MockDiscoverer(MagicMock):
    def discover_uri(self, file_uri):
        return MockDiscovererInfo()


class MockDiscovererInfo(MagicMock):
    def get_tags(self):
        mock_tags = MagicMock()
        mock_tags.get_string = MagicMock(side_effect=mock_get_string)
        mock_tags.get_sample = MagicMock(side_effect=mock_get_sample)
        return mock_tags

    def get_duration(self):
        return 6000000000


@patch('horn.player.track.GstPbutils.Discoverer',
       new=MockDiscoverer())
@patch('horn.player.track.Gst.SECOND', new=1000000000)
@patch('horn.player.track.Gst', new=MagicMock())
@patch('horn.player.track.GstPbutils', new=MagicMock())
@patch('horn.player.track.os.path.abspath', new=mock_abspath)
class TestTrack(unittest.TestCase):
    def test_simple(self):
        file_path = 'test/path'
        title = 'test_title'
        track = Track(file_path)
        self.assertEqual(track.title, title)
        self.assertEqual(track.file_path, "ABS_%".format(file_path))
        self.assertEqual(track.duration, 6.0)
