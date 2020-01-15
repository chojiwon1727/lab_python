import graphviz
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz

# 데이터 load
iris = load_iris()
x = iris.data
y = iris.target
features = iris.feature_names


# 의사결정나무(알고리즘) 객체 생성
decision_tree = DecisionTreeClassifier()
decision_tree.fit(x, y)
# decision_tree.predict()

# 의사결정 나무 텍스트 출력
text_result = export_text(decision_tree, features)
print(text_result)

# 의사결정 나무 그래프 출력
graph_data = export_graphviz(decision_tree, feature_names=features)   # 그래프를 그릴 수 있는 데이터
graph = graphviz.Source(graph_data)           # 그래프 객체
graph.render('iris')                          # 그래프 객체를 파일(pdf)로 작성
