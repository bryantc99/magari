import numerox as nx
from model import get_model


data = nx.load_zip('numerai_dataset.zip')
model = get_model()

prediction = nx.production(model, data, 'bernie', verbosity=1)
prediction.to_csv('output.csv', tournament='bernie')