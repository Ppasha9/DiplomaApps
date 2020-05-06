"""
FID_Calculator application - calculating Frechet Inception Distance (FID) of certain generator model.

Usage:
    FID_Calculator.exe --model-path PATH [--output PATH]
    FID_Calculator.exe --help

Options:
    --model-path PATH           Path to the generator's model - general argument for all applications.
    --output PATH               Path to the txt file, where the FID metric will be written
    -h, --help                  Show this message.
"""

import docopt

from fid_calculator import calculate_fid


def run(opts):
    calculate_fid(opts)


if __name__ == "__main__":
    run(docopt.docopt(__doc__))
