import rng.rngcpp

class _Random:
    __generator = rng.rngcpp.MT19937()
    __method = 'mt19937'

    @classmethod
    def set_generator(self, method, seed):
        seed = seed if seed else 57
        if method == 'mt19937':
            self.__generator = rng.rngcpp.MT19937(seed)
        elif method == 'middle-square':
            self.__generator = rng.rngcpp.MiddleSquare(seed)
        elif method == 'congruence':
            self.__generator = rng.rngcpp.CongruenceGenerator(seed)
        else:
            raise ValueError('Unknown generator method')
        
    @classmethod
    def get_method(self):
        return self.__method
    
    @classmethod
    def generate(self):
        return self.__generator.uniform()