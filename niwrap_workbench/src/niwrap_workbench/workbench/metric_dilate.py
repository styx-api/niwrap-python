# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_DILATE_METADATA = Metadata(
    id="282a4511febb7319b4f30912bc37cef4227b8d67.boutiques",
    name="metric-dilate",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


MetricDilateParameters = typing.TypedDict('MetricDilateParameters', {
    "__STYX_TYPE__": typing.Literal["metric-dilate"],
    "metric": InputPathType,
    "surface": InputPathType,
    "distance": float,
    "metric_out": str,
    "opt_bad_vertex_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_data_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[str | None],
    "opt_nearest": bool,
    "opt_linear": bool,
    "opt_exponent_exponent": typing.NotRequired[float | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
    "opt_legacy_cutoff": bool,
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
        "metric-dilate": metric_dilate_cargs,
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
        "metric-dilate": metric_dilate_outputs,
    }.get(t)


class MetricDilateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_dilate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_dilate_params(
    metric: InputPathType,
    surface: InputPathType,
    distance: float,
    metric_out: str,
    opt_bad_vertex_roi_roi_metric: InputPathType | None = None,
    opt_data_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_nearest: bool = False,
    opt_linear: bool = False,
    opt_exponent_exponent: float | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_legacy_cutoff: bool = False,
) -> MetricDilateParameters:
    """
    Build parameters.
    
    Args:
        metric: the metric to dilate.
        surface: the surface to compute on.
        distance: distance in mm to dilate.
        metric_out: the output metric.
        opt_bad_vertex_roi_roi_metric: specify an roi of vertices to overwrite,\
            rather than vertices with value zero: metric file, positive values\
            denote vertices to have their values replaced.
        opt_data_roi_roi_metric: specify an roi of where there is data: metric\
            file, positive values denote vertices that have data.
        opt_column_column: select a single column to dilate: the column number\
            or name.
        opt_nearest: use the nearest good value instead of a weighted average.
        opt_linear: fill in values with linear interpolation along strongest\
            gradient.
        opt_exponent_exponent: use a different exponent in the weighting\
            function: exponent 'n' to use in (area / (distance ^ n)) as the\
            weighting function (default 6).
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        opt_legacy_cutoff: use the v1.3.2 method of choosing how many vertices\
            to use when calulating the dilated value with weighted method.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-dilate",
        "metric": metric,
        "surface": surface,
        "distance": distance,
        "metric_out": metric_out,
        "opt_nearest": opt_nearest,
        "opt_linear": opt_linear,
        "opt_legacy_cutoff": opt_legacy_cutoff,
    }
    if opt_bad_vertex_roi_roi_metric is not None:
        params["opt_bad_vertex_roi_roi_metric"] = opt_bad_vertex_roi_roi_metric
    if opt_data_roi_roi_metric is not None:
        params["opt_data_roi_roi_metric"] = opt_data_roi_roi_metric
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if opt_exponent_exponent is not None:
        params["opt_exponent_exponent"] = opt_exponent_exponent
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    return params


def metric_dilate_cargs(
    params: MetricDilateParameters,
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
    cargs.append("-metric-dilate")
    cargs.append(execution.input_file(params.get("metric")))
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(str(params.get("distance")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_bad_vertex_roi_roi_metric") is not None:
        cargs.extend([
            "-bad-vertex-roi",
            execution.input_file(params.get("opt_bad_vertex_roi_roi_metric"))
        ])
    if params.get("opt_data_roi_roi_metric") is not None:
        cargs.extend([
            "-data-roi",
            execution.input_file(params.get("opt_data_roi_roi_metric"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("opt_nearest"):
        cargs.append("-nearest")
    if params.get("opt_linear"):
        cargs.append("-linear")
    if params.get("opt_exponent_exponent") is not None:
        cargs.extend([
            "-exponent",
            str(params.get("opt_exponent_exponent"))
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    if params.get("opt_legacy_cutoff"):
        cargs.append("-legacy-cutoff")
    return cargs


def metric_dilate_outputs(
    params: MetricDilateParameters,
    execution: Execution,
) -> MetricDilateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricDilateOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def metric_dilate_execute(
    params: MetricDilateParameters,
    execution: Execution,
) -> MetricDilateOutputs:
    """
    Dilate a metric file.
    
    For all metric vertices that are designated as bad, if they neighbor a
    non-bad vertex with data or are within the specified distance of such a
    vertex, replace the value with a distance-based weighted average of nearby
    non-bad vertices that have data, otherwise set the value to zero. No matter
    how small <distance> is, dilation will always use at least the immediate
    neighbor vertices. If -nearest is specified, it will use the value from the
    closest non-bad vertex with data within range instead of a weighted average.
    
    If -bad-vertex-roi is specified, all vertices with a positive ROI value are
    bad. If it is not specified, only vertices that have data, with a value of
    zero, are bad. If -data-roi is not specified, all vertices are assumed to
    have data.
    
    Note that the -corrected-areas option uses an approximate correction for the
    change in distances along a group average surface.
    
    To get the behavior of version 1.3.2 or earlier, use '-legacy-cutoff
    -exponent 2'.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricDilateOutputs`).
    """
    params = execution.params(params)
    cargs = metric_dilate_cargs(params, execution)
    ret = metric_dilate_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_dilate(
    metric: InputPathType,
    surface: InputPathType,
    distance: float,
    metric_out: str,
    opt_bad_vertex_roi_roi_metric: InputPathType | None = None,
    opt_data_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_nearest: bool = False,
    opt_linear: bool = False,
    opt_exponent_exponent: float | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_legacy_cutoff: bool = False,
    runner: Runner | None = None,
) -> MetricDilateOutputs:
    """
    Dilate a metric file.
    
    For all metric vertices that are designated as bad, if they neighbor a
    non-bad vertex with data or are within the specified distance of such a
    vertex, replace the value with a distance-based weighted average of nearby
    non-bad vertices that have data, otherwise set the value to zero. No matter
    how small <distance> is, dilation will always use at least the immediate
    neighbor vertices. If -nearest is specified, it will use the value from the
    closest non-bad vertex with data within range instead of a weighted average.
    
    If -bad-vertex-roi is specified, all vertices with a positive ROI value are
    bad. If it is not specified, only vertices that have data, with a value of
    zero, are bad. If -data-roi is not specified, all vertices are assumed to
    have data.
    
    Note that the -corrected-areas option uses an approximate correction for the
    change in distances along a group average surface.
    
    To get the behavior of version 1.3.2 or earlier, use '-legacy-cutoff
    -exponent 2'.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        metric: the metric to dilate.
        surface: the surface to compute on.
        distance: distance in mm to dilate.
        metric_out: the output metric.
        opt_bad_vertex_roi_roi_metric: specify an roi of vertices to overwrite,\
            rather than vertices with value zero: metric file, positive values\
            denote vertices to have their values replaced.
        opt_data_roi_roi_metric: specify an roi of where there is data: metric\
            file, positive values denote vertices that have data.
        opt_column_column: select a single column to dilate: the column number\
            or name.
        opt_nearest: use the nearest good value instead of a weighted average.
        opt_linear: fill in values with linear interpolation along strongest\
            gradient.
        opt_exponent_exponent: use a different exponent in the weighting\
            function: exponent 'n' to use in (area / (distance ^ n)) as the\
            weighting function (default 6).
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        opt_legacy_cutoff: use the v1.3.2 method of choosing how many vertices\
            to use when calulating the dilated value with weighted method.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricDilateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_DILATE_METADATA)
    params = metric_dilate_params(
        metric=metric,
        surface=surface,
        distance=distance,
        metric_out=metric_out,
        opt_bad_vertex_roi_roi_metric=opt_bad_vertex_roi_roi_metric,
        opt_data_roi_roi_metric=opt_data_roi_roi_metric,
        opt_column_column=opt_column_column,
        opt_nearest=opt_nearest,
        opt_linear=opt_linear,
        opt_exponent_exponent=opt_exponent_exponent,
        opt_corrected_areas_area_metric=opt_corrected_areas_area_metric,
        opt_legacy_cutoff=opt_legacy_cutoff,
    )
    return metric_dilate_execute(params, execution)


__all__ = [
    "METRIC_DILATE_METADATA",
    "MetricDilateOutputs",
    "MetricDilateParameters",
    "metric_dilate",
    "metric_dilate_params",
]
