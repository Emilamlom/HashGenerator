import hashlib

class Hashes:
    def hash(text, opt):
        '''
        Computes the hash of a given function using the chosen algorithm
        :param text: A string of text
        :param opt: str; should only be md5, sha256, or sha512
        :return: the computed hash
        '''
        if opt == 'md5':
            return hashlib.md5(text).hexdigest()
        elif opt == 'sha256':
            return hashlib.sha256(text).hexdigest()
        elif opt == 'sha512':
            return hashlib.sha512(text).hexdigest()
        else:
            raise ValueError(f'{opt} is not a valid hashtype')

    def hashtest(wordlist1, wordlist2, suffix, option):
        with open(wordlist1, 'r') as w, open(wordlist2, 'r') as f:
            word1 = w.readline().rstrip()
            word2 = f.readline().rstrip()
            text = word1 + word2 + suffix
        try:
            return Hashes.hash(text, option)
        except ValueError as e:
            return e

    def hashbatch(self):
        pass