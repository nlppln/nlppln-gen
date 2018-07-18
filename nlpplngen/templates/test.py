# -*- coding: utf-8 -*-
import os

from click.testing import CliRunner

# FIXME: import correct methods for testing
from nlppln.commands.{{command_name}} import {{command_name}}


# Documentation about testing click commands: http://click.pocoo.org/5/testing/
def test_{{command_name}}():
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.makedirs('in')
        os.makedirs('out')

        # FIXME: create example input file(s)
        with open('in/test.txt', 'w') as f:
            content = '\n' \
                      '\n'
            f.write(content)

        # FIXME: update command, options and arguments
        result = runner.invoke({{command_name}}, ['<argument>', '--out_dir', 'out'])

        assert result.exit_code == 0

        # FIXME: What files should exist after command execution?
        #assert os.path.exists('out/test.xml')
