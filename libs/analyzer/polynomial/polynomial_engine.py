from typing import Any, Tuple
from sklearn.preprocessing import PolynomialFeatures

class PolynomialEngine:
    
    def fit_polynomial(self, np_dataset, degree) -> Tuple[PolynomialFeatures, Any]:
        poly = PolynomialFeatures(degree=degree)
        x_poly = poly.fit_transform(np_dataset)
        return poly, x_poly