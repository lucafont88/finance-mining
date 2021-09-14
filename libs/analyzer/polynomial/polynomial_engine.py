from typing import Any, Tuple
from sklearn.preprocessing import PolynomialFeatures

class PolynomialEngine:
    
    def compute_polynomial_features(self, np_dataset, degree) -> Tuple[PolynomialFeatures, Any]:
        poly = PolynomialFeatures(degree=degree)
        x_poly = poly.fit_transform(np_dataset)
        return poly, x_poly