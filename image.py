from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus


def save_image(clf, feature_cols):
    class_names = ['v-good', 'good', 'unacc', 'acc']
    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, feature_names=feature_cols, class_names=class_names)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    Image(graph.create_png())

    graph.write_png('cars.png')
    Image(graph.create_png())
