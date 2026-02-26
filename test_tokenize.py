from shunting_yard import infix_to_postfix, tokenize#### ce fichier est généré par IA

TEST_EXPRESSIONS = {
    # valides
    "simple_int": "12+34",
    "simple_float": "3.14*2",
    "negative_prefix": "-5+3",
    "negative_in_paren": "2*(-3)",
    "decimal_without_leading": ".5+.25",
    "multiple_digits_and_dots": "12.34+0.66",

    # erreurs: caractères invalides
    "invalid_char_letter": "2a+3",
    "invalid_char_symbol": "5$3",

    # erreurs: malformations de nombre
    "multiple_dots": "1.2.3 + 4",
    "dot_at_end": "12.+3",
    "isolated_dot": ". + 1",

    # erreurs: opérateurs consécutifs
    "consecutive_ops": "3++4",
    "op_at_end": "5+",
    "op_at_start": "+3",

    # cas limites
    "empty": "",
    "spaces_only": "   ",
    "long_number": "" + "9"*100 + "+1",
    "complex_negative": "-(-3)+4",
}


def run_tests():
    print("Running tokenize tests:\n")
    for name, expr in TEST_EXPRESSIONS.items():
        try:
            tokens = infix_to_postfix(expr)
            print(f"{name}: OK -> {tokens}")
        except Exception as e:
            print(f"{name}: EXCEPTION -> {e}")


if __name__ == "__main__":
    run_tests()
