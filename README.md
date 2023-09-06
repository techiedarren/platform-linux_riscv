# Linux RISCV: development platform for [PlatformIO](https://platformio.org)

Linux (RISC-V) is a Unix-like operating system that adheres mostly to the POSIX standard. It is developed and distributed following the principles of free and open-source software. Using host OS (Mac OS X, Linux) you can build native application for Linux RISC-V platform.

# Usage

1. [Install PlatformIO](https://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](https://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = linux_riscv
board = ...
...
```
