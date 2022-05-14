import unittest
from hashes import *


class MyTestCase(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(Hashes.hash('123', 'md5'), '202cb962ac59075b964b07152d234b70')
        self.assertEqual(Hashes.hash('123', 'sha256'), 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3')
        self.assertEqual(Hashes.hash('123', 'sha512'), '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2')
        
        self.assertRaises(ValueError, Hashes.hash, '', 'bogus')
    
    def test_hashtest(self):
        self.assertEqual(Hashes.hashtest('adj.txt', 'pokemon.txt', 'md5', '123'), "abandonedBulbasaur123:\n5da91ed98765fcb7096e0a61768e9a89")
        
        self.assertEqual(Hashes.hashtest('adj.txt', 'pokemon.txt', 'bogus', '123'),"bogus is not a valid hashtype")
        self.assertEqual(Hashes.hashtest('bogus1.txt', 'bogus2.txt', 'md5', '123'),"An error occurred. Check your filenames.")

    def test_hashbatch(self):
        Hashes.hashbatch('adj.txt', 'pokemon.txt', 'md5', '123')
        testout = open('wordlists/adj_pokemon123.txt', 'r')
        testline = testout.readline()
        self.assertEqual(testline, "abandonedBulbasaur123:5da91ed98765fcb7096e0a61768e9a89\n")

        self.assertEqual(Hashes.hashbatch('adj.txt', 'pokemon.txt', 'bogus', '123'), "bogus is not a valid hashtype")
        self.assertEqual(Hashes.hashbatch('bogus1.txt', 'bogus2.txt', 'md5', '123'), "An error occurred. Check your filenames.")
        testout.close()


if __name__ == '__main__':
    unittest.main()
