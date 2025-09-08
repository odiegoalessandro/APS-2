from typing import Tuple

from fermat_primality_test import fermat_primality_test


def miller_rabin_test(n: int, k: int) -> Tuple[bool, list]:
    fermat_test_passed, witnesses = fermat_primality_test(n)

    if not fermat_test_passed:
        return False, [witnesses]

    # TODO: implementar o teste de Miller-Rabin

    return True, []
