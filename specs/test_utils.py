# -*- coding: utf-8 -*-

import unittest

from acrylamid.utils import NestedProperties


class TestNestedProperties(unittest.TestCase):

    def test_works(self):

        dct = NestedProperties()
        dct['hello.world'] = 1

        assert dct['hello']['world'] == 1
        assert dct.hello.world == 1

        try:
            dct.foo
            dct.foo.bar
        except KeyError:
            assert True
        else:
            assert False

        dct['hello.foreigner'] = 2

        assert dct['hello']['world'] == 1
        assert dct.hello.world == 1

        assert dct.hello.foreigner == 2

    def test_redirects(self):

        dct = NestedProperties()
        alist = [1, 2, 3]

        dct['foo'] = alist
        dct.redirect('foo', 'baz')

        assert 'foo' in dct
        assert 'baz' in dct
        assert dct['baz'] == alist
