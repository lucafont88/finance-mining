from numpy import ndarray
from sklearn.pipeline import Pipeline
from libs.analyzer.polynomial.interpolation_engine import InterpolationEngine
from typing import Any, Dict, List, Tuple, Union
from sklearn.preprocessing import PolynomialFeatures

class PolynomialEngine:
    
    def compute_polynomial_features(self, np_dataset, degree) -> Tuple[PolynomialFeatures, Any]:
        poly = PolynomialFeatures(degree=degree)
        x_poly = poly.fit_transform(np_dataset)
        return poly, x_poly

    def compute_interpolated_polynomial(self, np_dataset: ndarray, degrees: List[int] = [3, 4, 5], n_points: int = 10, do_plot: bool = False) -> Dict[int, Pipeline]:
        interpolation_engine = InterpolationEngine(np_dataset, degrees, n_points)
        models = interpolation_engine.create_interpolation_model()
        
        fig = interpolation_engine.plot_interpolation_model(degrees, do_plot)
        
        return models, fig