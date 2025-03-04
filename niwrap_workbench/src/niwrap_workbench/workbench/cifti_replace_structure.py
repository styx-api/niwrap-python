# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_REPLACE_STRUCTURE_METADATA = Metadata(
    id="9c3e18b84a0136395940d5ee50cb45c790ea3cbb.boutiques",
    name="cifti-replace-structure",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiReplaceStructureVolumeAllParameters = typing.TypedDict('CiftiReplaceStructureVolumeAllParameters', {
    "__STYX_TYPE__": typing.Literal["volume_all"],
    "volume": InputPathType,
    "opt_from_cropped": bool,
})


CiftiReplaceStructureLabelParameters = typing.TypedDict('CiftiReplaceStructureLabelParameters', {
    "__STYX_TYPE__": typing.Literal["label"],
    "structure": str,
    "label": InputPathType,
})


CiftiReplaceStructureMetricParameters = typing.TypedDict('CiftiReplaceStructureMetricParameters', {
    "__STYX_TYPE__": typing.Literal["metric"],
    "structure": str,
    "metric": InputPathType,
})


CiftiReplaceStructureVolumeParameters = typing.TypedDict('CiftiReplaceStructureVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["volume"],
    "structure": str,
    "volume": InputPathType,
    "opt_from_cropped": bool,
})


CiftiReplaceStructureParameters = typing.TypedDict('CiftiReplaceStructureParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-replace-structure"],
    "cifti": str,
    "direction": str,
    "volume_all": typing.NotRequired[CiftiReplaceStructureVolumeAllParameters | None],
    "opt_discard_unused_labels": bool,
    "opt_label_collision_action": typing.NotRequired[str | None],
    "label": typing.NotRequired[list[CiftiReplaceStructureLabelParameters] | None],
    "metric": typing.NotRequired[list[CiftiReplaceStructureMetricParameters] | None],
    "volume": typing.NotRequired[list[CiftiReplaceStructureVolumeParameters] | None],
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
        "cifti-replace-structure": cifti_replace_structure_cargs,
        "volume_all": cifti_replace_structure_volume_all_cargs,
        "label": cifti_replace_structure_label_cargs,
        "metric": cifti_replace_structure_metric_cargs,
        "volume": cifti_replace_structure_volume_cargs,
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
    }.get(t)


def cifti_replace_structure_volume_all_params(
    volume: InputPathType,
    opt_from_cropped: bool = False,
) -> CiftiReplaceStructureVolumeAllParameters:
    """
    Build parameters.
    
    Args:
        volume: the input volume.
        opt_from_cropped: the input is cropped to the size of the data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume_all",
        "volume": volume,
        "opt_from_cropped": opt_from_cropped,
    }
    return params


def cifti_replace_structure_volume_all_cargs(
    params: CiftiReplaceStructureVolumeAllParameters,
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
    cargs.append("-volume-all")
    cargs.append(execution.input_file(params.get("volume")))
    if params.get("opt_from_cropped"):
        cargs.append("-from-cropped")
    return cargs


def cifti_replace_structure_label_params(
    structure: str,
    label: InputPathType,
) -> CiftiReplaceStructureLabelParameters:
    """
    Build parameters.
    
    Args:
        structure: the structure to replace the data of.
        label: the input label file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label",
        "structure": structure,
        "label": label,
    }
    return params


def cifti_replace_structure_label_cargs(
    params: CiftiReplaceStructureLabelParameters,
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
    cargs.append("-label")
    cargs.append(params.get("structure"))
    cargs.append(execution.input_file(params.get("label")))
    return cargs


def cifti_replace_structure_metric_params(
    structure: str,
    metric: InputPathType,
) -> CiftiReplaceStructureMetricParameters:
    """
    Build parameters.
    
    Args:
        structure: the structure to replace the data of.
        metric: the input metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric",
        "structure": structure,
        "metric": metric,
    }
    return params


def cifti_replace_structure_metric_cargs(
    params: CiftiReplaceStructureMetricParameters,
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
    cargs.append("-metric")
    cargs.append(params.get("structure"))
    cargs.append(execution.input_file(params.get("metric")))
    return cargs


def cifti_replace_structure_volume_params(
    structure: str,
    volume: InputPathType,
    opt_from_cropped: bool = False,
) -> CiftiReplaceStructureVolumeParameters:
    """
    Build parameters.
    
    Args:
        structure: the structure to replace the data of.
        volume: the input volume.
        opt_from_cropped: the input is cropped to the size of the component.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume",
        "structure": structure,
        "volume": volume,
        "opt_from_cropped": opt_from_cropped,
    }
    return params


