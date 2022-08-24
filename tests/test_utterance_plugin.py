import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from neon_utterance_normalizer_plugin import UtteranceNormalizer


class TestUtterancePlugin(unittest.TestCase):
    def test_transform(self):
        normalizer = UtteranceNormalizer()

        # Contraction, article, and punctuation
        test_utterance = "what's a common name?"
        utterances, _ = normalizer.transform([test_utterance])
        self.assertEqual(utterances, [
            "what is a common name",
            "what is common name",
            "what's a common name",
            "what's a common name?"
        ])

        # Multiple transcriptions
        test_utterances = ["what's your name", "what your name"]
        utterances, _ = normalizer.transform(test_utterances)
        self.assertEqual(utterances, [
            "what is your name",
            "what's your name",
            "what your name"
        ])

    def test_strip_punctuation(self):
        self.assertEqual(UtteranceNormalizer._strip_punctuation('hello???'),
                         'hello')
        self.assertEqual(UtteranceNormalizer._strip_punctuation('test?test'),
                         'test?test')
        self.assertEqual(UtteranceNormalizer._strip_punctuation('another!test?'),
                         'another!test')


if __name__ == "__main__":
    unittest.main()
