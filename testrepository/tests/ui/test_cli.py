#
# Copyright (c) 2009 Testrepository Contributors
# 
# Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
# license at the users choice. A copy of both licenses are available in the
# project source as Apache-2.0 and BSD. You may not use this file except in
# compliance with one of these two licences.
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# license you chose for the specific language governing permissions and
# limitations under that license.

"""Tests for UI support logic and the UI contract."""

from cStringIO import StringIO

from testrepository import commands
from testrepository.ui import cli
from testrepository.tests import ResourcedTestCase


class TestCLIUI(ResourcedTestCase):

    def test_construct(self):
        stdout = StringIO()
        stdin = StringIO()
        stderr = StringIO()
        ui = cli.UI([], stdin, stdout, stderr)

    def test_stream_comes_from_stdin(self):
        stdout = StringIO()
        stdin = StringIO('foo\n')
        stderr = StringIO()
        ui = cli.UI([], stdin, stdout, stderr)
        cmd = commands.Command(ui)
        cmd.input_streams = ['subunit']
        ui.set_command(cmd)
        results = []
        for stream in ui.iter_streams('subunit'):
            results.append(stream.read())
        self.assertEqual(['foo\n'], results)

    def test_dash_d_sets_here_option(self):
        stdout = StringIO()
        stdin = StringIO('foo\n')
        stderr = StringIO()
        ui = cli.UI(['-d', '/nowhere/'], stdin, stdout, stderr)
        cmd = commands.Command(ui)
        ui.set_command(cmd)
        self.assertEqual('/nowhere/', ui.here)
