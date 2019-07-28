import subprocess

from behave import given, when, then


@given('{first_hand} and {second_hand} hands')
def given_hands(context, first_hand, second_hand):
    context.hands = [first_hand, second_hand]


@when('{scriptname} script is run')
def when_script_is_run(context, scriptname):
    process = subprocess.Popen(
        [scriptname, *context.hands],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    context.result, error = process.communicate()
    assert error is None or error == b'', error
    assert context.result is not None
    context.result = context.result.decode().strip()


@then('expected output is equal to {expected_output}')
def then_check_result(context, expected_output):
    assert context.result == expected_output, f'result: [{context.result}], expected: [{expected_output}]'
