def test__conversion_date(operations_instance):
    assert operations_instance.conversion_date() == "26.08.2019"
    assert isinstance(operations_instance.conversion_date(), str)
    assert len(operations_instance.conversion_date()) == 10


def test__masking_payment_information(operations_instance):
    assert operations_instance.mask_payment_info(
        operations_instance.from_
    ) == "Счет **5560"
    assert operations_instance.mask_payment_info(
        operations_instance.to
    ) == "Visa Gold 5999 41** **** 6353"
