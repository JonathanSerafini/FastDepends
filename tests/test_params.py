from fast_depends import Depends
from fast_depends.library import CustomField
from fast_depends.core import build_call_model


def test_params():
    def func1(m):
        ...

    def func2(c, b=Depends(func1), d=CustomField()):  # noqa: B008
        ...

    def func3(b):
        ...

    def main(a, b, m=Depends(func2), k=Depends(func3)):
        ...

    model = build_call_model(main)

    assert set(model.real_params.keys()) == {"a", "b"}
    assert set(model.flat_params.keys()) == {"a", "b", "c", "m"}
