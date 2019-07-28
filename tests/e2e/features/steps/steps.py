import subprocess

from behave import given, when, then


@given('{first_hand} and {second_hand} hands')
def given_hands(context, first_hand, second_hand):
    context.hands = [first_hand, second_hand]


@given('no arguments')
def given_no_args(context):
    context.hands = []


@given('{hand} argument')
def given_one_arg(context, hand):
    context.hands = [hand]


@given('below list of arguments')
def given_list_of_args(context):
    context.hands = context.text.split()


@when('{scriptname} script is run')
def when_script_is_run(context, scriptname):
    process = subprocess.Popen(
        [scriptname, *context.hands],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    context.result, context.error = process.communicate()


@then('it should fail')
def should_fail(context):
    assert context.error is not None and context.error != b''
    assert context.result is None or context.result == b''


@then('it should succeed')
def should_succeed(context):
    assert context.error is None or context.error == b'', context.error
    assert context.result is not None
    context.result = context.result.decode().strip()


@then('expected output is equal to {expected_output}')
def then_check_result(context, expected_output):
    assert context.result == expected_output,\
        f'result: [{context.result}], expected: [{expected_output}]'