def cifti_replace_structure_volume_cargs(
    params: CiftiReplaceStructureVolumeParameters,
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
    cargs.append(params.get("structure"))
    cargs.append(execution.input_file(params.get("volume")))
    if params.get("opt_from_cropped"):
        cargs.append("-from-cropped")
    return cargs


class CiftiReplaceStructureOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_replace_structure(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_replace_structure_params(
    cifti: str,
    direction: str,
    volume_all: CiftiReplaceStructureVolumeAllParameters | None = None,
    opt_discard_unused_labels: bool = False,
    opt_label_collision_action: str | None = None,
    label: list[CiftiReplaceStructureLabelParameters] | None = None,
    metric: list[CiftiReplaceStructureMetricParameters] | None = None,
    volume: list[CiftiReplaceStructureVolumeParameters] | None = None,
) -> CiftiReplaceStructureParameters:
    """
    Build parameters.
    
    Args:
        cifti: the cifti to modify.
        direction: which dimension to interpret as a single map, ROW or COLUMN.
        volume_all: replace the data in all volume components.
        opt_discard_unused_labels: when operating on a dlabel file, drop any\
            unused label keys from the label table.
        opt_label_collision_action: how to handle conflicts between label keys:\
            'ERROR', 'LEFT_SURFACE_FIRST', or 'LEGACY', default 'ERROR', use\
            'LEGACY' to match v1.4.2 and earlier.
        label: replace the data in a surface label component.
        metric: replace the data in a surface component.
        volume: replace the data in a volume component.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-replace-structure",
        "cifti": cifti,
        "direction": direction,
        "opt_discard_unused_labels": opt_discard_unused_labels,
    }
    if volume_all is not None:
        params["volume_all"] = volume_all
    if opt_label_collision_action is not None:
        params["opt_label_collision_action"] = opt_label_collision_action
    if label is not None:
        params["label"] = label
    if metric is not None:
        params["metric"] = metric
    if volume is not None:
        params["volume"] = volume
    return params


def cifti_replace_structure_cargs(
    params: CiftiReplaceStructureParameters,
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
    cargs.append("-cifti-replace-structure")
    cargs.append(params.get("cifti"))
    cargs.append(params.get("direction"))
    if params.get("volume_all") is not None:
        cargs.extend(dyn_cargs(params.get("volume_all")["__STYXTYPE__"])(params.get("volume_all"), execution))
    if params.get("opt_discard_unused_labels"):
        cargs.append("-discard-unused-labels")
    if params.get("opt_label_collision_action") is not None:
        cargs.extend([
            "-label-collision",
            params.get("opt_label_collision_action")
        ])
    if params.get("label") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("label")] for a in c])
    if params.get("metric") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("metric")] for a in c])
    if params.get("volume") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("volume")] for a in c])
    return cargs


def cifti_replace_structure_outputs(
    params: CiftiReplaceStructureParameters,
    execution: Execution,
) -> CiftiReplaceStructureOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiReplaceStructureOutputs(
        root=execution.output_file("."),
    )
    return ret


def cifti_replace_structure_execute(
    params: CiftiReplaceStructureParameters,
    execution: Execution,
) -> CiftiReplaceStructureOutputs:
    """
    Replace data in a structure in a cifti file.
    
    This is a fairly low-level command, you probably want to use
    -cifti-create-dense-from-template instead.
    
    You must specify at least one of -metric, -label, -volume, or -volume-all
    for this command to do anything. Input volumes must line up with the output
    of -cifti-separate. For dtseries/dscalar, use COLUMN, and if your dconn
    matrix will be fully symmetric, COLUMN is more efficient. The -volume-all
    option must not be specified when using a -volume option. A -metric option
    must not be specified when using a -label option, and is not recommended on
    a label-type cifti file. For each <structure> argument, use one of the
    following strings:
    
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
        NamedTuple of outputs (described in `CiftiReplaceStructureOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_replace_structure_cargs(params, execution)
    ret = cifti_replace_structure_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_replace_structure(
    cifti: str,
    direction: str,
    volume_all: CiftiReplaceStructureVolumeAllParameters | None = None,
    opt_discard_unused_labels: bool = False,
    opt_label_collision_action: str | None = None,
    label: list[CiftiReplaceStructureLabelParameters] | None = None,
    metric: list[CiftiReplaceStructureMetricParameters] | None = None,
    volume: list[CiftiReplaceStructureVolumeParameters] | None = None,
    runner: Runner | None = None,
) -> CiftiReplaceStructureOutputs:
    """
    Replace data in a structure in a cifti file.
    
    This is a fairly low-level command, you probably want to use
    -cifti-create-dense-from-template instead.
    
    You must specify at least one of -metric, -label, -volume, or -volume-all
    for this command to do anything. Input volumes must line up with the output
    of -cifti-separate. For dtseries/dscalar, use COLUMN, and if your dconn
    matrix will be fully symmetric, COLUMN is more efficient. The -volume-all
    option must not be specified when using a -volume option. A -metric option
    must not be specified when using a -label option, and is not recommended on
    a label-type cifti file. For each <structure> argument, use one of the
    following strings:
    
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
        cifti: the cifti to modify.
        direction: which dimension to interpret as a single map, ROW or COLUMN.
        volume_all: replace the data in all volume components.
        opt_discard_unused_labels: when operating on a dlabel file, drop any\
            unused label keys from the label table.
        opt_label_collision_action: how to handle conflicts between label keys:\
            'ERROR', 'LEFT_SURFACE_FIRST', or 'LEGACY', default 'ERROR', use\
            'LEGACY' to match v1.4.2 and earlier.
        label: replace the data in a surface label component.
        metric: replace the data in a surface component.
        volume: replace the data in a volume component.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiReplaceStructureOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_REPLACE_STRUCTURE_METADATA)
    params = cifti_replace_structure_params(
        cifti=cifti,
        direction=direction,
        volume_all=volume_all,
        opt_discard_unused_labels=opt_discard_unused_labels,
        opt_label_collision_action=opt_label_collision_action,
        label=label,
        metric=metric,
        volume=volume,
    )
    return cifti_replace_structure_execute(params, execution)


__all__ = [
    "CIFTI_REPLACE_STRUCTURE_METADATA",
    "CiftiReplaceStructureLabelParameters",
    "CiftiReplaceStructureMetricParameters",
    "CiftiReplaceStructureOutputs",
    "CiftiReplaceStructureParameters",
    "CiftiReplaceStructureVolumeAllParameters",
    "CiftiReplaceStructureVolumeParameters",
    "cifti_replace_structure",
    "cifti_replace_structure_label_params",
    "cifti_replace_structure_metric_params",
    "cifti_replace_structure_params",
    "cifti_replace_structure_volume_all_params",
    "cifti_replace_structure_volume_params",
]
