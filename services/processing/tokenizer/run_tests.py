from tests import *
from tests import TokenizerTests
from tests.ServiceTests import ServiceTest
from tests.TokenizerTests import TokenizerTest

print("\n\nRunning tokenization test ...")
TokenizerTest.run()

print("\n\nRunning HTTP-service test ...")
ServiceTest.run()
