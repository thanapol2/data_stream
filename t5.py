# The second example demonstrates how to compare two models
from skmultiflow.data import SEAGenerator
from skmultiflow.trees import HoeffdingTree
from skmultiflow.bayes import NaiveBayes
from skmultiflow.evaluation import EvaluatePrequential
from skmultiflow.data.regression_generator import RegressionGenerator

# Set the stream
# stream = SEAGenerator(classification_function = 2, random_state = 112,
#                                   balance_classes = False,noise_percentage = 0.28)

stream = RegressionGenerator(n_samples=100, n_features=20, n_targets=4, n_informative=6, random_state=0)
stream.prepare_for_use()
# stream.generate_drift()

# Set the models
ht = HoeffdingTree()
# nb = NaiveBayes()

evaluator = EvaluatePrequential(max_samples=10000,
                                max_time=1000,
                                show_plot=True,
                                metrics=['average_mean_squared_error'])

# Run evaluation
evaluator.evaluate(stream=stream, model=[ht], model_names=['HT'])