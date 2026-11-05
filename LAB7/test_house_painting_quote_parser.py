from hypothesis import given, strategies as st
from house_painting_quote_parser import clean_colour_name, room_area, total_wall_area

@given(st.text() | st.none())
def test_clean_colour_name_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_room_area_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_total_wall_area_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass
