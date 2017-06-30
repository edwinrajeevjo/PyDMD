from unittest import TestCase
from dmd.dmd import DMD

import numpy as np

# 15 snapshot with 400 data. The matrix is 400x15 and it contains
# the following data: f1 + f2 where
# f1 = lambda x,t: sech(x+3)*(1.*np.exp(1j*2.3*t))
# f2 = lambda x,t: (sech(x)*np.tanh(x))*(2.*np.exp(1j*2.8*t))
sample_data = np.load('tests/test_datasets/input_sample.npy')


class TestDmd(TestCase):
	def test_dmd_shape(self):
		dmd = DMD()
		dmd.fit(X=sample_data)
		assert dmd.modes.shape[1] == sample_data.shape[1] - 1

	def test_dmd_truncation_shape(self):
		dmd = DMD(k=3)
		dmd.fit(X=sample_data)
		assert dmd.modes.shape[1] == 3

	def test_dmd_decomposition(self):
		dmd = DMD()
		dmd.fit(X=sample_data)
		dmd_data = dmd.reconstructed_data
		assert np.allclose(dmd_data, sample_data)