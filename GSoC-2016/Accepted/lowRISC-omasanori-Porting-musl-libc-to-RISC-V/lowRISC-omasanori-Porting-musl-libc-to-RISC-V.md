---
title:
  Porting musl libc to RISC-V
author:
  Masanori Ogino
date:
  \today
abstract:
  musl is an implementation of the C standard library for Linux. It is clean,
  robust, efficient and conformant with most of the ISO C11 and POSIX 2008
  standards. This project aims to port musl to RISC-V to provide an attractive
  alternative to glibc for the open instruction set architecture ecosystem.
...

# Motivation

Newlib and glibc have already been ported to the RISC-V ISA. The former is used
for bare-metal programs and the latter is for Linux-based systems. While glibc
is the most popular Linux libc for servers and PCs, there are some alternative
implementations.

[musl](http://www.musl-libc.org/) is an implementation of libc for Linux. musl
is used by some Linux distribution including Alpine Linux, Sabotage Linux and
Void Linux as their primary libc. musl features an excellent support for static
linking while it supports dynamic linking efficiently too. According to
"[Comparison of C/POSIX standard library implementations for
Linux](http://www.etalabs.net/compare_libcs.html)", the code size of musl is
much smaller than that of glibc for static linking.

While musl focuses on code size, it offers most of the C APIs in ISO C11 and
POSIX 2008 standards with some extensions provided by BSD libc and glibc. musl
is designed to be robust, e.g. consideration to algorithmic complexity attacks,
avoiding unnecessary dynamic allocation, etc.

The goal of this project is porting musl to RISC-V. Due to its code size and
robustness, it will become an attractive alternative to glibc especially for
developers of embedded systems. It will also involve opportunities to find
failures in other layers: kernels, toolchains, simulators or hardware.
Moreover, its simple and clean code base will yield benefits for both
production and education use.

# Related Work

There is a [RISC-V port of musl](https://github.com/lluixhi/musl-riscv) by Aric
Belsito. Although it is not merged to the upstream tree, it already has most of
the mandatory part of porting and it looks good to me. Thus, I will use the
port as the basis.

# Targets

RISC-V is a modular ISA: it consists of base instruction sets and some standard
extensions. This proposal assumes RV32G and RV64G as main targets; they are
32-bit and 64-bit variants of RISC-V ISA with multiplication and division
instructions, atomic instructions and floating-point instructions with binary32
and binary64 formats in IEEE 754-2008. However, some deliverables may assumes
other prerequisites.

The [Spike RISC-V simulator](https://github.com/riscv/riscv-isa-sim) and/or
QEMU will be used for testing.

# Deliverables

## Basic RISC-V Support [required]

This is the essential part of the proposal. It contains an implementation of
mandatory `arch/${ISA}` portion of musl for RISC-V (both the 32-bit and 64-bit
variants) and related changes to the toolchain. After that, we can build and
run some programs on Linux on RISC-V with musl. Also, we can use libc-test and
libc-bench tools to measure the quality of the port then.

Since the code will be derived from the existing port, bug fixes and
implementation of missing part will be the main tasks on this field.

## Optimized Implementation of Certain Functions [required]

musl provides the way to replace generic implementations to ones for a
particular architecture. It is mainly used to provide an optimized version of
mathematical functions, string manipulation functions or so on. For example,
musl provides a custom version of `log2` using the `fyl2x` instruction on x86.

While practical optimization requires careful measurement with actual hardware,
I do not have any working hardware yet. Thus, the optimization will be limited
to some cases. For example, the use of special instructions or great reduction
of instruction cycles is viable. Optimization will be done not only on musl
itselft, but also on the toolchain if needed.

## Support for Processors without Floating-point Instructions [required]

As I specified in the "Targets" section, I choose RISC-V processors with
floating-point units (FPUs) as the primary targets. However, some RISC-V
microcontrollers omit FPUs as permitted by the ISA specification.

In addition to the primary targets, it is worthwhile to test musl against the
software floating-point (soft-float) ABI and fix errors in order to support
such microcontrollers.

## Support for Processors without Atomic Instructions [required]

As I specified in the "Targets" section, I choose RISC-V processors with atomic
instructions. However, the ISA specification permits processors to omit such
instructions specified in the A standard extension.

musl requires compare-and-swap (CAS) or other atomic memory operation that can
be used for implementing CAS. Thus, an additional work is required to support
processors without atomic instructions.

### Migration of CAS Emulation System Calls to vDSO Functions [optional]

The [RISC-V fork of Linux kernel](https://github.com/riscv/riscv-linux)
provides CAS emulation system calls for processors without atomic instructions
and glibc calls them if it is built for such processors. It costs CPU time for
interruption and context switching every time CAS is performed.

Moreover, when a system is ported to processors with atomic instructions, we
need to recompile the library to gain the advantage of atomic instructions. The
situation is getting worse if we use static-linked binaries; we need to rebuild
the whole system to eliminate unnecessary system calls. Also, on non-SMP
systems, CAS can be achieved by much simpler way than what we do for now.

The virtual dynamic shared object (vDSO) is a mechanism to avoid system calls
in such situation. With vDSO, userland has to call functions exported from
kernel and the functions will choose the best way on the current setup.
Implementing vDSO functions for CAS emulation will benefit not only musl-based
systems but also glibc-based systems if the libc uses them.

## Automatic Testing Infrastructure [required]

Since the software stack of RISC-V is still in heavy development, it is desired
to have an infrastructure to test the port automatically against latest
simulator, toolchain, kernel and so on. Then we will be able to find when
something goes wrong.

At the beginning, it will be made of bunch of scripts to checkout the sources,
build the tools and rootfs image, run the simulator and save the result into a
file. It will run on my machine for a while, but it would be better to have a
place in either of the projects.

## Improvement of musl Porting Guide [required]

As I mentioned before, musl has a porting document. However, recent changes
made it obsolete, while the majority is still useful now. Also, the document is
made of links to memos, archives of the mailing list, commits, ISA vendors'
official documents and so on.

It would be better to have an up-to-date and self-contained porting guide
describing topics that is common between architectures on the official wiki.

## Preliminary Work toward System V ABI RISC-V Processor Supplement [optional]

On other architectures, modern Unix systems use the System V ABI Processor
Supplement (psABI) documents for the reference of calling conventions,
interface with operating systems, the value of ELF field headers and so on. In
contrast, there is no such documents for RISC-V, though Linux and some \*BSDs
have already been ported to RISC-V. The user-level ISA specification only
specifies some aspect of calling conventions. It will benefit software
developers to have a complete psABI document.

It is too hard for a twelve-weeks project to discuss and specify whole psABI
while the porting is underway. Thus I will write some documents describing the
current ABI for a starting point toward actual psABI.  I will survey and
discuss the ABI with other developers during porting anyway, so the work will
be a summary of my research and the discussions.

## Others

As part of the project, I may contribute other patches to related projects,
e.g. tools provided by the RISC-V project, musl, libc-test, etc.

# Schedule

## Community Bonding Period (April 22 -- May 22)

- Building tools, kernel and rootfs with glibc, and then executing them.
- Reading musl, trying to fix trivial problems and discussing them.
- Reading patches in
  [riscv-gnu-toolchain](https://github.com/riscv/riscv-gnu-toolchain) to
  understand RISC-V specific part of the toolchain.
- Reading patches in [musl-cross](https://bitbucket.org/GregorR/musl-cross) to
  understand musl specific part of the toolchain.
- Research the existing port.
- Communicating with other developers to understand the details.

## Week 1 -- 3 (May 23 -- June 12)

- Integrate the existing port to the toolchain.
- Implement the missing features for RV64G.
- Fix bugs blocking the integration.

## Week 4 (June 13 -- June 19)

- Build rootfs with musl-based toolchain.
- Fix userland code if it depends on glibc.
- Run Linux with musl-based userland on the simulator.
- Debug the port if the system does not launch.

## Week 5 (June 20 -- June 26)

- Build [libc-test](http://nsz.repo.hu/git/?p=libc-test) and execute it.
- Check the result of the test and compare with x86.
- Submit the patch to the mailing list for reviewing.
- Update the patch in response to the result of reviewing.
- Prepare and submit the mid-term evaluation.

## Week 6 -- 7 (June 27 -- July 10)

- Write test automation scripts.
- Implement the missing features for RV32G.
- Build the toolchain with multilib setting.
- Fix bugs blocking multilib.

## Week 8 (July 11 -- July 17)

- Build [libc-bench](http://git.musl-libc.org/cgit/libc-bench/) and execute it.
- Test the code on RV32IMA and RV64IMA (soft-float) settings.
- Fix bugs for soft-float settings.

## Week 9 -- 10 (July 18 -- July 31)

- Implement atomic operation primitives for `-mno-atomic`.
  <!-- arch/rv*/atomic_arch.h -->
- Test the code on `-mno-atomic` settings.
- Submit the patches to the mailing lists for reviewing.
- Update the patches in response to the result of reviewing.

## Week 11 -- 12 (August 1 -- August 14)

- Work on optimization.
- Write the porting guide.

## Week 13 -- 14 (August 15 -- August 23)

- Work on the remaining works.
- Clean up the code.
- Prepare and submit the final evaluation and code samples.

# Biographical Information

I am an information science master's student in Japan. My field of study is
coding theory. In particular, data compression for the output data of particle
detectors was the main theme of my bachelor thesis.

I am interested in how operating systems work. I wrote a tiny (less than 3
kSLOC) OS with cooperative multitasking and serial I/O written in C for a H8
microcontroller as a hobby. I choose Windows and Linux for daily use. However,
sometimes I try to install, play with and read implementations of other kinds
of OSs like Hurd, \*BSDs, OpenIndiana and so on. I have no experience in
large-scale OS development, though.

I have participated in OSS projects for few years. I have contributed 50+
patches to the [Rust programming language](https://www.rust-lang.org/) and
written part of the [Rust overlay for Gentoo
Linux](https://github.com/gentoo/gentoo-rust). I have contributed some patches
to [compiler-rt](http://compiler-rt.llvm.org/) and other projects too.
