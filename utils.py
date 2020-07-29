from pathlib import Path
from typing import Tuple
import numpy as np
from nibabel import freesurfer


def load_data_cases_controls(input_cases_path: Path,
                             input_controls_path: Path) -> Tuple[np.ndarray, np.ndarray]:
    # 1-Dimensional arrays, of shape (num_vertices, )
    case_data = freesurfer.read_morph_data(input_cases_path)
    control_data = freesurfer.read_morph_data(input_controls_path)

    return case_data, control_data


def select_morph_vertices(cases_morph_mat: np.ndarray,
                          controls_morph_mat: np.ndarray,
                          threshold: float = 0.0) -> np.ndarray:
    # Look for the maximum values for the vertices, which in this case is scanning for the maximum value
    # across the IDCs, which is why we use axis=0
    max_vert_data_cases = np.max(cases_morph_mat,
                                 axis=0)
    max_vert_data_controls = np.max(controls_morph_mat,
                                    axis=0)

    # Then we get the indices at which the maximum vertices for both cases and controls is above 0
    selected_vertices = np.where((max_vert_data_cases > threshold) & (max_vert_data_controls > threshold))[0]

    return selected_vertices