"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_create_doctor():
    from inflammation.models import Doctor, Patient

    name = 'Bob'
    patients = [Patient('Alice')]
    d = Doctor(name=name, patients=patients)

    assert d.name == name
    assert d.patients[0].name == 'Alice'

