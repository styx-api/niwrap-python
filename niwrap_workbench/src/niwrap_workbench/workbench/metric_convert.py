# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_CONVERT_METADATA = Metadata(
    id="2d62355f182fd73a5faeb9eb4724469210621e2f.boutiques",
    name="metric-convert",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


MetricConvertToNiftiParameters = typing.TypedDict('MetricConvertToNiftiParameters', {
    "__STYXTYPE__": typing.Literal["to_nifti"],
    "metric_in": InputPathType,
    "nifti_out": str,
})


MetricConvertFromNiftiParameters = typing.TypedDict('MetricConvertFromNiftiParameters', {
    "__STYXTYPE__": typing.Literal["from_nifti"],
    "nifti_in": InputPathType,
    "surface_in": InputPathType,
    "metric_out": str,
})


MetricConvertParameters = typing.TypedDict('MetricConvertParameters', {
    "__STYXTYPE__": typing.Literal["metric-convert"],
    "to_nifti": typing.NotRequired[MetricConvertToNiftiParameters | None],
    "from_nifti": typing.NotRequired[MetricConvertFromNiftiParameters | None],
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
        "metric-convert": metric_convert_cargs,
        "to_nifti": metric_convert_to_nifti_cargs,
        "from_nifti": metric_convert_from_nifti_cargs,
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
        "metric-convert": metric_convert_outputs,
        "to_nifti": metric_convert_to_nifti_outputs,
        "from_nifti": metric_convert_from_nifti_outputs,
    }.get(t)


class MetricConvertToNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MetricConvertToNiftiParameters | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    nifti_out: OutputPathType
    """the output nifti file"""


def metric_convert_to_nifti_params(
    metric_in: InputPathType,
    nifti_out: str,
) -> MetricConvertToNiftiParameters:
    """
    Build parameters.
    
    Args:
        metric_in: the metric to convert.
        nifti_out: the output nifti file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "to_nifti",
        "metric_in": metric_in,
        "nifti_out": nifti_out,
    }
    return params


def metric_convert_to_nifti_cargs(
    params: MetricConvertToNiftiParameters,
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
    cargs.append("-to-nifti")
    cargs.append(execution.input_file(params.get("metric_in")))
    cargs.append(params.get("nifti_out"))
    return cargs


def metric_convert_to_nifti_outputs(
    params: MetricConvertToNiftiParameters,
    execution: Execution,
) -> MetricConvertToNiftiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricConvertToNiftiOutputs(
        root=execution.output_file("."),
        nifti_out=execution.output_file(params.get("nifti_out")),
    )
    return ret


class MetricConvertFromNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MetricConvertFromNiftiParameters | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


def metric_convert_from_nifti_params(
    nifti_in: InputPathType,
    surface_in: InputPathType,
    metric_out: str,
) -> MetricConvertFromNiftiParameters:
    """
    Build parameters.
    
    Args:
        nifti_in: the nifti file to convert.
        surface_in: surface file to use number of vertices and structure from.
        metric_out: the output metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "from_nifti",
        "nifti_in": nifti_in,
        "surface_in": surface_in,
        "metric_out": metric_out,
    }
    return params


def metric_convert_from_nifti_cargs(
    params: MetricConvertFromNiftiParameters,
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
    cargs.append("-from-nifti")
    cargs.append(execution.input_file(params.get("nifti_in")))
    cargs.append(execution.input_file(params.get("surface_in")))
    cargs.append(params.get("metric_out"))
    return cargs


def metric_convert_from_nifti_outputs(
    params: MetricConvertFromNiftiParameters,
    execution: Execution,
) -> MetricConvertFromNiftiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricConvertFromNiftiOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


class MetricConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    to_nifti: MetricConvertToNiftiOutputs | None
    """Outputs from `metric_convert_to_nifti_outputs`."""
    from_nifti: MetricConvertFromNiftiOutputs | None
    """Outputs from `metric_convert_from_nifti_outputs`."""


def metric_convert_params(
    to_nifti: MetricConvertToNiftiParameters | None = None,
    from_nifti: MetricConvertFromNiftiParameters | None = None,
) -> MetricConvertParameters:
    """
    Build parameters.
    
    Args:
        to_nifti: convert metric to nifti.
        from_nifti: convert nifti to metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-convert",
    }
    if to_nifti is not None:
        params["to_nifti"] = to_nifti
    if from_nifti is not None:
        params["from_nifti"] = from_nifti
    return params


def metric_convert_cargs(
    params: MetricConvertParameters,
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
    cargs.append("-metric-convert")
    if params.get("to_nifti") is not None:
        cargs.extend(dyn_cargs(params.get("to_nifti")["__STYXTYPE__"])(params.get("to_nifti"), execution))
    if params.get("from_nifti") is not None:
        cargs.extend(dyn_cargs(params.get("from_nifti")["__STYXTYPE__"])(params.get("from_nifti"), execution))
    return cargs


def metric_convert_outputs(
    params: MetricConvertParameters,
    execution: Execution,
) -> MetricConvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricConvertOutputs(
        root=execution.output_file("."),
        to_nifti=dyn_outputs(params.get("to_nifti")["__STYXTYPE__"])(params.get("to_nifti"), execution) if params.get("to_nifti") else None,
        from_nifti=dyn_outputs(params.get("from_nifti")["__STYXTYPE__"])(params.get("from_nifti"), execution) if params.get("from_nifti") else None,
    )
    return ret


def metric_convert_execute(
    params: MetricConvertParameters,
    execution: Execution,
) -> MetricConvertOutputs:
    """
    Convert metric file to fake nifti.
    
    The purpose of this command is to convert between metric files and nifti1 so
    that gifti-unaware programs can operate on the data. You must specify
    exactly one of the options.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricConvertOutputs`).
    """
    params = execution.params(params)
    cargs = metric_convert_cargs(params, execution)
    ret = metric_convert_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_convert(
    to_nifti: MetricConvertToNiftiParameters | None = None,
    from_nifti: MetricConvertFromNiftiParameters | None = None,
    runner: Runner | None = None,
) -> MetricConvertOutputs:
    """
    Convert metric file to fake nifti.
    
    The purpose of this command is to convert between metric files and nifti1 so
    that gifti-unaware programs can operate on the data. You must specify
    exactly one of the options.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        to_nifti: convert metric to nifti.
        from_nifti: convert nifti to metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_CONVERT_METADATA)
    params = metric_convert_params(
        to_nifti=to_nifti,
        from_nifti=from_nifti,
    )
    return metric_convert_execute(params, execution)


__all__ = [
    "METRIC_CONVERT_METADATA",
    "MetricConvertFromNiftiOutputs",
    "MetricConvertFromNiftiParameters",
    "MetricConvertOutputs",
    "MetricConvertParameters",
    "MetricConvertToNiftiOutputs",
    "MetricConvertToNiftiParameters",
    "metric_convert",
    "metric_convert_from_nifti_params",
    "metric_convert_params",
    "metric_convert_to_nifti_params",
]
