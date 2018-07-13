class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        if n==3:
            return 1
        
        prime_number=1
        not_prime =dict.fromkeys(range(3,n, 2))

        for key in range(3,n, 2):
            if not_prime[key] is None:
                prime_number+=1
                for j in range(key, int(n/key)+1, 2):
                    not_prime[j*key] = 1
                            
        return prime_number