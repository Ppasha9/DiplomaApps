from PyInstaller.__main__ import run


def setup(opts):
    if opts.get('--fid-calculator-exe', None):
        run([
            '--name=FID_Calculator',
            '--onefile',
            '--console',
            'main_fid_calculator.py',
        ])
