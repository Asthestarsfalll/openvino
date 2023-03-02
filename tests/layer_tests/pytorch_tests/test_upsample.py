# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import pytest

from pytorch_layer_test_class import PytorchLayerTest


class TestUpsample1D(PytorchLayerTest):
    def _prepare_input(self):
        import numpy as np
        return (np.random.randn(1, 3, 224).astype(np.float32),)

    def create_model(self, size, scale, mode):
        import torch
        import torch.nn.functional as F

        class aten_upsample(torch.nn.Module):
            def __init__(self, size, scale, mode):
                super().__init__()
                self.size = size
                self.scale = scale
                self.mode = mode

            def forward(self, x):
                return F.interpolate(x, self.size, scale_factor=self.scale, mode=self.mode)

        ref_net = None

        return aten_upsample(size, scale, mode), ref_net, F"aten::upsample_{mode}1d"

    @pytest.mark.parametrize("mode,size,scale", [
        ('nearest', 300, None),
        ('nearest', 200, None),
        ('nearest', None, 2.5),
        ('nearest', None, 0.75),
        ('linear', 300, None),
        ('linear', 200, None),
        ('linear', None, 2.5,),
        ('linear', None, 0.75),
    ])
    @pytest.mark.nightly
    @pytest.mark.precommit
    def test_upsample1d(self, mode, size, scale, ie_device, precision, ir_version):
        self._test(*self.create_model(size, scale, mode), ie_device,
                   precision, ir_version, trace_model=True)


class TestUpsample2D(PytorchLayerTest):
    def _prepare_input(self):
        import numpy as np
        return (np.random.randn(1, 3, 200, 200).astype(np.float32),)

    def create_model(self, size, scale, mode):
        import torch
        import torch.nn.functional as F

        class aten_upsample(torch.nn.Module):
            def __init__(self, size, scale, mode):
                super().__init__()
                self.size = size
                self.scale = scale
                self.mode = mode

            def forward(self, x):
                return F.interpolate(x, self.size, scale_factor=self.scale, mode=self.mode)

        ref_net = None

        return aten_upsample(size, scale, mode), ref_net, F"aten::upsample_{mode}2d"

    @pytest.mark.parametrize("mode,size,scale", [
        ('nearest', 300, None),
        ('nearest', 150, None),
        ('nearest', (300, 400), None),
        ('nearest', None, 2.5),
        ('nearest', None, 0.75),
        ('nearest', None, (1.5, 2)),
        ('bilinear', 300, None),
        ('bilinear', 150, None),
        ('bilinear', (400, 480), None),
        ('bilinear', None, 2.5,),
        ('bilinear', None, 0.75),
        ('bilinear', None, (1.2, 1.3)),
        ('bicubic', 300, None),
        ('bicubic', 150, None),
        ('bicubic', (400, 480), None),
        ('bicubic', None, 2.5,),
        ('bicubic', None, 0.75),
        ('bicubic', None, (1.2, 1.3))
    ])
    @pytest.mark.nightly
    @pytest.mark.precommit
    def test_upsample2d(self, mode, size, scale, ie_device, precision, ir_version):
        self._test(*self.create_model(size, scale, mode), ie_device,
                   precision, ir_version, trace_model=True, **{"custom_eps": 1e-3})


class TestUpsample3D(PytorchLayerTest):
    def _prepare_input(self):
        import numpy as np
        return (np.random.randn(1, 3, 100, 100, 100).astype(np.float32),)

    def create_model(self, size, scale, mode):
        import torch
        import torch.nn.functional as F

        class aten_upsample(torch.nn.Module):
            def __init__(self, size, scale, mode):
                super().__init__()
                self.size = size
                self.scale = scale
                self.mode = mode

            def forward(self, x):
                return F.interpolate(x, self.size, scale_factor=self.scale, mode=self.mode)

        ref_net = None

        return aten_upsample(size, scale, mode), ref_net, F"aten::upsample_{mode}3d"

    @pytest.mark.parametrize("mode,size,scale", [
        ('nearest', 200, None),
        ('nearest', 150, None),
        ('nearest', (150, 200, 250), None),
        ('nearest', None, 2.5),
        ('nearest', None, 0.75),
        ('nearest', None, (1.5, 2, 2.5)),
        ('trilinear', 200, None),
        ('trilinear', 150, None),
        ('trilinear', (200, 240, 210), None),
        ('trilinear', None, 2.5,),
        ('trilinear', None, 0.75),
        ('trilinear', None, (1.2, 1.1, 1.5)),
    ])
    @pytest.mark.nightly
    @pytest.mark.precommit
    def test_upsample3d(self, mode, size, scale, ie_device, precision, ir_version):
        self._test(*self.create_model(size, scale, mode), ie_device,
                   precision, ir_version, trace_model=True, **{"custom_eps": 1e-3})
