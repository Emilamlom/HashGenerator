import hashlib

class Hashes:
    dir = 'wordlists/'
    
    def hash(text, opt):
        '''
        Computes the hash of a given function using the chosen algorithm
        :param text: A string of text
        :param opt: str; should only be md5, sha256, or sha512
        :return: the computed hash
        '''
        if opt == 'md5':
            return hashlib.md5(text.encode()).hexdigest()
        elif opt == 'sha256':
            return hashlib.sha256(text.encode()).hexdigest()
        elif opt == 'sha512':
            return hashlib.sha512(text.encode()).hexdigest()
        else:
            raise ValueError(f'{opt} is not a valid hashtype')

    def hashtest(wordlist1, wordlist2, suffix='', option):
        '''
        Combines wordlists and suffix and hashes them once
        :param wordlist1: filepath to a wordlist in wordlists dir
        :param wordlist2: filepath to a wordlist in wordlists dir
        :param suffix: str; a suffix added onto the test line, empty string by default
        :param option: type of hash algo selected
        :return: Exit status message
        '''
        with open(Hashes.dir + wordlist1, 'r') as f, open(Hashes.dir + wordlist2, 'r') as g:
            word1 = f.readline().rstrip()
            word2 = g.readline().rstrip()
            text = word1 + word2 + str(suffix)
        try:
            return f'{text}:\n' \
                   f'{Hashes.hash(text, option)}'
        except ValueError as e:
            return e
        except:
            return 'An error occurred. Check your filenames.'

    def hashbatch(wordlist1, wordlist2, suffix='', option):
        '''
        Combines wordlists and suffix and hashes them in a batch process.
        :param wordlist1: filepath to a wordlist in wordlists dir
        :param wordlist2: filepath to a wordlist in wordlists dir
        :param suffix: str; a suffix added onto each line, empty string by default
        :param option: type of hash algo selected
        :return: Exit status message
        '''
        list1 = wordlist1.split('.')
        list2 = wordlist2.split('.')
        filename = Hashes.dir + list1[0] + '_' + list2[0] + suffix + '.txt'

        try:
            with open(Hashes.dir + wordlist1, 'r') as f, open(Hashes.dir + wordlist2, 'r') as g, open(filename, 'a') as h:
                words1 = f.readlines()
                words2 = g.readlines()
                for w1 in words1:
                    for w2 in words2:
                        text = w1.rstrip() + w2.rstrip() + str(suffix)
                        h.write(text + ':' + Hashes.hash(text, option) + "\n")
            return f'Hashes saved to {filename} using {option}'
        except ValueError as e:
            return e
        except:
            return 'An error occurred. Check your filenames.'

if __name__ == '__main__':
    Hashes.hashbatch('pokemon.txt', 'adj.txt', '', 'md5')