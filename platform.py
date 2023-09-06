# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from platformio import exception
from platformio.public import PlatformBase, get_systype


class Linux_riscvPlatform(PlatformBase):

    @staticmethod
    def _is_native():
        systype = get_systype()
        return "linux_riscv32" in systype or "linux_riscv64" in systype

    @property
    def packages(self):
        packages = PlatformBase.packages.fget(self)
        if self._is_native() and "toolchain-riscv" in packages:
            del packages['toolchain-riscv']
        return packages