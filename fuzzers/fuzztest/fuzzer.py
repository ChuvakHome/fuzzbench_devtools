import os
import subprocess

# Helper library that contains important functions for building.
from fuzzers import utils

def build():
    """Build benchmark and copy fuzzer to $OUT."""
    flags = [
        # List of flags to append to CFLAGS, CXXFLAGS during
        # benchmark compilation.
    ]
    utils.append_flags('CFLAGS', flags)     # Adds flags to existing CFLAGS.
    utils.append_flags('CXXFLAGS', flags)   # Adds flags to existing CXXFLAGS.

    os.environ['CC'] = 'clang'              # C compiler.
    os.environ['CXX'] = 'clang++'           # C++ compiler.

    os.environ['FUZZER_LIB'] = '/usr/lib/FuzzTest.a'   # Path to your compiled fuzzer lib.

    # Helper function that actually builds benchmarks using the environment you
    # have prepared.
    utils.build_benchmark()

    # You should copy any fuzzer binaries that you need at runtime to the
    # $OUT directory. E.g. for AFL:
    # shutil.copy('/afl/afl-fuzz', os.environ['OUT'])


def fuzz(input_corpus, output_corpus, target_binary):
    """Run fuzzer.

    Arguments:
      input_corpus: Directory containing the initial seed corpus for
                    the benchmark.
      output_corpus: Output directory to place the newly generated corpus
                     from fuzzer run.
      target_binary: Absolute path to the fuzz target binary.
    """
    # Run your fuzzer on the benchmark.
    subprocess.call([
        your_fuzzer,
        '<flag-for-input-corpus>',
        input_corpus,
        '<flag for-output-corpus',
        output_corpus,
        '<other command-line options>',
        target_binary,
    ])

