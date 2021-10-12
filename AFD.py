class AFD():
    _initial: int  # The
    _final_states: set
    _alphabet: set
    _transitions: dict
    word: str
    actual: int
    idx: int

    def __init__(self, initial=0, final_states=set(), alphabet=set(), transitions=dict(), word=None) -> None:
        self._initial = initial
        self._final_states = final_states
        self._alphabet = alphabet
        self._transitions = transitions

        self.actual = self._initial
        self.idx = 0
        self.word = word

    def __str__(self) -> str:
        if self.idx < len(self.word):
            return "The word is still processing"

        status = "Accepted" if self.is_accepted() else "Rejected"
        return f'The word {self.word} is {status}'

    def is_accepted(self):
        return self.actual in self._final_states

    def reset(self):
        self.actual = self._initial
        self.idx = 0

    def __iter__(self):
        if self.word is None:
            raise Exception('There\'s not word to process')

        self.reset()
        return self

    def __next__(self):
        past = self.actual

        if self.idx == len(self.word):
            self.idx += 1
            return past

        if self.idx > len(self.word):
            raise StopIteration

        if self.word[self.idx] not in self._alphabet:
            raise Exception("The word is not in the alphabet")

        letter = self.word[self.idx]
        transition = self._transitions[self.actual]

        try:
            self.actual = transition[letter]
            self.idx += 1
            return past

        except:
            raise Exception('Inconsistent design')
