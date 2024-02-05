import unittest

"""
Count names with more than x letters
"""
def count_long_names(prenoms: list[str]) ->str:
    nombre_caracteres = 7
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > nombre_caracteres:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_long_names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()