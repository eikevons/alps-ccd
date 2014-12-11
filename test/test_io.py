import unittest
from inspect import getsourcefile
from os.path import dirname, join
import numpy as np

from ccd.io import frameset, get_frame


class TestFrameSet(unittest.TestCase):
    def test_masked(self):
        """Test than FrameSet.mean_frame respects masked arrays."""
        shape = (2, 2)
        d1 = 1.0 * np.ones(shape)
        d2 = 2.0 * np.ones(shape)
        d3 = np.ma.masked_array(3.0 * np.ones(shape), mask=[[0,0], [1,1]])

        fs = frameset.FrameSet([d1, d2, d3])
        m = fs.mean_frame()
        self.assertEqual(m[0, 0], 2.0)
        self.assertEqual(m[0, 1], 2.0)
        self.assertEqual(m[1, 0], 1.5)
        self.assertEqual(m[1, 1], 1.5)


class TestFrame(unittest.TestCase):
    def test_spe_frame_input(self):
        d = dirname(getsourcefile(lambda: None))

        frame = get_frame(join(d, "testframe_1500x1400_T=-10C_RO=100kHz.spe"))
        self.assertEqual(frame.info["temperature"], 263.16)
        self.assertEqual(frame.info["exposure"], 0.0)
        self.assertEqual(frame.info["ro_mode"], "100kHz")
        self.assertEqual(frame.shape, (1400, 1500))

        frame = get_frame(join(d, "testframe_1500x1400_T=-10C_RO=2MHz.spe"))
        self.assertEqual(frame.info["temperature"], 263.16)
        self.assertEqual(frame.info["exposure"], 0.0)
        self.assertEqual(frame.info["ro_mode"], "2MHz")
        self.assertEqual(frame.shape, (1400, 1500))


if __name__ == "__main__":

    unittest.main()
