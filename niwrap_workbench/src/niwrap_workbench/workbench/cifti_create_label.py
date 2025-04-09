# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_CREATE_LABEL_METADATA = Metadata(
    id="2bf058c43e7a0c065eaedc3a853fa58976abb094.boutiques",
    name="cifti-create-label",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiCreateLabelVolumeParameters = typing.TypedDict('CiftiCreateLabelVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["volume"],
    "label_volume": InputPathType,
    "structure_label_volume": InputPathType,
})


CiftiCreateLabelLeftLabelParameters = typing.TypedDict('CiftiCreateLabelLeftLabelParameters', {
    "__STYX_TYPE__": typing.Literal["left_label"],
    "label": InputPathType,
    "opt_roi_left_roi_metric": typing.NotRequired[InputPathType | None],
})


CiftiCreateLabelRightLabelParameters = typing.TypedDict('CiftiCreateLabelRightLabelParameters', {
    "__STYX_TYPE__": typing.Literal["right_label"],
    "label": InputPathType,
    "opt_roi_right_roi_metric": typing.NotRequired[InputPathType | None],
})


CiftiCreateLabelCerebellumLabelParameters = typing.TypedDict('CiftiCreateLabelCerebellumLabelParameters', {
    "__STYX_TYPE__": typing.Literal["cerebellum_label"],
    "label": InputPathType,
    "opt_roi_cerebellum_roi_metric": typing.NotRequired[InputPathType | None],
})


CiftiCreateLabelParameters = typing.TypedDict('CiftiCreateLabelParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-create-label"],
    "cifti_out": str,
    "volume": typing.NotRequired[CiftiCreateLabelVolumeParameters | None],
    "left_label": typing.NotRequired[CiftiCreateLabelLeftLabelParameters | None],
    "right_label": typing.NotRequired[CiftiCreateLabelRightLabelParameters | None],
    "cerebellum_label": typing.NotRequired[CiftiCreateLabelCerebellumLabelParameters | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "cifti-create-label": cifti_create_label_cargs,
        "volume": cifti_create_label_volume_cargs,
        "left_label": cifti_create_label_left_label_cargs,
        "right_label": cifti_create_label_right_label_cargs,
        "cerebellum_label": cifti_create_label_cerebellum_label_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "cifti-create-label": cifti_create_label_outputs,
    }.get(t)


def cifti_create_label_volume_params(
    label_volume: InputPathType,
    structure_label_volume: InputPathType,
) -> CiftiCreateLabelVolumeParameters:
    """
    Build parameters.
    
    Args:
        label_volume: label volume file containing the data to be copied.
        structure_label_volume: label volume file that defines which voxels to\
            use.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume",
        "label_volume": label_volume,
        "structure_label_volume": structure_label_volume,
    }
    return params


def cifti_create_label_volume_cargs(
    params: CiftiCreateLabelVolumeParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-volume")
    cargs.append(execution.input_file(params.get("label_volume")))
    cargs.append(execution.input_file(params.get("structure_label_volume")))
    return cargs


def cifti_create_label_left_label_params(
    label: InputPathType,
    opt_roi_left_roi_metric: InputPathType | None = None,
) -> CiftiCreateLabelLeftLabelParameters:
    """
    Build parameters.
    
    Args:
        label: the label file.
        opt_roi_left_roi_metric: roi of vertices to use from left surface: the\
            ROI as a metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "left_label",
        "label": label,
    }
    if opt_roi_left_roi_metric is not None:
        params["opt_roi_left_roi_metric"] = opt_roi_left_roi_metric
    return params


def cifti_create_label_left_label_cargs(
    params: CiftiCreateLabelLeftLabelParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-left-label")
    cargs.append(execution.input_file(params.get("label")))
    if params.get("opt_roi_left_roi_metric") is not None:
        cargs.extend([
            "-roi-left",
            execution.input_file(params.get("opt_roi_left_roi_metric"))
        ])
    return cargs


def cifti_create_label_right_label_params(
    label: InputPathType,
    opt_roi_right_roi_metric: InputPathType | None = None,
) -> CiftiCreateLabelRightLabelParameters:
    """
    Build parameters.
    
    Args:
        label: the label file.
        opt_roi_right_roi_metric: roi of vertices to use from right surface:\
            the ROI as a metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "right_label",
        "label": label,
    }
    if opt_roi_right_roi_metric is not None:
        params["opt_roi_right_roi_metric"] = opt_roi_right_roi_metric
    return params


def cifti_create_label_right_label_cargs(
    params: CiftiCreateLabelRightLabelParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-right-label")
    cargs.append(execution.input_file(params.get("label")))
    if params.get("opt_roi_right_roi_metric") is not None:
        cargs.extend([
            "-roi-right",
            execution.input_file(params.get("opt_roi_right_roi_metric"))
        ])
    return cargs


def cifti_create_label_cerebellum_label_params(
    label: InputPathType,
    opt_roi_cerebellum_roi_metric: InputPathType | None = None,
) -> CiftiCreateLabelCerebellumLabelParameters:
    """
    Build parameters.
    
    Args:
        label: the label file.
        opt_roi_cerebellum_roi_metric: roi of vertices to use from right\
            surface: the ROI as a metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cerebellum_label",
        "label": label,
    }
    if opt_roi_cerebellum_roi_metric is not None:
        params["opt_roi_cerebellum_roi_metric"] = opt_roi_cerebellum_roi_metric
    return params


