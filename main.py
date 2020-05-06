"""
Project for diploma's applications.
List of supported applications:
    * FID_Calculator - calculating Frechet Inception Distance (FID) of certain generator model.

Usage:
    DiplomaApps.exe --fid-calculate --model-path PATH [--output PATH]
    DiplomaApps.exe --build-exe --fid-calculator-exe
    DiplomaApps.exe --build-self-exe
    DiplomaApps.exe --help

Options:
    --fid-calculate             Bool flag, it means that FID_Calculator is running now.
    --model-path PATH           Path to the generator's model - general argument for all applications.
    --output PATH               Special argument for all applications (optional).
                                It has different meanings for different applications.
                                For `FID_Calculator` - path to the txt file, where the FID metric will be written.
    --build-exe                 Bool flag, it means that project is running in building exe mode.
    --fid-calculator-exe        Bool flag, build exe for FID_Calculator.
    --build-self-exe            Bool fag for building DiplomaApps.exe.
    -h, --help                  Show this message.
"""

import docopt

from fid_calculator import calculate_fid
from setup import setup


def run(opts):
    if opts.get('--fid-calculate', None):
        calculate_fid(opts)
        return

    if opts.get('--build-exe', None):
        setup(opts)
        return


if __name__ == "__main__":
    run(docopt.docopt(__doc__))
