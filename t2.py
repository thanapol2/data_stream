from skmultiflow.data import SEAGenerator
from skmultiflow.trees import HoeffdingTree
from skmultiflow.bayes import NaiveBayes
from skmultiflow.evaluation import EvaluateHoldout
from skmultiflow.data import AGRAWALGenerator
# Set the stream
# stream = SEAGenerator(random_state=1)

stream = SEAGenerator()
stream.prepare_for_use()
# Set the model
ht = HoeffdingTree()
nb = NaiveBayes()
# Set the evaluator
evaluator = EvaluateHoldout(max_samples=100000,max_time=1000,
show_plot=True,
metrics=['accuracy', 'kappa'],
dynamic_test_set=True)
 # Run evaluation
evaluator.evaluate(stream=stream, model=[ht, nb], model_names=['HT', 'NB'])