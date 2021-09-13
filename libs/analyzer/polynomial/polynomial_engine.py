from typing import Any, Tuple
from sklearn.preprocessing import PolynomialFeatures

class PolynomialEngine:
    
    def fit_polynomial(self, x_train, y_train, degree) -> Tuple[PolynomialFeatures, Any]:
        poly = PolynomialFeatures(degree=degree)
        x_poly = poly.fit_transform(x_train)
        return poly, x_poly