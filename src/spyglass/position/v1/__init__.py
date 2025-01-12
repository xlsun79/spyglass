from .dlc_reader import do_pose_estimation, read_yaml, save_yaml
from .dlc_utils import (
    _convert_mp4,
    check_videofile,
    find_full_path,
    find_root_directory,
    get_dlc_processed_data_dir,
    get_dlc_root_data_dir,
    get_video_path,
)
from .position_dlc_centroid import DLCCentroid, DLCCentroidParams, DLCCentroidSelection
from .position_dlc_cohort import DLCSmoothInterpCohort, DLCSmoothInterpCohortSelection
from .position_dlc_model import (
    DLCModel,
    DLCModelEvaluation,
    DLCModelInput,
    DLCModelParams,
    DLCModelSelection,
    DLCModelSource,
)
from .position_dlc_orient import (
    DLCOrientation,
    DLCOrientationParams,
    DLCOrientationSelection,
)
from .position_dlc_pose_estimation import DLCPoseEstimation, DLCPoseEstimationSelection
from .position_dlc_position import (
    DLCSmoothInterp,
    DLCSmoothInterpParams,
    DLCSmoothInterpSelection,
)
from .position_dlc_project import BodyPart, DLCProject
from .position_dlc_selection import (
    DLCPosSelection,
    DLCPosV1,
    DLCPosVideo,
    DLCPosVideoParams,
    DLCPosVideoSelection,
)
from .position_dlc_training import (
    DLCModelTraining,
    DLCModelTrainingParams,
    DLCModelTrainingSelection,
)
from .position_trodes_position import (
    TrodesPosParams,
    TrodesPosSelection,
    TrodesPosV1,
    TrodesPosVideo,
)


def schemas():
    return _schemas


_schemas = [
    "position_dlc_project",
    "position_dlc_training",
    "position_dlc_model",
    "position_dlc_pose_estimation",
    "position_dlc_position",
    "position_dlc_cohort",
    "position_dlc_centroid",
    "position_dlc_orient",
    "position_dlc_selection",
    "position_trodes_position",
]
