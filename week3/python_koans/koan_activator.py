import subprocess, re, os


def hide_koans():
    hidden_koans = subprocess.check_output("grep \#from runner/path_to_enlightenment.py".split()).split('\n')
    hidden_koans = [ koan.split(' import ')[1] for koan in hidden_koans if 'import' in koan ]
    hidden_koans = [ re.sub('(?!^)([A-Z]+)', r'_\1',koan).lower() for koan in hidden_koans ]
    hidden_koans = [ koan + '.py' for koan in hidden_koans]

    for koan in hidden_koans:
        is_visible_koan = 'koans/{koan}'.format(koan=koan)
        is_hidden_koan = 'koans/.{koan}'.format(koan=koan)
        print "Moving {visible} to {hidden}".format(visible=is_visible_koan,hidden=is_hidden_koan)
        os.rename(is_visible_koan, is_hidden_koan)

def show_active_koans():
    active_koans = subprocess.check_output("grep suite.addTests runner/path_to_enlightenment.py".split()).split('\n')
    active_koans = [ koan.split('TestCase(')[1].replace(')', '') for koan in active_koans if 'TestCase' in koan if '#' not in koan ]
    active_koans = [ re.sub('(?!^)([A-Z]+)', r'_\1',koan).lower() for koan in active_koans ]

    for koan in active_koans:
        print "koans/{koan}.py".format(koan=koan)
