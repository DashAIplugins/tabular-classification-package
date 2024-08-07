from DashAI.back.core.schema_fields import (
    BaseSchema,
    enum_field,
    int_field,
    none_type,
    schema_field,
)
from sklearn.tree import DecisionTreeClassifier as _DecisionTreeClassifier

from dashai_test_tabular_classification_plugin.sklearn_like_model import (
    SklearnLikeModel,
)
from dashai_test_tabular_classification_plugin.tabular_classification_model import (
    TabularClassificationModel,
)


class DecisionTreeClassifierSchema(BaseSchema):
    """Decision Trees are a set of are a non-parametric supervised learning method that
    learns simple decision rules (structured as a tree) inferred from the data features.
    """

    criterion: schema_field(
        enum_field(enum=["entropy", "gini", "log_loss"]),
        placeholder="entropy",
        description="The function to measure the quality of a split. Supported "
        "criteria are “gini” for the Gini impurity and “log_loss” and “entropy” both "
        "for the Shannon information gain.",
    )  # type: ignore
    max_depth: schema_field(
        none_type(int_field(ge=1)),
        placeholder=None,
        description="The maximum depth of the tree. If None, then nodes are "
        "expanded until all leaves are pure or until all leaves contain less than "
        "min_samples_split samples.",
    )  # type: ignore
    min_samples_split: schema_field(
        int_field(ge=1),
        placeholder=1,
        description="The minimum number of samples required to split an internal "
        "node.",
    )  # type: ignore
    min_samples_leaf: schema_field(
        int_field(ge=1),
        placeholder=1,
        description="The minimum number of samples required to be at a leaf node.",
    )  # type: ignore
    max_features: schema_field(
        none_type(enum_field(enum=["auto", "sqrt", "log2"])),
        placeholder=None,
        description="The number of features to consider when looking for the best "
        "split.",
    )  # type: ignore


class DecisionTreeClassifier(
    TabularClassificationModel, SklearnLikeModel, _DecisionTreeClassifier
):
    """Scikit-learn's Decision Tree Classifier wrapper for DashAI."""

    SCHEMA = DecisionTreeClassifierSchema

    def __init__(self, **kwargs) -> None:
        kwargs = self.validate_and_transform(kwargs)
        super().__init__(**kwargs)
