# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_ERODE_METADATA = Metadata(
    id="a492ce6bed6371b601abe48af82f65a25d3c76e6.boutiques",
    name="metric-erode",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


MetricErodeParameters = typing.TypedDict('MetricErodeParameters', {
    "__STYXTYPE__": typing.Literal["metric-erode"],
    "metric": InputPathType,
    "surface": InputPathType,
    "distance": float,
    "metric_out": str,
    "opt_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[str | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
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
        "metric-erode": metric_erode_cargs,
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
        "metric-erode": metric_erode_outputs,
    }.get(t)


class MetricErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_erode_params(
    metric: InputPathType,
    surface: InputPathType,
    distance: float,
    metric_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> MetricErodeParameters:
    """
    Build parameters.
    
    Args:
        metric: the metric file to erode.
        surface: the surface to compute on.
        distance: distance in mm to erode.
        metric_out: the output metric.
        opt_roi_roi_metric: assume values outside this roi are nonzero: metric\
            file, positive values denote vertices that have data.
        opt_column_column: select a single column to erode: the column number\
            or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-erode",
        "metric": metric,
        "surface": surface,
        "distance": distance,
        "metric_out": metric_out,
    }
    if opt_roi_roi_metric is not None:
        params["opt_roi_roi_metric"] = opt_roi_roi_metric
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    return params


def metric_erode_cargs(
    params: MetricErodeParameters,
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
    cargs.append("-metric-erode")
    cargs.append(execution.input_file(params.get("metric")))
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(str(params.get("distance")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_roi_roi_metric") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_metric"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    return cargs


def metric_erode_outputs(
    params: MetricErodeParameters,
    execution: Execution,
) -> MetricErodeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricErodeOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def metric_erode_execute(
    params: MetricErodeParameters,
    execution: Execution,
) -> MetricErodeOutputs:
    """
    Erode a metric file.
    
    Around each vertex with a value of zero, set surrounding vertices to zero.
    The surrounding vertices are all immediate neighbors and all vertices within
    the specified distance.
    
    Note that the -corrected-areas option uses an approximate correction for
    distance along the surface.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricErodeOutputs`).
    """
    params = execution.params(params)
    cargs = metric_erode_cargs(params, execution)
    ret = metric_erode_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_erode(
    metric: InputPathType,
    surface: InputPathType,
    distance: float,
    metric_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> MetricErodeOutputs:
    """
    Erode a metric file.
    
    Around each vertex with a value of zero, set surrounding vertices to zero.
    The surrounding vertices are all immediate neighbors and all vertices within
    the specified distance.
    
    Note that the -corrected-areas option uses an approximate correction for
    distance along the surface.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        metric: the metric file to erode.
        surface: the surface to compute on.
        distance: distance in mm to erode.
        metric_out: the output metric.
        opt_roi_roi_metric: assume values outside this roi are nonzero: metric\
            file, positive values denote vertices that have data.
        opt_column_column: select a single column to erode: the column number\
            or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricErodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_ERODE_METADATA)
    params = metric_erode_params(
        metric=metric,
        surface=surface,
        distance=distance,
        metric_out=metric_out,
        opt_roi_roi_metric=opt_roi_roi_metric,
        opt_column_column=opt_column_column,
        opt_corrected_areas_area_metric=opt_corrected_areas_area_metric,
    )
    return metric_erode_execute(params, execution)


__all__ = [
    "METRIC_ERODE_METADATA",
    "MetricErodeOutputs",
    "MetricErodeParameters",
    "metric_erode",
    "metric_erode_params",
]
