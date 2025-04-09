# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_CREATE_DENSE_FROM_TEMPLATE_METADATA = Metadata(
    id="da0229304fc3d58a84e54c110629007c8a6c124b.boutiques",
    name="cifti-create-dense-from-template",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiCreateDenseFromTemplateSeriesParameters = typing.TypedDict('CiftiCreateDenseFromTemplateSeriesParameters', {
    "__STYX_TYPE__": typing.Literal["series"],
    "step": float,
    "start": float,
    "opt_unit_unit": typing.NotRequired[str | None],
})


CiftiCreateDenseFromTemplateVolumeAllParameters = typing.TypedDict('CiftiCreateDenseFromTemplateVolumeAllParameters', {
    "__STYX_TYPE__": typing.Literal["volume_all"],
    "volume_in": InputPathType,
    "opt_from_cropped": bool,
})


CiftiCreateDenseFromTemplateCiftiParameters = typing.TypedDict('CiftiCreateDenseFromTemplateCiftiParameters', {
    "__STYX_TYPE__": typing.Literal["cifti"],
    "cifti_in": InputPathType,
})


CiftiCreateDenseFromTemplateMetricParameters = typing.TypedDict('CiftiCreateDenseFromTemplateMetricParameters', {
    "__STYX_TYPE__": typing.Literal["metric"],
    "structure": str,
    "metric_in": InputPathType,
})


CiftiCreateDenseFromTemplateLabelParameters = typing.TypedDict('CiftiCreateDenseFromTemplateLabelParameters', {
    "__STYX_TYPE__": typing.Literal["label"],
    "structure": str,
    "label_in": InputPathType,
})


CiftiCreateDenseFromTemplateVolumeParameters = typing.TypedDict('CiftiCreateDenseFromTemplateVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["volume"],
    "structure": str,
    "volume_in": InputPathType,
    "opt_from_cropped": bool,
})


CiftiCreateDenseFromTemplateParameters = typing.TypedDict('CiftiCreateDenseFromTemplateParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-create-dense-from-template"],
    "template_cifti": InputPathType,
    "cifti_out": str,
    "series": typing.NotRequired[CiftiCreateDenseFromTemplateSeriesParameters | None],
    "volume_all": typing.NotRequired[CiftiCreateDenseFromTemplateVolumeAllParameters | None],
    "opt_label_collision_action": typing.NotRequired[str | None],
    "cifti": typing.NotRequired[list[CiftiCreateDenseFromTemplateCiftiParameters] | None],
    "metric": typing.NotRequired[list[CiftiCreateDenseFromTemplateMetricParameters] | None],
    "label": typing.NotRequired[list[CiftiCreateDenseFromTemplateLabelParameters] | None],
    "volume": typing.NotRequired[list[CiftiCreateDenseFromTemplateVolumeParameters] | None],
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
        "cifti-create-dense-from-template": cifti_create_dense_from_template_cargs,
        "series": cifti_create_dense_from_template_series_cargs,
        "volume_all": cifti_create_dense_from_template_volume_all_cargs,
        "cifti": cifti_create_dense_from_template_cifti_cargs,
        "metric": cifti_create_dense_from_template_metric_cargs,
        "label": cifti_create_dense_from_template_label_cargs,
        "volume": cifti_create_dense_from_template_volume_cargs,
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
        "cifti-create-dense-from-template": cifti_create_dense_from_template_outputs,
    }.get(t)


def cifti_create_dense_from_template_series_params(
    step: float,
    start: float,
    opt_unit_unit: str | None = None,
) -> CiftiCreateDenseFromTemplateSeriesParameters:
    """
    Build parameters.
    
    Args:
        step: increment between series points.
        start: start value of the series.
        opt_unit_unit: select unit for series (default SECOND): unit identifier.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "series",
        "step": step,
        "start": start,
    }
    if opt_unit_unit is not None:
        params["opt_unit_unit"] = opt_unit_unit
    return params


def cifti_create_dense_from_template_series_cargs(
    params: CiftiCreateDenseFromTemplateSeriesParameters,
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
    cargs.append("-series")
    cargs.append(str(params.get("step")))
    cargs.append(str(params.get("start")))
    if params.get("opt_unit_unit") is not None:
        cargs.extend([
            "-unit",
            params.get("opt_unit_unit")
        ])
    return cargs


def cifti_create_dense_from_template_volume_all_params(
    volume_in: InputPathType,
    opt_from_cropped: bool = False,
) -> CiftiCreateDenseFromTemplateVolumeAllParameters:
    """
    Build parameters.
    
    Args:
        volume_in: the input volume file.
        opt_from_cropped: the input is cropped to the size of the voxel data in\
            the template file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume_all",
        "volume_in": volume_in,
        "opt_from_cropped": opt_from_cropped,
    }
    return params


def cifti_create_dense_from_template_volume_all_cargs(
    params: CiftiCreateDenseFromTemplateVolumeAllParameters,
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
    cargs.append(execution.input_file(params.get("volume_in")))
    if params.get("opt_from_cropped"):
        cargs.append("-from-cropped")
    return cargs


def cifti_create_dense_from_template_cifti_params(
    cifti_in: InputPathType,
) -> CiftiCreateDenseFromTemplateCiftiParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: cifti file containing input data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti",
        "cifti_in": cifti_in,
    }
    return params


