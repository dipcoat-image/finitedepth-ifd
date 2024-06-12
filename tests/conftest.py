import os

import pytest
from finitedepth import get_sample_path

os.environ["FINITEDEPTH_TEST_SAMPLEPATH"] = get_sample_path()


@pytest.fixture
def finitedepth_tmp_path(tmp_path):
    os.environ["FINITEDEPTH_TEST_TEMPATH"] = str(tmp_path)
    return tmp_path
