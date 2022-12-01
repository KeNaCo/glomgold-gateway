from payment import Payment
from gate import Gate


def test_process_one_payment_should_success():
    payment = Payment()
    gate = Gate(provider=Provider())

    assert payment.is_initialised()
    gate_response = gate.process(payment)
    assert gate_response == GateResponse(...)