def cifti_create_dense_from_template_cifti_cargs(
    params: CiftiCreateDenseFromTemplateCiftiParameters,
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
    cargs.append("-cifti")
    cargs.append(execution.input_file(params.get("cifti_in")))
    return cargs


def cifti_create_dense_from_template_metric_params(
    structure: str,
    metric_in: InputPathType,
) -> CiftiCreateDenseFromTemplateMetricParameters:
    """
    Build parameters.
    
    Args:
        structure: which structure to put the metric file into.
        metric_in: input metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric",
        "structure": structure,
        "metric_in": metric_in,
    }
    return params


def cifti_create_dense_from_template_metric_cargs(
    params: CiftiCreateDenseFromTemplateMetricParameters,
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
    cargs.append(execution.input_file(params.get("metric_in")))
    return cargs


def cifti_create_dense_from_template_label_params(
    structure: str,
    label_in: InputPathType,
) -> CiftiCreateDenseFromTemplateLabelParameters:
    """
    Build parameters.
    
    Args:
        structure: which structure to put the label file into.
        label_in: input label file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label",
        "structure": structure,
        "label_in": label_in,
    }
    return params


def cifti_create_dense_from_template_label_cargs(
    params: CiftiCreateDenseFromTemplateLabelParameters,
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
    cargs.append(execution.input_file(params.get("label_in")))
    return cargs


def cifti_create_dense_from_template_volume_params(
    structure: str,
    volume_in: InputPathType,
    opt_from_cropped: bool = False,
) -> CiftiCreateDenseFromTemplateVolumeParameters:
    """
    Build parameters.
    
    Args:
        structure: which structure to put the volume file into.
        volume_in: the input volume file.
        opt_from_cropped: the input is cropped to the size of the volume\
            structure.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume",
        "structure": structure,
        "volume_in": volume_in,
        "opt_from_cropped": opt_from_cropped,
    }
    return params


def cifti_create_dense_from_template_volume_cargs(
    params: CiftiCreateDenseFromTemplateVolumeParameters,
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
    cargs.append(execution.input_file(params.get("volume_in")))
    if params.get("opt_from_cropped"):
        cargs.append("-from-cropped")
    return cargs


class CiftiCreateDenseFromTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_dense_from_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_dense_from_template_params(
    template_cifti: InputPathType,
    cifti_out: str,
    series: CiftiCreateDenseFromTemplateSeriesParameters | None = None,
    volume_all: CiftiCreateDenseFromTemplateVolumeAllParameters | None = None,
    opt_label_collision_action: str | None = None,
    cifti: list[CiftiCreateDenseFromTemplateCiftiParameters] | None = None,
    metric: list[CiftiCreateDenseFromTemplateMetricParameters] | None = None,
    label: list[CiftiCreateDenseFromTemplateLabelParameters] | None = None,
    volume: list[CiftiCreateDenseFromTemplateVolumeParameters] | None = None,
) -> CiftiCreateDenseFromTemplateParameters:
    """
    Build parameters.
    
    Args:
        template_cifti: file to match brainordinates of.
        cifti_out: the output cifti file.
        series: make a dtseries file instead of a dscalar.
        volume_all: specify an input volume file for all voxel data.
        opt_label_collision_action: how to handle conflicts between label keys:\
            'ERROR', 'SURFACES_FIRST', or 'LEGACY', default 'ERROR', use 'LEGACY'\
            to match v1.4.2 and earlier.
        cifti: use input data from a cifti file.
        metric: use input data from a metric file.
        label: use input data from surface label files.
        volume: use a volume file for a single volume structure's data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-create-dense-from-template",
        "template_cifti": template_cifti,
        "cifti_out": cifti_out,
    }
    if series is not None:
        params["series"] = series
    if volume_all is not None:
        params["volume_all"] = volume_all
    if opt_label_collision_action is not None:
        params["opt_label_collision_action"] = opt_label_collision_action
    if cifti is not None:
        params["cifti"] = cifti
    if metric is not None:
        params["metric"] = metric
    if label is not None:
        params["label"] = label
    if volume is not None:
        params["volume"] = volume
    return params


def cifti_create_dense_from_template_cargs(
    params: CiftiCreateDenseFromTemplateParameters,
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
    cargs.append("-cifti-create-dense-from-template")
    cargs.append(execution.input_file(params.get("template_cifti")))
    cargs.append(params.get("cifti_out"))
    if params.get("series") is not None:
        cargs.extend(dyn_cargs(params.get("series")["__STYXTYPE__"])(params.get("series"), execution))
    if params.get("volume_all") is not None:
        cargs.extend(dyn_cargs(params.get("volume_all")["__STYXTYPE__"])(params.get("volume_all"), execution))
    if params.get("opt_label_collision_action") is not None:
        cargs.extend([
            "-label-collision",
            params.get("opt_label_collision_action")
        ])
    if params.get("cifti") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("cifti")] for a in c])
    if params.get("metric") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("metric")] for a in c])
    if params.get("label") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("label")] for a in c])
    if params.get("volume") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("volume")] for a in c])
    return cargs


