import decision_tree
import discretization
import image

source_file = "resources/car.data"
discrete_data = "resources/discrete.data"

col_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'label']

feature_cols = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']

discretization.discrete(source_file, discrete_data, col_names)

clf = decision_tree.train(discrete_data, col_names, feature_cols)

image.save_image(clf, feature_cols)
