import pytest

from pytests.BaseClass import BaseClass
from pytests.conftest import dataload


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_profiledata(self, dataload):
        log = self.logname()
        log.info(dataload[1])
        log.info(dataload[0])
        print(dataload)