def cifti_create_dense_from_template_outputs(
    params: CiftiCreateDenseFromTemplateParameters,
    execution: Execution,
) -> CiftiCreateDenseFromTemplateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiCreateDenseFromTemplateOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_create_dense_from_template_execute(
    params: CiftiCreateDenseFromTemplateParameters,
    execution: Execution,
) -> CiftiCreateDenseFromTemplateOutputs:
    """
    Create cifti with matching dense map.
    
    This command helps you make a new dscalar, dtseries, or dlabel cifti file
    that matches the brainordinate space used in another cifti file. The
    template file must have the desired brainordinate space in the mapping along
    the column direction (for dtseries, dscalar, dlabel, and symmetric dconn
    this is always the case). All input cifti files must have a brain models
    mapping along column and use the same volume space and/or surface vertex
    count as the template for structures that they contain. If any input files
    contain label data, then input files with non-label data are not allowed,
    and the -series option may not be used.
    
    Any structure that isn't covered by an input is filled with zeros or the
    unlabeled key.
    
    The <structure> argument of -metric, -label or -volume must be one of the
    following:
    
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
    THALAMUS_RIGHT
    
    The argument to -unit must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateDenseFromTemplateOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_create_dense_from_template_cargs(params, execution)
    ret = cifti_create_dense_from_template_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_create_dense_from_template(
    template_cifti: InputPathType,
    cifti_out: str,
    series: CiftiCreateDenseFromTemplateSeriesParameters | None = None,
    volume_all: CiftiCreateDenseFromTemplateVolumeAllParameters | None = None,
    opt_label_collision_action: str | None = None,
    cifti: list[CiftiCreateDenseFromTemplateCiftiParameters] | None = None,
    metric: list[CiftiCreateDenseFromTemplateMetricParameters] | None = None,
    label: list[CiftiCreateDenseFromTemplateLabelParameters] | None = None,
    volume: list[CiftiCreateDenseFromTemplateVolumeParameters] | None = None,
    runner: Runner | None = None,
) -> CiftiCreateDenseFromTemplateOutputs:
    """
    Create cifti with matching dense map.
    
    This command helps you make a new dscalar, dtseries, or dlabel cifti file
    that matches the brainordinate space used in another cifti file. The
    template file must have the desired brainordinate space in the mapping along
    the column direction (for dtseries, dscalar, dlabel, and symmetric dconn
    this is always the case). All input cifti files must have a brain models
    mapping along column and use the same volume space and/or surface vertex
    count as the template for structures that they contain. If any input files
    contain label data, then input files with non-label data are not allowed,
    and the -series option may not be used.
    
    Any structure that isn't covered by an input is filled with zeros or the
    unlabeled key.
    
    The <structure> argument of -metric, -label or -volume must be one of the
    following:
    
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
    THALAMUS_RIGHT
    
    The argument to -unit must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        template_cifti: file to match brainordinates of.
        cifti_out: the output cifti file.
        series: make a dtseries file instead of a dscalar.
        volume_all: specify an input volume file for all voxel data.
        opt_label_collision_action: how to handle conflicts between label keys:\
            'ERROR', 'SURFACES_FIRST', or 'LEGACY', default 'ERROR', use 'LEGACY'\
            to match v1.4.2 and earlier.
        cifti: use input data from a cifti file.
        metric: use input data from a metric file.
        label: use input data from surface label files.
        volume: use a volume file for a single volume structure's data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateDenseFromTemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CREATE_DENSE_FROM_TEMPLATE_METADATA)
    params = cifti_create_dense_from_template_params(
        template_cifti=template_cifti,
        cifti_out=cifti_out,
        series=series,
        volume_all=volume_all,
        opt_label_collision_action=opt_label_collision_action,
        cifti=cifti,
        metric=metric,
        label=label,
        volume=volume,
    )
    return cifti_create_dense_from_template_execute(params, execution)


__all__ = [
    "CIFTI_CREATE_DENSE_FROM_TEMPLATE_METADATA",
    "CiftiCreateDenseFromTemplateCiftiParameters",
    "CiftiCreateDenseFromTemplateLabelParameters",
    "CiftiCreateDenseFromTemplateMetricParameters",
    "CiftiCreateDenseFromTemplateOutputs",
    "CiftiCreateDenseFromTemplateParameters",
    "CiftiCreateDenseFromTemplateSeriesParameters",
    "CiftiCreateDenseFromTemplateVolumeAllParameters",
    "CiftiCreateDenseFromTemplateVolumeParameters",
    "cifti_create_dense_from_template",
    "cifti_create_dense_from_template_cifti_params",
    "cifti_create_dense_from_template_label_params",
    "cifti_create_dense_from_template_metric_params",
    "cifti_create_dense_from_template_params",
    "cifti_create_dense_from_template_series_params",
    "cifti_create_dense_from_template_volume_all_params",
    "cifti_create_dense_from_template_volume_params",
]
