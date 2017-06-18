from chibi_dict import Chibi_dict
import pytest
from expects import expect, be, raise_error


@pytest.fixture
def simple_dict():
    return Chibi_dict( a=10, b=20, c=30 )


class Test_chibi_dict:
    def test_simple_dict_can_retrieve_by_attr_and_key( self, simple_dict ):
        expect( simple_dict.a ).to( be(simple_dict[ 'a' ] ) )
        expect( simple_dict.b ).to( be(simple_dict[ 'b' ] ) )
        expect( simple_dict.c ).to( be(simple_dict[ 'c' ] ) )

    def test_retrieve_a_not_exists_attribute_raises_expection( self,
                                                               simple_dict ):
        def mock_for_retrieve_attr():
            simple_dict.d

        expect( mock_for_retrieve_attr ).to( raise_error( AttributeError ) )

    def test_add_new_attributes( self, simple_dict ):
        simple_dict.d = 40
        expect( simple_dict.d ).to( be( simple_dict[ 'd' ] ) )

    def test_add_new_key( self, simple_dict ):
        simple_dict[ 'd' ] = 40
        expect( simple_dict.d ).to( be( simple_dict[ 'd' ] ) )