def cifti_create_label_cerebellum_label_cargs(
    params: CiftiCreateLabelCerebellumLabelParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-cerebellum-label")
    cargs.append(execution.input_file(params.get("label")))
    if params.get("opt_roi_cerebellum_roi_metric") is not None:
        cargs.extend([
            "-roi-cerebellum",
            execution.input_file(params.get("opt_roi_cerebellum_roi_metric"))
        ])
    return cargs


class CiftiCreateLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_label_params(
    cifti_out: str,
    volume: CiftiCreateLabelVolumeParameters | None = None,
    left_label: CiftiCreateLabelLeftLabelParameters | None = None,
    right_label: CiftiCreateLabelRightLabelParameters | None = None,
    cerebellum_label: CiftiCreateLabelCerebellumLabelParameters | None = None,
) -> CiftiCreateLabelParameters:
    """
    Build parameters.
    
    Args:
        cifti_out: the output cifti file.
        volume: volume component.
        left_label: label file for left surface.
        right_label: label for left surface.
        cerebellum_label: label for the cerebellum.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-create-label",
        "cifti_out": cifti_out,
    }
    if volume is not None:
        params["volume"] = volume
    if left_label is not None:
        params["left_label"] = left_label
    if right_label is not None:
        params["right_label"] = right_label
    if cerebellum_label is not None:
        params["cerebellum_label"] = cerebellum_label
    return params


def cifti_create_label_cargs(
    params: CiftiCreateLabelParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-label")
    cargs.append(params.get("cifti_out"))
    if params.get("volume") is not None:
        cargs.extend(dyn_cargs(params.get("volume")["__STYXTYPE__"])(params.get("volume"), execution))
    if params.get("left_label") is not None:
        cargs.extend(dyn_cargs(params.get("left_label")["__STYXTYPE__"])(params.get("left_label"), execution))
    if params.get("right_label") is not None:
        cargs.extend(dyn_cargs(params.get("right_label")["__STYXTYPE__"])(params.get("right_label"), execution))
    if params.get("cerebellum_label") is not None:
        cargs.extend(dyn_cargs(params.get("cerebellum_label")["__STYXTYPE__"])(params.get("cerebellum_label"), execution))
    return cargs


def cifti_create_label_outputs(
    params: CiftiCreateLabelParameters,
    execution: Execution,
) -> CiftiCreateLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiCreateLabelOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_create_label_execute(
    params: CiftiCreateLabelParameters,
    execution: Execution,
) -> CiftiCreateLabelOutputs:
    """
    Create a cifti label file.
    
    All input files must have the same number of columns/subvolumes. Only the
    specified components will be in the output cifti. At least one component
    must be specified.
    
    The -volume option requires two volume arguments, the label-volume argument
    contains all labels you want to display (e.g. nuclei of the thalamus),
    whereas the structure-label-volume argument contains all CIFTI voxel-based
    structures you want to include data within (e.g. THALAMUS_LEFT,
    THALAMUS_RIGHT, etc). See -volume-label-import and -volume-help for format
    details of label volume files. If you just want the labels in voxels to be
    the structure names, you may use the same file for both arguments. The
    structure-label-volume must use some of the label names from this list, all
    other label names in the structure-label-volume will be ignored:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateLabelOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_create_label_cargs(params, execution)
    ret = cifti_create_label_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_create_label(
    cifti_out: str,
    volume: CiftiCreateLabelVolumeParameters | None = None,
    left_label: CiftiCreateLabelLeftLabelParameters | None = None,
    right_label: CiftiCreateLabelRightLabelParameters | None = None,
    cerebellum_label: CiftiCreateLabelCerebellumLabelParameters | None = None,
    runner: Runner | None = None,
) -> CiftiCreateLabelOutputs:
    """
    Create a cifti label file.
    
    All input files must have the same number of columns/subvolumes. Only the
    specified components will be in the output cifti. At least one component
    must be specified.
    
    The -volume option requires two volume arguments, the label-volume argument
    contains all labels you want to display (e.g. nuclei of the thalamus),
    whereas the structure-label-volume argument contains all CIFTI voxel-based
    structures you want to include data within (e.g. THALAMUS_LEFT,
    THALAMUS_RIGHT, etc). See -volume-label-import and -volume-help for format
    details of label volume files. If you just want the labels in voxels to be
    the structure names, you may use the same file for both arguments. The
    structure-label-volume must use some of the label names from this list, all
    other label names in the structure-label-volume will be ignored:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_out: the output cifti file.
        volume: volume component.
        left_label: label file for left surface.
        right_label: label for left surface.
        cerebellum_label: label for the cerebellum.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CREATE_LABEL_METADATA)
    params = cifti_create_label_params(
        cifti_out=cifti_out,
        volume=volume,
        left_label=left_label,
        right_label=right_label,
        cerebellum_label=cerebellum_label,
    )
    return cifti_create_label_execute(params, execution)


__all__ = [
    "CIFTI_CREATE_LABEL_METADATA",
    "CiftiCreateLabelCerebellumLabelParameters",
    "CiftiCreateLabelLeftLabelParameters",
    "CiftiCreateLabelOutputs",
    "CiftiCreateLabelParameters",
    "CiftiCreateLabelRightLabelParameters",
    "CiftiCreateLabelVolumeParameters",
    "cifti_create_label",
    "cifti_create_label_cerebellum_label_params",
    "cifti_create_label_left_label_params",
    "cifti_create_label_params",
    "cifti_create_label_right_label_params",
    "cifti_create_label_volume_params",
]
